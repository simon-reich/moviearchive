from modules.es.types.search_queries import BasicSearch
from modules.es.dtos.search_dto import BasicSearchDto
from modules.es.utils.mapping import map_imdbApiSchema_to_indexSchema, getImdbApiKeys
from modules.es.schemas.schema_moviearchive import get_movieIndex_schema
from modules.imdbApi.utils.mapping import map_movie_to_indexSchema
from pathlib import Path
import glob
import json

PATH_TO_MOVIE_FILES = '../movie_data/'


class EsService:
    def createIndex(self, es_obj):
        return es_obj.es.indices.create(index=es_obj.name, body=get_movieIndex_schema())


    def getAllIndices(self, es_obj):  
        list_of_indicies = []
        for index in es_obj.es.indices.get_alias("*"):
            list_of_indicies.append(index)
            print(index)
        return list_of_indicies


    def getIndexInfo(self, es_obj):
        indexName = es_obj.name
        index = es_obj.es.indicies.get_alias(indexName)
        # Query here...
        return index


    def exactSearch(self, es_obj, dto):
        index = es_obj.name
        field = dto.field
        value = dto.value
        query = BasicSearch().exact_search_query(field, value)
        print(query)
        size = dto.size
        search_results = es_obj.es.search(index=index, body=query, size=size)
        hits = [doc for doc in search_results['hits']['hits']]
        for hit in hits:
            print(hit['_source']['title'])
        return hits


    def singleFieldSearch(self, es_obj, dto):
        index = es_obj.name
        field = dto.field.lower()
        value = dto.value.lower()
        query = BasicSearch().single_field_query(field, value)
        size = dto.size
        search_results = es_obj.es.search(index=index, body=query, size=size)
        hits = [doc for doc in search_results['hits']['hits']]
        for hit in hits:
            print(hit['_source']['title'])
        return hits


    def multiFieldSearch(self, es_obj, dto):
        index = es_obj.name
        value = dto.value.lower()
        query = BasicSearch().std_search_query(value)
        print(query)
        size = dto.size
        search_results = es_obj.es.search(index=index, body=query, size=size)
        hits = [doc for doc in search_results['hits']['hits']]
        for hit in hits:
            print(hit['_source']['title'])
        return hits


    def advancedSearch(self, es_obj, dto):
        index = es_obj.name
        parameters = {}
        for key, value in dto.parameters.items():
            print(key)
            print(value)
            if value and isinstance(value, str):
                parameters[key] = value.lower()
            elif value and isinstance(value, int):
                parameters[key] = value
            elif value and isinstance(value, list):
                parameters[key] = [item.lower() for item in value]
        print("PARAMETERS: ")
        print(parameters)
        # query = BasicSearch().std_search_query(value)
        size = dto.size
        # search_results = es_obj.es.search(index=index, body=query, size=size)
        # hits = [doc for doc in search_results['hits']['hits']]
        # for hit in hits:
        #     print(hit['_source']['title'])
        # return hits


    def getDataById(self, es_obj, id):
        index = es_obj.name
        field = 'imdbID'
        value = id.lower()
        query = BasicSearch().exact_search_query(field, value)
        search_results = es_obj.es.search(index=index, body=query)
        hits = [doc for doc in search_results['hits']['hits']]
        for hit in hits:
            print(hit['_source']['title'])
        return hits


    def getDistinctValues(self, es_obj, field):
        index = es_obj.name
        query = BasicSearch().distinct_values_from_field_query(field)
        print(query)
        search_results = es_obj.es.search(index=index, body=query, size=0)
        values = search_results['aggregations']['field-values']['buckets']
        return values      


    def indexData(self, es_obj, id, data):
        if not self.duplicationCheck(es_obj, id):
            es_obj.es.index(index=es_obj.name, body=data, refresh=True)
            if self.duplicationCheck(es_obj, id):
                print(f'movie "{data["title"]}" indexed')
                return 201, {'Etag': 'some-opaque-string'}
            else:
                return 409, {'Etag': 'some-opaque-string'}
        else:
            print('data is already indexed')


    def indexFolder(self, es_obj):
        path = PATH_TO_MOVIE_FILES
        if Path(path).exists():
            files = glob.glob(f'{path}/*.json')
            for file in files:
                with Path(file).open('r') as moviefile:
                    movie = json.load(moviefile)
                    if self.checkStructure(list(movie)):
                        movie_mapped = map_movie_to_indexSchema(movie)
                        self.indexData(es_obj, movie_mapped['imdbID'], movie_mapped)


    def duplicationCheck(self, es_obj, id):
        query = {
            "query": {
                "term": {
                    "imdbID": id
                }
            }
        }
        result = es_obj.es.search(index=es_obj.name, body=query)
        if result['hits']['total']['value'] == 0:
            return False
        else:
            return True


    def checkStructure(self, list_of_keys):
        if list_of_keys == getImdbApiKeys():
            return True
        else:
            print('no movie file')
            return False

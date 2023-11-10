from src.modules.es.types.search_queries import BasicSearch
from src.modules.es.dtos.search_dto import BasicSearchDto
from src.modules.es.schemas.schema_tmdb import get_tmdb_schema
from src.modules.es.utils.schema_controller import schemas, mapping_to_schema
from src.modules.es.utils.mapping import map_movie_to_index_schema, map_movie_to_index_schema_2, get_keys_of_given_schema
from src.modules.db.index.db_index_service import DbIndexService

from pathlib import Path
import glob
import json
import os

PATH_TO_MOVIE_FILES = '../movie_data'


class EsService:
    def createIndex(self, es_obj, dto):
        index_name = dto.name
        index_schema = schemas[dto.schema]
        return es_obj.es.indices.create(index=index_name, body=index_schema)


    def deleteIndex(self, es_obj):
        response = es_obj.es.indices.delete(index=es_obj.name)
        if 'acknowledged' in response and response['acknowledged']:
            print(f"Index {index_name} was successfully deleted.")
            return response
        else:
            print(f"Failed to delete index {index_name}.")
            return response


    def getAllIndices(self, es_obj):  
        return es_obj.es.cat.indices(format="json")


    def getIndex(self, es_obj):
        return es_obj.es.cat.indices(index=es_obj.name, format="json")


    def getIndexMappingInfo(self, es_obj):
        return es_obj.es.indices.get_mapping(index=es_obj.name)


    def indexMovie(self, es_obj, data):
        if not self.duplicationCheck(es_obj, data['imdb_id']):
            index = DbIndexService.get_by_name(es_obj.name)
            data_mapped = mapping_to_schema[index.schema](data)
            es_obj.es.index(index=es_obj.name, body=data_mapped, refresh=True)

            if self.duplicationCheck(es_obj, data['imdb_id']):
                print(f'movie "{data["title"]}" indexed')
                return 201, {'Etag': f'{data["title"]}: indexing successful.'}
            else:
                return 409, {'Etag': f'{data["title"]}: indexing failed.'}
        else:
            return 411, {'Etag': f'{data["title"]}: already indexed.'}


    def indexFolder(self, es_obj, dto):
        path = f'{os.getcwd()}/../{dto.path}'
        indexing = {
            'success': {
                'count': 0,
                'titles': [],
            },
            'failed': {
                'count': 0,
                'titles': []
            }
        }
        if Path(path).exists():
            files = glob.glob(f'{path}/*.json')
            for file in files:
                with Path(file).open('r') as moviefile:
                    movie = json.load(moviefile)
                    response = self.indexMovie(es_obj, movie)
                    if response[0] == 201:
                        print(response[1]['Etag'])
                        indexing['success']['count'] += 1
                        indexing['success']['titles'] += [movie['title']]
                    else:
                        print(response[1]['Etag'])
                        indexing['failed']['count'] += 1
                        indexing['failed']['titles'] += [movie['title']]
        else:
            print(f'{path} does not exist.')
        
        print(f"{indexing['success']['count']} movies indexed, {indexing['failed']['count']} failed to index.")
        return indexing


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
        print(query)
        size = dto.size
        search_results = es_obj.es.search(index=index, body=query, size=size)
        hits = [doc for doc in search_results['hits']['hits']]
        for hit in hits:
            print(hit['_source']['title'])
        return hits


    def multiFieldSearch(self, es_obj, dto):
        index = es_obj.name
        value = dto.value.lower()
        query = BasicSearch().standard_search_query(value)
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


    def getDocByImdbId(self, es_obj, id):
        index = es_obj.name
        field = 'imdb_id'
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
    

    def editDoc(self, es_obj, dto):
        index = es_obj.name
        doc_id = self.getDocIdByImdbId(es_obj, dto.imdb_id)
        update_data = {
            "doc": {
                "watched": dto.watched,
                "personal_notes": dto.personal_notes,
                "personal_rating": dto.personal_rating
            }
        }
        es_obj.es.update(index=index, id=doc_id, body=update_data)
    

    def deleteDocByImdbId(self, es_obj, imdb_id):
        index_name = es_obj.name
        field_name = 'imdb_id'
        value_to_delete = imdb_id
        query = {
            "query": {
                "term": {
                    field_name: imdb_id
                }
            }
        }
        response = es_obj.es.delete_by_query(index=index_name, body=query)
        print(response)
        return response
    

    def deleteDocByDocId(self, es_obj, doc_id):
        response = es_obj.es.delete(index=es_obj.name, id=doc_id)
        return response


    def getDocIdByImdbId(self, es_obj, imdb_id):
        index = es_obj.name
        field = 'imdb_id'
        value = imdb_id.lower()
        query = BasicSearch().exact_search_query(field, value)
        response = es_obj.es.search(index=index, body=query)
        
        if response["hits"]["total"]["value"] == 1:
            return response["hits"]["hits"][0]["_id"]
        else:
            print("Multiple matching documents found.")
            return None
    

    def duplicationCheck(self, es_obj, imdb_id):
        query = {
            "query": {
                "term": {
                    "imdb_id": imdb_id
                }
            }
        }
        result = es_obj.es.search(index=es_obj.name, body=query)
        if result['hits']['total']['value'] == 0:
            return False
        else:
            return True
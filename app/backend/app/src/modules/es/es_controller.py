from flask import request
from flask_restful import Resource, reqparse

from src.modules.es.es_service import EsService
from src.modules.es.dtos.search_dto import BasicSearchDto
from src.modules.es.dtos.index_dto import IndexFolderDto
from src.modules.es.es import get_es

ES_INDEX_NAME = 'movietest6'

singleFieldSearch_post_args = reqparse.RequestParser()
advancedSearch_post_args = reqparse.RequestParser()
createIndex_post_args = reqparse.RequestParser()
indexFolder_post_args = reqparse.RequestParser()
editDoc_post_args = reqparse.RequestParser()


class Es(Resource):
    def __init__(self):
        self.es = get_es()
        self.name = ES_INDEX_NAME

    def test_connection(self):
        if self.es.ping():
            return True 
        else:
            return False

    def check_index_exists(self):
        if self.es.indices.exists(self.name):
            print(f'{self.name} exists')
            return True
        else:
            print(f'{self.name} does not exist')
            return False


class EsCreateIndex(Es):
    resource = '/es/index/create'

    createIndex_post_args.add_argument('name', type=str)
    createIndex_post_args.add_argument('schema', type=str)

    def post(self):
        dto = createIndex_post_args.parse_args()
        if self.test_connection:
            return EsService().createIndex(self, dto)


class EsDeleteIndex(Es):
    resource = '/es/index/delete/<string:indexName>'
    def delete(self, indexName):
        self.name = indexName
        if self.test_connection and self.check_index_exists:
            return EsService().deleteIndex(self)


class EsGetAllIndicies(Es):
    resource = '/es/all'
    def get(self):
        if self.test_connection and self.check_index_exists:
            return EsService().getAllIndices(self)


class EsGetIndex(Es):
    resource = '/es/<string:indexName>'
    def get(self, indexName):
        self.name = indexName
        if self.test_connection and self.check_index_exists:
            return EsService().getIndex(self)


class EsGetIndexMappingInfo(Es):
    resource = '/es/mapping/<string:indexName>'
    def get(self, indexName):
        self.name = indexName
        if self.test_connection and self.check_index_exists:
            return EsService().getIndexMappingInfo(self)


class EsExactSearch(Es):
    resource = '/es/search/exact/<string:indexName>'

    singleFieldSearch_post_args.add_argument('field', type=str)
    singleFieldSearch_post_args.add_argument('value', type=str)
    singleFieldSearch_post_args.add_argument('size', type=str)

    def post(self, indexName):
        self.name = indexName
        dto = singleFieldSearch_post_args.parse_args()
        if self.test_connection and self.check_index_exists:
            return EsService().exactSearch(self, dto)


class EsSingleFieldSearch(Es):
    resource = '/es/search/single/<string:indexName>'

    singleFieldSearch_post_args.add_argument('field', type=str)
    singleFieldSearch_post_args.add_argument('value', type=str)
    singleFieldSearch_post_args.add_argument('size', type=str)

    def post(self, indexName):
        self.name = indexName
        dto = singleFieldSearch_post_args.parse_args()
        if self.test_connection and self.check_index_exists:
            return EsService().singleFieldSearch(self, dto)


class EsMultiFieldSearch(Es):
    resource = '/es/search/multi-field/<string:indexName>'

    singleFieldSearch_post_args.add_argument('field', type=str)
    singleFieldSearch_post_args.add_argument('value', type=str)
    singleFieldSearch_post_args.add_argument('size', type=str)

    def post(self, indexName):
        self.name = indexName
        dto = singleFieldSearch_post_args.parse_args()
        if self.test_connection and self.check_index_exists:
            return EsService().multiFieldSearch(self, dto)


class EsGetMovieById(Es):
    resource = '/es/search/id/<string:indexName>/<string:imdbId>'
    def get(self, indexName, imdbId):
        self.name = indexName
        if self.test_connection and self.check_index_exists:
            return EsService().getDocByImdbId(self, imdbId)


class EsGetDistinctValues(Es):
    resource = '/es/search/values/<string:indexName>/<string:field>'
    def get(self, indexName, field):
        self.name = indexName
        if self.test_connection and self.check_index_exists:
            return EsService().getDistinctValues(self, field)


class EsGetEditValues(Es):
    resource = '/es/edit/id/<string:indexName>/<string:imdbId>'
    def get(self, indexName, imdbId):
        self.name = indexName
        if self.test_connection and self.check_index_exists:
            return EsService().getDocByImdbId(self, imdbId)


class EsAdvancedSearch(Es):
    resource = '/es/search/advanced/<string:indexName>'

    advancedSearch_post_args.add_argument('parameters', type=dict)
    advancedSearch_post_args.add_argument('size', type=str)

    def post(self, indexName):
        self.name = indexName
        dto = advancedSearch_post_args.parse_args()
        if self.test_connection and self.check_index_exists:
            return EsService().advancedSearch(self, dto)


class EsIndexing(Es):
    def indexing(self, index_name, data):
        self.name = index_name
        if self.test_connection and self.check_index_exists:
            return EsService().indexMovie(self, data)


class EsIndexFolder(Es):
    resource = '/es/indexing/<string:indexName>/index-folder'

    indexFolder_post_args.add_argument('path', type=str)    

    def post(self, indexName):
        self.name = indexName
        dto = indexFolder_post_args.parse_args()
        if self.test_connection and self.check_index_exists:
            return EsService().indexFolder(self, dto)


class EsEditValues(Es):
    resource = '/es/edit/<string:indexName>'

    editDoc_post_args.add_argument('imdb_id', type=str)
    editDoc_post_args.add_argument('watched', type=bool)
    editDoc_post_args.add_argument('personal_notes', type=str)
    editDoc_post_args.add_argument('personal_rating', type=int)

    def post(self, indexName):
        self.name = indexName
        dto = editDoc_post_args.parse_args()
        if self.test_connection and self.check_index_exists:
            return EsService().editDoc(self, dto)


class EsDeleteMovieByDocId(Es):
    resource = '/es/delete/<string:indexName>/doc-id/<string:docId>'
    def delete(self, indexName, docId):
        self.name = indexName
        if self.test_connection and self.check_index_exists:
            return EsService().deleteDocByDocId(self, docId)
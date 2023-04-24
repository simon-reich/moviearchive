from flask import request
from flask_restful import Resource, reqparse
from elasticsearch import Elasticsearch
from modules.es.es_service import EsService
from modules.es.dtos.search_dto import BasicSearchDto
from modules.es.dtos.index_dto import IndexFolderDto


ES_HOST = 'localhost'
ES_PORT = 9200
ES_INDEX_NAME = 'movietest'

singleFieldSearch_post_args = reqparse.RequestParser()
advancedSearch_post_args = reqparse.RequestParser()
indexFolder_post_args = reqparse.RequestParser()

class Es(Resource):
    def __init__(self):
            self.es = Elasticsearch([{
                'host': ES_HOST,
                'port': ES_PORT
            }])
            self.name = ES_INDEX_NAME

    def test_connection(self):
        if self.es.ping():
            return True 
        else:
            return False

    def check_index_exists(self):
        if self.es.indices.exists(self.name):
            print('exists')
            return True
        else:
            print('does not exist')
            return False


class EsCreateIndex(Es):
    resource = '/es/create'
    def get(self):
        if self.test_connection:
            if not self.check_index_exists:
                print('create index')
                return EsService().createIndex(self)


class EsGetAllIndicies(Es):
    resource = '/es/all'
    def get(self):
        if self.test_connection and self.check_index_exists:
            return EsService().getAllIndices(self)


class EsGetIndexInfo(Es):
    resource = '/es'
    def get(self):
        if self.test_connection and self.check_index_exists:
            return EsService().getIndexInfo(self)


class EsExactSearch(Es):
    resource = '/es/search/exact'

    singleFieldSearch_post_args.add_argument('field', type=str)
    singleFieldSearch_post_args.add_argument('value', type=str)
    singleFieldSearch_post_args.add_argument('size', type=str)

    def post(self):
        dto = singleFieldSearch_post_args.parse_args()
        print(dto)
        if self.test_connection and self.check_index_exists:
            return EsService().exactSearch(self, dto)


class EsSingleFieldSearch(Es):
    resource = '/es/search/single'

    singleFieldSearch_post_args.add_argument('field', type=str)
    singleFieldSearch_post_args.add_argument('value', type=str)
    singleFieldSearch_post_args.add_argument('size', type=str)

    def post(self):
        dto = singleFieldSearch_post_args.parse_args()
        print(dto)
        if self.test_connection and self.check_index_exists:
            return EsService().singleFieldSearch(self, dto)


class EsMultiFieldSearch(Es):
    resource = '/es/search/multi'

    singleFieldSearch_post_args.add_argument('field', type=str)
    singleFieldSearch_post_args.add_argument('value', type=str)
    singleFieldSearch_post_args.add_argument('size', type=str)

    def post(self):
        dto = singleFieldSearch_post_args.parse_args()
        print(dto)
        if self.test_connection and self.check_index_exists:
            return EsService().multiFieldSearch(self, dto)


class EsGetMovieById(Es):
    resource = '/es/search/id/<string:imdbId>'
    def get(self, imdbId):
        if self.test_connection and self.check_index_exists:
            return EsService().getDataById(self, imdbId)


class EsGetDistinctValues(Es):
    resource = '/es/search/values/<string:field>'
    def get(self, field):
        if self.test_connection and self.check_index_exists:
            return EsService().getDistinctValues(self, field)


class EsAdvancedSearch(Es):
    resource = '/es/search/advanced'

    advancedSearch_post_args.add_argument('parameters', type=dict)
    advancedSearch_post_args.add_argument('size', type=str)

    def post(self):
        dto = advancedSearch_post_args.parse_args()
        print(dto)
        if self.test_connection and self.check_index_exists:
            return EsService().advancedSearch(self, dto)


class EsIndexing(Es):
    def indexing(self, id, data):
        if self.test_connection and self.check_index_exists:
            return EsService().indexData(self, id, data)


class EsIndexFolder(Es):
    resource = '/es/index-folder'

    def get(self):
        print('response')
        if self.test_connection and self.check_index_exists:
            print('action')
            return EsService().indexFolder(self)
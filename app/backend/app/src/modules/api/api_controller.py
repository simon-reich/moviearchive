from flask_restful import Resource, reqparse
from src.modules.api.api_service import ApiService

apiSearch_args = reqparse.RequestParser()
indexMovie_args = reqparse.RequestParser()

class Api(Resource):
    pass

class ApiSearch(Api):
    resource = '/api/search'
    
    apiSearch_args.add_argument("title", type=str, help="title is required", required=True)
    apiSearch_args.add_argument("year", type=int)
    
    def post(self):
        query = apiSearch_args.parse_args()
        searchresults = ApiService.search(query)
        return searchresults


class ApiIndexMovie(Api):
    resource = '/api/index'

    indexMovie_args.add_argument("index_name", type=str)
    indexMovie_args.add_argument("tmdb_id", type=str)

    def post(self):
        dto = indexMovie_args.parse_args()
        return ApiService.index_movie(dto)
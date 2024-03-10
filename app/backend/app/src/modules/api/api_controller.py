from flask_restful import Resource, reqparse
from src.modules.api.api_service import ApiService

apiSearch_args = reqparse.RequestParser()
indexMovie_args = reqparse.RequestParser()
indexByFile_post_args = reqparse.RequestParser()

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
    indexMovie_args.add_argument("wikipedia", type=bool)

    def post(self):
        dto = indexMovie_args.parse_args()
        return ApiService.index_movie(dto)


class ApiIndexByFile(Api):
    resource = '/api/index-by-file'

    indexByFile_post_args.add_argument("index_name", type=str)
    indexByFile_post_args.add_argument('path', type=str)    
    indexByFile_post_args.add_argument("wikipedia", type=bool)  

    def post(self):
        dto = indexByFile_post_args.parse_args()
        return ApiService.index_by_file(dto)
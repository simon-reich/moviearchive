from flask_restful import Resource, reqparse
from modules.imdbApi.imdbapi_service import ImdbApiService

imdbApiSearch_args = reqparse.RequestParser()

class ImdbApi(Resource):
    pass

class ImdbApiSearch(ImdbApi):
    resource = '/imdbapi/search'
    
    imdbApiSearch_args.add_argument("title", type=str, help="title is required", required=True)
    imdbApiSearch_args.add_argument("year", type=int)
    
    def post(self):
        query = imdbApiSearch_args.parse_args()
        searchresults = ImdbApiService.search(query)
        return searchresults


class ImdbApiArchiveMovie(ImdbApi):
    resource = '/imdbapi/<string:imdbId>'

    def get(self, imdbId):
        movieData = ImdbApiService.archive_movie(imdbId)
        return movieData
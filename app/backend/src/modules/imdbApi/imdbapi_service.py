import requests

from modules.imdbApi.utils.file_management import create_file_path, save_movie_data, load_file
from modules.imdbApi.utils.mapping import map_movie_to_indexSchema
from modules.es.es_controller import EsIndexing

API_KEY = 'k_3rlgY00a'
FILE_PATH = '../movie_data/'

class ImdbApiService:
    def search(query):
        url = build_imdbapi_search_movie_request(query['title'])
        response = imdbapi_search_movie(url)
        return response

    def archive_movie(imdbId):
        url = build_imdbapi_get_movie_request(imdbId)
        movie_data = imdbapi_get_movie(url)
        path = FILE_PATH
        filepath = create_file_path(movie_data, path)
        save_movie_data(movie_data, filepath)
        movie = load_file(filepath)
        movie_mapped = map_movie_to_indexSchema(movie)
        return EsIndexing().indexing(movie_mapped['imdbID'], movie_mapped)
        


#-----------------
# Helper functions
#-----------------

def build_imdbapi_search_movie_request(title):
    url = '/'.join(['https://imdb-api.com/en/API/SearchMovie', API_KEY, title])
    print('looking for ' + title + '...')
    return url

def imdbapi_search_movie(url):
        response = requests.request('GET', url)
        if response.status_code == 200:
            response = response.json()
            if response['results'] != 0:
                return response
            else:
                print('ERROR: movie not found!')
                if len(response['errorMessage']) > 1:
                    print(response['errorMessage'])
        else:
            print(response.status_code())


def build_imdbapi_get_movie_request(imdb_id):
    options = ",".join(['FullActor', 'FullCast', 'Posters', 'Images', 'Trailer', 'Ratings', 'Wikipedia'])
    url = "/".join(['https://imdb-api.com/en/API/Title', API_KEY, imdb_id, options])
    return url

def imdbapi_get_movie(url):
    try:
        response = requests.request('GET', url)
        if response.status_code == 200:
            response = response.json()
            return response
        else:
            print(response.status_code())
    except:
        print('error')
import requests

from src.modules.api.utils.file_management import create_file_path, save_movie_data, load_file
from src.modules.es.utils.mapping import map_movie_to_index_schema, map_movie_to_index_schema_2
from src.modules.es.es_controller import EsIndexing

FILE_PATH = '../movie_data/'

TMDB_API_KEY = 'bbc0475142b24145391bfe1be6b14418'
TMDB_API_URL = 'https://api.themoviedb.org/3'

OMDB_API_KEY = 'fe2f032f'
OMDB_API_URL = 'http://www.omdbapi.com'


class ApiService:
    def search(query):
        url = build_tmdb_search_movie_request(query['title'])
        print(f'looking for {query["title"]}...')
        response = tmdb_search_movie(url)
        return response

    def index_movie(dto):
        index_name = dto.index_name
        tmdb_id = dto.tmdb_id

        url_tmdb = build_tmdb_get_movie_request(tmdb_id)
        tmdb_movie_data = tmdb_get_movie(url_tmdb)
        
        imdb_id = tmdb_movie_data['imdb_id']

        url_omdb = build_omdb_get_movie_request(imdb_id)
        omdb_movie_data = omdb_get_movie(url_omdb)
        
        movie_data = enrich_with_omdb_data(tmdb_movie_data, omdb_movie_data)

        filepath = create_file_path(movie_data['title'], movie_data['year'], imdb_id, FILE_PATH)
        save_movie_data(movie_data, filepath)
  
        movie = load_file(filepath)

        print(index_name)

        return EsIndexing().indexing(index_name, movie)
        

#-----------------
# Helper functions
#-----------------

### TMDB Search & Fetching Movie Data

def build_tmdb_search_movie_request(title):
    query = title.replace(' ', '+')
    return f'{TMDB_API_URL}/search/movie?query={query}&api_key={TMDB_API_KEY}'


def tmdb_search_movie(url):
    try:
        response = requests.request('GET', url)
        if response.status_code == 200:
            response = response.json()
            if response['results'] != 0:
                return response
            else:
                print('no movie found...')
        else:
            print(response.status_code())
    except:
        print('error: api call failed.')


def build_tmdb_get_movie_request(tmdb_id):
    options = ','.join(['credits', 'videos', 'images', 'keywords'])
    return f'{TMDB_API_URL}/movie/{tmdb_id}?api_key={TMDB_API_KEY}&append_to_response={options}'


def tmdb_get_movie(url):
    try:
        response = requests.request('GET', url)
        if response.status_code == 200:
            response = response.json()
            return response
        else:
            print(response.status_code())
    except:
        print('error: api call failed.')


### OMDB Search & Fetching Movie Data

def build_omdb_get_movie_request(imdb_id):
    return f'{OMDB_API_URL}/?apikey={OMDB_API_KEY}&i={imdb_id}&plot=full'


def omdb_get_movie(url):
    try:
        response = requests.request('GET', url)
        if response.status_code == 200:
            response = response.json()
            return response
        else:
            print(response.status_code())
    except:
        print('error: api call failed.')


### Add OMDB Data --> TMDB Data

def enrich_with_omdb_data(tmdb_data, omdb_data):
    movie_data = dict(tmdb_data)
    movie_data['title_english'] = omdb_data['Title'] if omdb_data else None 
    movie_data['year'] = omdb_data['Year'] if omdb_data else None
    movie_data['rated'] = omdb_data['Rated'] if omdb_data else None
    movie_data['director_list'] = omdb_data['Director'].split(',') if omdb_data else None
    movie_data['writer_list'] = omdb_data['Writer'].split(',') if omdb_data else None
    movie_data['main_cast'] = omdb_data['Actors'].split(',') if omdb_data else None
    movie_data['ratings'] = omdb_data['Ratings'] if omdb_data else None
    movie_data['imdb_rating'] = omdb_data['imdbRating'] if omdb_data else None
    movie_data['imdb_votes'] = omdb_data['imdbVotes'] if omdb_data else None
    return movie_data





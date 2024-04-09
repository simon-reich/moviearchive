import requests
import wikipediaapi
from src.modules.api.utils.file_management import create_file_path, save_movie_data, load_file
from src.modules.es.utils.mapping import map_movie_to_schema_tmdb, map_movie_to_schema_tmdb_2
from src.modules.es.es_controller import EsIndexing, EsDuplicationCheck

from dotenv import dotenv_values
import os

api_vars = dotenv_values('../.env.api')

FILE_PATH = '../movie_data/'

TMDB_API_KEY = api_vars['TMDB_API_KEY']
TMDB_API_URL = api_vars['TMDB_API_URL']

OMDB_API_KEY = api_vars['OMDB_API_KEY']
OMDB_API_URL = api_vars['OMDB_API_URL']

class ApiService:
    def search(query):
        url = build_tmdb_search_movie_request(query['title'])
        print(f'looking for {query["title"]}...')
        response = tmdb_search_movie(url)
        return response


    def index_movie(dto):
        index_name = dto.index_name
        tmdb_id = dto.tmdb_id

        if not EsDuplicationCheck().duplication_check(index_name, tmdb_id):
            url_tmdb = build_tmdb_get_movie_request(tmdb_id)
            tmdb_movie_data = tmdb_get_movie(url_tmdb)
            
            imdb_id = tmdb_movie_data['imdb_id']

            url_omdb = build_omdb_get_movie_request(imdb_id)
            omdb_movie_data = omdb_get_movie(url_omdb)
            movie_data = enrich_with_omdb_data(tmdb_movie_data, omdb_movie_data)

            if dto.wikipedia and dto.wikipedia == True:
                wiki_data = get_wikipedia_data(movie_data['title'], movie_data['original_title'], str(movie_data['year']))
                movie_data = enrich_with_wiki_data(movie_data, wiki_data)

            filepath = create_file_path(movie_data['title'], movie_data['year'], imdb_id, FILE_PATH)
            save_movie_data(movie_data, filepath)
    
            movie = load_file(filepath)

            return EsIndexing().indexing(index_name, movie)
        
        return False


    def index_by_file(dto):
        print('endpoint reachable')
        

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


### Fetching Wikipedia Data

def get_wikipedia_data(title: str, original_title: str, year: str):
    wiki_data = {
        'url': None,
        'plot': None,
        'plot_html': None,
        'summary': None,
        'critics': None,
        'full_html': None
    }

    page_id = title.replace(" ", "_")
    page_id_og = original_title.replace(" ", "_")
    page_id_alt = f'{page_id}_(film)'
    page_id_alt_year = f'{page_id}_({year}_film)'
    page_id_alt_og = f'{page_id_og}_(film)'
    page_id_alt_year_og = f'{page_id_og}_({year}_film)'

    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='MovieArchive (simonreich@posteo.de)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    wiki_html = wikipediaapi.Wikipedia(
        user_agent='MovieArchive (simonreich@posteo.de)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.HTML
    )
    page = wiki_wiki.page(page_id_alt_year_og)
    page_html = wiki_html.page(page_id_alt_year_og)

    if not page.exists():
        print(f'{page}: {page.exists()}')
        page = wiki_wiki.page(page_id_alt_og)
        page_html = wiki_html.page(page_id_alt_og)

        if not page.exists():
            print(f'{page}: {page.exists()}')
            page = wiki_wiki.page(page_id_og)
            page_html = wiki_html.page(page_id_og)

            if not page.exists():
                print(f'{page}: {page.exists()}')
                page = wiki_wiki.page(page_id_alt_year)
                page_html = wiki_html.page(page_id_alt_year)

                if not page.exists():
                    print(f'{page}: {page.exists()}')
                    page = wiki_wiki.page(page_id_alt)
                    page_html = wiki_html.page(page_id_alt)

                    if not page.exists():
                        print(f'{page}: {page.exists()}')
                        page = wiki_wiki.page(page_id)
                        page_html = wiki_html.page(page_id)

    if page.exists():
        wiki_data['url'] = page.fullurl
        wiki_data['summary'] = page.summary
        wiki_data['plot'] = page.section_by_title('Plot').text if page.section_by_title('Plot') else None
        wiki_data['plot_html'] = page_html.section_by_title('Plot').text if page.section_by_title('Plot') else None
        wiki_data['critics'] = page.section_by_title('Critical response').text if page.section_by_title('Critical response') else None
        wiki_data['full_html'] = page_html.text

    return wiki_data


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


### Add Wikipedia Data --> TMDB Data

def enrich_with_wiki_data(tmdb_data, wiki_data):
    movie_data = dict(tmdb_data)
    movie_data['wikipedia_url'] = wiki_data['url']
    movie_data['wikipedia_summary'] = wiki_data['summary']
    movie_data['wikipedia_plot'] = wiki_data['plot']
    movie_data['wikipedia_plot_html'] = wiki_data['plot_html']
    movie_data['wikipedia_critics'] = wiki_data['critics']
    movie_data['wikipedia_full_html'] =  wiki_data['full_html']
    return movie_data



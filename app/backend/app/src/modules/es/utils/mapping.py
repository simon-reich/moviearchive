import json


def map_movie_to_index_schema(movie):
    movie_mapped = {
        'tmdb_id': movie['id'],
        'imdb_id': movie['imdb_id'],
        'title': movie['title'],
        'original_title': movie['original_title'],
        'year': movie['year'],
        'poster': movie['poster_path'],
        'release_date': movie['release_date'] if len(movie['release_date']) > 1 else '1999-12-31',
        'runtime': movie['runtime'] if isinstance(movie['runtime'], int) else None,
        'synopsis': movie['overview'],
        'director_list': movie['director_list'],
        'writer_list': movie['writer_list'],
        'main_cast': movie['main_cast'],
        'full_cast': movie['credits']['cast'],
        'full_crew': movie['credits']['crew'],
        'genre_list': [item['name'] for item in movie['genres']],
        'country_list': movie['production_countries'],
        'language_list': movie['spoken_languages'],
        'company_list': movie['production_companies'],
        'keyword_list': [item['name'] for item in movie['keywords']['keywords']],
        'boxoffice': movie['revenue'],
        'content_rating': movie['rated'],
        'imdb_link': f'https://www.imdb.com/title/{movie["imdb_id"]}',
        'imdb_rating': float(movie['imdb_rating']) if movie['imdb_rating'] else None,
        'imdb_votes': int(movie['imdb_votes'].replace(',', '')) if movie['imdb_votes'] else None,
        'rating_list': movie['ratings'],
        'poster_list': movie['images']['posters'],
        'backdrop_list': movie['images']['backdrops'],
        'video_list': movie['videos']['results'],
        'trailer': max((v for v in movie['videos']['results'] if v["type"] == "Trailer"), key=lambda x: x["published_at"]) if any('Trailer' in v['type'] for v in movie['videos']['results']) else None,
        'watched': None,
        'personal_rating': None,
        'personal_notes': None,
    }
    return movie_mapped


def map_movie_to_index_schema_2(movie):
    movie_mapped = {
        'tmdb_id': movie['id'],
        'imdb_id': movie['imdb_id'],
        'title': movie['title'],
        'original_title': movie['original_title'],
        'year': movie['year'],
        'poster': movie['poster_path'],
        'release_date': movie['release_date'] if len(movie['release_date']) > 1 else '1999-12-31',
        'runtime': movie['runtime'] if isinstance(movie['runtime'], int) else None,
        'synopsis': movie['overview'],
        'director_list': movie['director_list'],
        'director_list_fulltext': movie['director_list'],
        'writer_list': movie['writer_list'],
        'writer_list_fulltext': movie['writer_list'],
        'main_cast': movie['main_cast'],
        'main_cast_fulltext': movie['main_cast'],
        'full_cast': movie['credits']['cast'],
        'full_crew': movie['credits']['crew'],
        'genre_list': [item['name'] for item in movie['genres']],
        'country_list': movie['production_countries'],
        'language_list': movie['spoken_languages'],
        'company_list': movie['production_companies'],
        'keyword_list': [item['name'] for item in movie['keywords']['keywords']],
        'boxoffice': movie['revenue'],
        'content_rating': movie['rated'],
        'imdb_link': f'https://www.imdb.com/title/{movie["imdb_id"]}',
        'imdb_rating': float(movie['imdb_rating']) if movie['imdb_rating'] else None,
        'imdb_votes': int(movie['imdb_votes'].replace(',', '')) if movie['imdb_votes'] else None,
        'rating_list': movie['ratings'],
        'poster_list': movie['images']['posters'],
        'backdrop_list': movie['images']['backdrops'],
        'video_list': movie['videos']['results'],
        'trailer': max((v for v in movie['videos']['results'] if v["type"] == "Trailer"), key=lambda x: x["published_at"]) if any('Trailer' in v['type'] for v in movie['videos']['results']) else None,
        'watched': None,
        'personal_rating': None,
        'personal_notes': None,
    }
    return movie_mapped


def get_keys_of_given_schema(schema):
    schema_dict = json.loads(schema)
    return schema_dict['mappings']['properties'].keys()
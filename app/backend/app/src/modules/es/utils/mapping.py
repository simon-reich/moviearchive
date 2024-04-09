import json


def map_movie_to_schema_tmdb(movie):
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


def map_movie_to_schema_tmdb_2(movie):
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

def map_movie_to_schema_tmdb_wiki(movie):
    movie_mapped = {
        'tmdb_id': movie['id'] if 'id' in movie else None,
        'imdb_id': movie['imdb_id'],
        'title': movie['title'],
        'original_title': movie['original_title'] if 'original_title' in movie else None,
        'year': movie['year'] if 'year' in movie else None,
        'poster': movie['poster_path'] if 'poster_path' in movie else None,
        'release_date': movie['release_date'] if "release_date" in movie and len(movie['release_date']) > 1 else '1999-12-31',
        'runtime': movie['runtime'] if 'runtime' in movie and isinstance(movie['runtime'], int) else None,
        'synopsis': movie['overview'] if 'overview' in movie else None,
        'director_list': movie['director_list'] if 'director_list' in movie else None,
        'writer_list': movie['writer_list'] if 'writer_list' in movie else None,
        'main_cast': movie['main_cast'] if 'main_cast' in movie else None,
        'full_cast': movie['credits']['cast'] if 'credits' in movie else None,
        'full_cast_names': [item['name'] for item in movie['credits']['cast']] if 'credits' in movie else None,
        'full_crew': movie['credits']['crew'] if 'credits' in movie else None,
        'full_crew_names': [item['name'] for item in movie['credits']['crew']] if 'credits' in movie else None,
        'genre_list': [item['name'] for item in movie['genres']] if 'genres' in movie else None,
        'country_list': movie['production_countries'] if 'production_countries' in movie else None,
        'country_list_names': [item['name'] for item in movie['production_countries']] if 'production_countries' in movie else None,
        'language_list': movie['spoken_languages'] if 'spoken_languages' in movie else None,
        'language_list_names': [item['name'] for item in movie['spoken_languages']] if 'spoken_languages' in movie else None,
        'company_list': movie['production_companies'] if 'production_companies' in movie else None,
        'company_list_names': [item['name'] for item in movie['production_companies']] if 'production_companies' in movie else None,
        'keyword_list': [item['name'] for item in movie['keywords']['keywords']] if 'keywords' in movie else None,
        'boxoffice': movie['revenue'] if 'revenue' in movie else None,
        'content_rating': movie['rated'] if 'rated' in movie else None,
        'imdb_link': f'https://www.imdb.com/title/{movie["imdb_id"]}',
        # 'imdb_votes': int(movie['imdb_votes'].replace(',', '')) if movie['imdb_votes'] else None,
        'rating_list': movie['ratings'] if 'ratings' in movie else None,
        'poster_list': movie['images']['posters'] if 'images' in movie else None,
        'backdrop_list': movie['images']['backdrops'] if 'images' in movie else None,
        'video_list': movie['videos']['results'] if 'videos' in movie else None,
        'trailer': max((v for v in movie['videos']['results'] if v["type"] == "Trailer"), key=lambda x: x["published_at"]) if any('Trailer' in v['type'] for v in movie['videos']['results']) else None,
        'watched': None,
        'personal_rating': None,
        'personal_notes': None,
        'wikipedia_url': movie['wikipedia_url'] if 'wikipedia_url' in movie else None,
        'wikipedia_plot': movie['wikipedia_plot'] if 'wikipedia_plot' in movie else None,
        'wikipedia_plot_html': movie['wikipedia_plot_html'] if 'wikipedia_plot_html' in movie else None,
        'wikipedia_summary': movie['wikipedia_summary'] if 'wikipedia_summary' in movie else None,
        'wikipedia_critics': movie['wikipedia_critics'] if 'wikipedia_critics' in movie else None,
        'wikipedia_full_html': movie['wikipedia_full_html'] if 'wikipedia_full_html' in movie else None,
    }
    
    try:
        movie_mapped['imdb_rating'] = float(movie['imdb_rating'])
    except:
        print(f'converting imdb_rating to float impossible: {movie["imdb_rating"]}')
    finally:
        movie_mapped['imdb_rating'] = None
    
    try:
        movie_mapped['imdb_votes'] = int(movie['imdb_votes'].replace(',', '')) if movie['imdb_votes'] else None,
    except:
        print(f'converting imdb_votes to int impossible: {movie["imdb_rating"]}')
    finally:
        movie_mapped['imdb_votes'] = None
    
    return movie_mapped


def get_schema_fields_as_text_map():
    return {
        "tmdb_id": "TMDb ID",
        "imdb_id": "IMDb ID",
        "title": "Title",
        "original_title": "Title (original)",
        "year": "Year",
        "release_date": "Release Date",
        "runtime": "Runtime",
        "poster": "Poster",
        "synopsis": "Plot",
        "director_list": "Directors",
        "writer_list": "Writers",
        "main_cast": "Main Cast",
        "full_cast": "Cast",
        "full_cast_names": "Cast",
        "full_crew": "Crew",
        "full_crew_names": "Crew",
        "genre_list": "Genres",
        "country_list": "Countries",
        "country_list_names": "Countries",
        "language_list": "Languages",
        "language_list_names": "Languages",
        "Company_list": "Companies",
        "Company_list_names": "Companies",
        "keyword_list": "Keywords",
        "content_rating": "Content Rating",
        "box_office": "Box Office",
        "imdb_link": "IMDb Link",
        "imdb_rating": "IMDb Rating",
        "imdb votes": "IMDb Votes",
        "rating_list": "Ratings",
        "poster_list": "Posters",
        "backdrop_list": "Backdrops",
        "video_list": "Videos",
        "trailer": "Trailer",
        "watched": "Watched",
        "personal_rating": "Personal Rating",
        "personal_notes": "Personal Notes",
        "wikiperdia_url": "Wikipedia URL",
        "wikipedia_plot": "Plot (Wikipedia)",
        "wikipedia_plot_html": "Plot (Wikipedia)",
        "wikipedia_summary": "Summary (Wikipedia)",
        "wikipedia_critics": "Reception (Wikipedia)",
        "wikipedia_full_html": "Wikipedia"
    }
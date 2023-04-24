def map_imdbApiSchema_to_indexSchema(movie):
    movie_mapped = {
        'title': movie['title'],
        'year': movie['year'],
        'imdbID': movie['id'],
        'originalTitle': movie['originalTitle'],
        'medium': movie['type'],
        'imageLink': movie['image'],
        'releaseDate': movie['releaseDate'],
        'runtime': movie['runtimeMins'] if isinstance(movie['runtimeMins'], int) else None,
        'plot': movie['plot'],
        'directorList': movie['directorList'],
        'writerList': movie['writerList'],
        'starList': movie['starList'],
        'actorList': movie['actorList'],
        'fullCast': movie['fullCast'],
        'genreList': [item['key'] for item in movie['genreList']],
        'countryList': [item['key'] for item in movie['countryList']],
        'languageList': [item['key'] for item in movie['languageList']],
        'contentRating': movie['contentRating'],
        'keywordList': movie['keywordList'],
        'companyList': movie['companyList'],
        'boxOffice': movie['boxOffice'],
        'imdbLink': '/'.join(['https://www.imdb.com/title', movie['id']]),
        'imdbRating': movie['imDbRating'],
        'imdbVotes': movie['imDbRatingVotes'],
        'ratingList': movie['ratings'],
        'wikiLink': movie['wikipedia']['url'],
        'wikiTextShort': movie['wikipedia']['plotShort']['plainText'] if movie['wikipedia']['plotShort'] else None,
        'wikiTextShortHtml': movie['wikipedia']['plotShort']['html'] if movie['wikipedia']['plotShort'] else None,
        'wikiTextFull': movie['wikipedia']['plotFull']['plainText'] if movie['wikipedia']['plotFull'] else None,
        'wikiTextFullHtml': movie['wikipedia']['plotFull']['html'] if movie['wikipedia']['plotFull'] else None,
        'posterList': movie['posters']['posters'],
        'imageList': movie['images']['items'],
        'trailer': movie['trailer'],
        'tvSeriesInfo': movie['tvSeriesInfo'],
        'tvEpisodeInfo': movie['tvEpisodeInfo'],
        'personalRating': None,
        'personalNotes': None
    }
    if len(movie_mapped['releaseDate']) < 2:
        movie_mapped['releaseDate'] = "1999-12-31"
    return movie_mapped

def map_movie_to_indexSchema(movie):
    movie_mapped = map_imdbApiSchema_to_indexSchema(movie)
    return movie_mapped
    
def map_movies_to_indexSchema(movies):
    movies_mapped = [map_imdbApiSchema_to_indexSchema(movie) for movie in movies]
    return movies_mapped
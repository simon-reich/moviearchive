def get_movie_index_schema():
    return {
        'settings' : {
            'number_of_shards' : 1,
            'analysis' : {
                'analyzer' : {
                    'custom_analyzer' : {
                        'type' : 'custom',
                        'tokenizer' : 'standard',
                        'filter' : [ 
                            'asciifolding',
                            'classic',
                            'elision',
                            'lowercase',
                            'stop',
                            'kstem',
                        ]   
                    }
                },
            }
        },
        # creating the schema in form of mappings
        'mappings' : {
            'dynamic' : 'strict',
            'properties': {
                'imdbID' : {
                   'type' : 'keyword', 
                   'index': 'true',
                },
                'title' : { 
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer',
                    # multi-field
                    'fields' : {
                        'raw' : {
                            'type' : 'keyword',
                            'index' : 'true',
                        }
                    }
                },
                'originalTitle' : { 
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer',
                    # multi-field
                    'fields' : {
                        'raw' : {
                            'type' : 'keyword',
                            'index' : 'true',
                        }
                    }
                },
                'medium' : {
                    'type' : 'keyword', 
                    'index' : 'false',
                },
                'imageLink' : { 
                    'type' : 'keyword',
                    'index' : 'false' 
                },
                'year' : {
                    'type' : 'integer',
                    'index' : 'true'
                },
                'releaseDate' : {
                    'type' : 'date',
                    'index' : 'true'
                },
                'runtime' : {
                    'type' : 'integer',
                    'index' : 'true'
                },
                'runtimeString' : {
                    'type' : 'keyword',
                    'index' : 'false'
                },
                'plot' : {
                    'type': 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer'
                },
                'directorList' : {
                    'type': 'flattened',
                    'index' : 'true',
                },
                'writerList' : {
                    'type': 'flattened',
                    'index' : 'true',
                },
                'starList' : {
                    'type': 'flattened',
                    'index' : 'true',
                },
                'actorList' : {
                    'type': 'flattened',
                    'index' : 'true',
                },
                'fullCast' : {
                    'type' : 'flattened',
                    'index' : 'true'
                },
                'genreList' : {
                    'type' : 'keyword',
                    'index' : 'true'
                },
                'countryList' : {
                    'type' : 'keyword',
                    'index' : 'true'
                },
                'languageList' : {
                    'type' : 'keyword',
                    'index' : 'true'
                },
                'contentRating' : {
                    'type' : 'keyword',
                    'index' : 'false'
                },
                'keywordList' : {
                    'type' : 'keyword',
                    'index' : 'true'
                },
                'companyList' : {
                    'type' : 'flattened',
                    'index' : 'true'
                },
                'boxOffice' : {
                    'type' : 'flattened',
                    'index' : 'false'
                },
                'imdbLink' : {
                    'type' : 'keyword',
                    'index' : 'true'
                },
                'imdbRating' : {
                    'type' : 'float',
                    'index' : 'true'
                },
                'imdbVotes' : {
                    'type' : 'integer',
                    'index' : 'true'
                },
                'ratingList' : {
                    'type' : 'flattened',
                    'index' : 'true'
                },
                'wikiLink' : {
                    'type' : 'keyword',
                    'index' : 'false'
                },
                'wikiTextShort' : {
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer'
                },
                'wikiTextShortHtml' : {
                    'type' : 'text',
                    'index' : 'false'
                },
                'wikiTextFull' : {
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer'
                },
                'wikiTextFullHtml' : {
                    'type' : 'text',
                    'index' : 'false'
                },
                'posterList': {
                    'type' : 'flattened',
                    'index' : 'false'
                },
                'imageList' : {
                    'type' : 'flattened',
                    'index' : 'false'
                },
                'trailer' : {
                    'type' : 'flattened',
                    'index' : 'false'
                },
                'tvSeriesInfo': {
                    'type' : 'object',
                    'dynamic' : 'true',
                },
                'tvEpisodeInfo' : {
                    'type' : 'object',
                    'dynamic' : 'true',
                },
                'personalRating' : {
                    'type' : 'float',
                    'index' : 'true'
                },
                'personalNotes' : {
                    'type' : 'text',
                    'index' : 'true'
                }         
            }
        }
    }
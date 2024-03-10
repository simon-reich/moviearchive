def get_schema_tmdb_wiki():
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
                    },
                },
            }
        },
        # creating the schema in form of mappings
        'mappings' : {
            'dynamic' : 'strict',
            'properties': {
                'tmdb_id' : {
                   'type' : 'integer', 
                   'index': 'true',
                },

                'imdb_id' : {
                   'type' : 'keyword', 
                   'index': 'true',
                },
                'title' : { 
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer',
                    'fields' : {
                        'raw' : {
                            'type' : 'keyword',
                            'index' : 'true',
                        }
                    }
                },
                'original_title' : { 
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer' : 'custom_analyzer',
                    'fields' : {
                        'raw' : {
                            'type' : 'keyword',
                            'index' : 'true',
                        }
                    }
                },
                'year' : {
                    'type' : 'integer',
                    'index' : 'true'
                },
                'release_date' : {
                    'type' : 'date',
                    'index' : 'true'
                },
                'runtime' : {
                    'type' : 'integer',
                    'index' : 'true'
                },
                'poster' : { 
                    'type' : 'keyword',
                    'index' : 'false' 
                },
                'synopsis' : {
                    'type': 'text',
                    'index': 'true',
                    'analyzer': 'custom_analyzer'
                },
                'director_list' : {
                    'type': 'keyword',
                    'index' : 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'writer_list' : {
                    'type': 'keyword',
                    'index' : 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'main_cast' : {
                    'type': 'keyword',
                    'index' : 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'full_cast' : {
                    'type': 'flattened',
                    'index' : 'true',
                },
                'full_cast_names' : {
                    'type': 'keyword',
                    'index' : 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'full_crew' : {
                    'type': 'flattened',
                    'index': 'true',
                },
                'full_crew_names' : {
                    'type': 'keyword',
                    'index': 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'genre_list' : {
                    'type': 'keyword',
                    'index': 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'country_list' : {
                    'type' : 'flattened',
                    'index' : 'true',
                },
                'country_list_names' : {
                    'type' : 'keyword',
                    'index' : 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'language_list' : {
                    'type' : 'flattened',
                    'index' : 'true',
                },
                'language_list_names' : {
                    'type' : 'keyword',
                    'index' : 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'company_list' : {
                    'type' : 'flattened',
                    'index' : 'true',
                },
                'company_list_names' : {
                    'type' : 'keyword',
                    'index' : 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'keyword_list' : {
                    'type' : 'keyword',
                    'index' : 'true',
                    'fields': {
                        'text': {
                            'type': 'text',
                            'index': 'true',
                            'analyzer': 'custom_analyzer',
                        }
                    }
                },
                'content_rating' : {
                    'type' : 'keyword',
                    'index' : 'false'
                },
                'boxoffice' : {
                    'type' : 'integer',
                    'index' : 'false'
                },
                'imdb_link' : {
                    'type' : 'keyword',
                    'index' : 'true'
                },
                'imdb_rating' : {
                    'type' : 'float',
                    'index' : 'true'
                },
                'imdb_votes' : {
                    'type' : 'integer',
                    'index' : 'true'
                },
                'rating_list' : {
                    'type' : 'flattened',
                    'index' : 'true'
                },
                'poster_list': {
                    'type' : 'flattened',
                    'index' : 'false'
                },
                'backdrop_list' : {
                    'type' : 'flattened',
                    'index' : 'false'
                },
                'video_list' : {
                    'type' : 'flattened',
                    'index' : 'false'
                },
                'trailer' : {
                    'type' : 'flattened',
                    'index' : 'false'
                },
                'watched' : {
                    'type' : 'boolean',
                    'index' : 'false'
                },
                'personal_rating' : {
                    'type' : 'float',
                    'index' : 'true'
                },
                'personal_notes' : {
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer': 'custom_analyzer'
                },
                'wikipedia_url': {
                    'type' : 'keyword',
                    'index' : 'false'
                },
                'wikipedia_plot': {
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer': 'custom_analyzer'
                },
                'wikipedia_plot_html': {
                    'type' : 'text',
                    'index' : 'false'
                },
                'wikipedia_summary': {
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer': 'custom_analyzer'
                },
                'wikipedia_critics': {
                    'type' : 'text',
                    'index' : 'true',
                    'analyzer': 'custom_analyzer'
                },
                'wikipedia_full_html': {
                    'type' : 'text',
                    'index' : 'false'
                },
            }
        }
    }
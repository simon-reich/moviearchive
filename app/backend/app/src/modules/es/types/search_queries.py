from src.modules.es.utils.nlp_functions import year_to_century, check_if_string_is_runtime, check_if_string_is_releaseYear

GENRES = ['horror', 'drama', 'romance', 'thriller', 'crime', 'comedy', 'documentary', 'action']

class Search(object):
    def __init__(self):
        super().__init__()

    ### blocks to build customized multi field bool queries

    def boolQuery(self, boolBlock):
        return {
            "query": {
                "bool": boolBlock
            }
        }

    def termBlock(self, field, value):
        return {
            "term": {
                field : value
            }
        }
    
    def boolFilterBlock(self, field, termBlocks):
        return {
            "filter": termBlocks
        }

    def boolMustBlock(self, field, termBlocks):
        return {
            "must": termBlocks
        }

    def boolShouldBlock(self, field, termBlocks):
        return {
            "should": termBlocks
        }


    ### exact term query
    def termQuery(self, field, value, sort="title.raw", size=10000):
        return {
            "query": {
                "term": {
                    field : value
                }
            },
            "sort": [{
                sort: {
                    "order": "asc"
                }
            }],
            "size": size,
        }


    ### fuzzy query
    def matchQuery(self, field, value, analyzer="custom_analyzer", size=1000):
        return {
            "query": {
                "match": {
                    field : value,
                    "analyzer": analyzer,
                }
            },
            "size": size,
        }

    
    def phraseQuery(self, field, value, analyzer="custom_analyzer", size=1000):
        return {
            "query": {
                "match_phrase": {
                    field: value,
                    "analyzer": analyzer,
                }
            },
            "size": size,
        }


    def multiMatchQuery(self, value, fields, analyzer="custom_analyzer", size=1000):
        body = {
            'query': {
                'multi_match': {
                    'query': value,
                    'fields': fields,
                    'type': 'most_fields',
                    "analyzer": analyzer,
                }
            },
            'highlight': {
                'fields': {}
            },
            'size': size,
        }

        for field in fields:
            field = field.split('^')[0]
            body['highlight']['fields'][field] = {} 
        return body


    def nearestNumberQuery(self, field, value, size=100):
        return {
            "aggs": {
                "field-values": {           
                    "terms": {
                        "field": field,
                    }
                }
            },
            "sort": {
                "_script": {
                    "type": "number",
                    "script": {
                        "lang": "painless",
                        "source": "Math.abs(doc[params.field].value - params.target_number)",
                        "params": {
                            "target_number": value,
                            "field": field
                        }
                    },
                    "order": "asc"
                }
            },
            "size": size
        }
    

    def distinctValuesQuery(self, field, size=1000):
        return { 
            "aggs": {
                "field-values": {           
                    "terms": {
                        "field": field,
                    }
                }
            },
            "size": size
        }
    

    def getAllQuery(self, sort="title.raw", size=10000):
        return {
            "query": {
                "match_all": {}
            },
            "sort": [{
                sort: {
                    "order": "asc"
                }
            }],
            "size": size,
        }


class BasicSearch(Search):
    def __init__(self):
        super().__init__()

    def exact_search_query(self, field, term, sort='title.raw', size=10000):
        return self.termQuery(field, term, sort, size)

    def single_field_query(self, field, term, size=1000):
        return self.matchQuery(field, term, size)

    def standard_search_query(self, term, size=1000):
        print(f'query: {term}')
        term_type = self.categorize_query(term)
        if term_type == 'text':
            fields = [
                'title^2', 
                'original_title^2', 
                'synopsis^4',
                'wikipedia_plot^4',
                'director_list.text^2', 
                'writer_list.text^2',
                'main_cast.text^2',
                'full_cast_names.text^1',
                'full_crew_names.text^1',
                'keyword_list^4',
            ]
            query = self.multiMatchQuery(term, fields, analyzer="custom_analyzer", size=1000)
        elif term_type == 'runtime':
            query = self.nearestNumberQuery('runtime', int(term))
        elif term_type == 'year':
            query = self.nearestNumberQuery('year', int(term))
        elif term_type == 'century':
            term = year_to_century(term)
            fields = ['synopsis^2', 'wikipedia_plot^2', 'keyword_list^4']
            query = self.multiMatchQuery(term, fields, analyzer="custom_analyzer", size=1000)
        elif term_type == 'genre':
            query = self.exact_search_query('genre_list.text', term)
        elif term_type == 'all':
            query = self.getAllQuery()
        return query
    
    def distinct_values_from_field_query(self, field, size=1000):
        return self.distinctValuesQuery(field, size)

    def categorize_query(self, term):
        term = term.strip()
        print(term)
        if term.isnumeric():
            if check_if_string_is_runtime(term):
                return 'runtime'
            elif check_if_string_is_releaseYear(term):
                return 'year'
            else:
                return 'century'
        elif term in GENRES:
            return 'genre'
        elif term == '' or term == 'all':
            print('ALL')
            return 'all'
        else:
            return 'text'
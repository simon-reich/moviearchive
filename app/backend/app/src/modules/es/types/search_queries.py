from src.modules.es.utils.nlp_functions import year_to_century, check_if_string_is_runtime, check_if_string_is_releaseYear

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

    def termQuery(self, field, value):
        return {
            "query": {
                "term": {
                    field : value
                }
            }
        }

    ### fuzzy query

    def matchQuery(self, field, value):
        return {
            "query": {
                'match': {
                    field : value
                }
            }
        }
    


    def multiMatchQuery(self, value, fields):
        return {
            'query': {
                'multi_match': {
                        'query': value,
                        'type': 'most_fields',
                        'fields': fields
                }
            }
        }

    def nearestNumberQuery(self, field, value):
        return {
            "aggs": {
                "field-values": {           
                    "terms": {
                        "field": field
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
            }
        }
    
    def distinctValuesQuery(self, field, size=1000):
        return { 
            "aggs": {
                "field-values": {           
                    "terms": {
                        "field": field,
                        "size": size
                    }
                }
            }
        }

class BasicSearch(Search):
    def __init__(self):
        super().__init__()

    def exact_search_query(self, field, term):
        return self.termQuery(field, term)

    def single_field_query(self, field, term):
        return self.matchQuery(field, term)

    def standard_search_query(self, term):
        term_type = self.categorize_query(term)
        if term_type == 'text':
            fields = [
                'title^4', 
                'original_title^4', 
                'synopsis^2', 
                'director_list_fulltext^4', 
                'writer_list_fulltext^2',
                'main_cast_fulltext^4',
                'full_cast^2',
                'full-crew^1',
                'keyword_list^4',
                ]
            query = self.multiMatchQuery(term, fields)
        elif term_type == 'runtime':
            query = self.nearestNumberQuery('runtime', int(term))
        elif term_type == 'year':
            query = self.nearestNumberQuery('year', int(term))
        elif term_type == 'century':
            term = year_to_century(term)
            fields = ['synopsis^2', 'keyword_list^4']
            query = self.multiMatchQuery(term, fields)
        elif term_type == 'genre':
            pass
        return query
    
    def distinct_values_from_field_query(self, field, size=100):
        return self.distinctValuesQuery(field, size=100)

    def categorize_query(self, term):
        term = term.strip()
        if term.isnumeric():
            if check_if_string_is_runtime(term):
                return 'runtime'
            elif check_if_string_is_releaseYear(term):
                return 'year'
            else:
                return 'century'
        else:
            return 'text'
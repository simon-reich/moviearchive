from elasticsearch import Elasticsearch

def connect_to_es():
    es = Elasticsearch([{
        'host': 'localhost',
        'port': 9200
    }])
    if es.ping():
        print('läuft')
        return es
    else:
        print('no connection')

def check_index(es, name):
    es.indices.exists(name)
        #print(name, 'exists, alles roger')
        #return True

es = connect_to_es()
check_index(es, 'moviearchive')

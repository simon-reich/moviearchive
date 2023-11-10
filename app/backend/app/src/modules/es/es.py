from elasticsearch7 import Elasticsearch
import os

ELASTIC_HOST = os.environ.get('ES_HOST', 'localhost')
ELASTIC_URI = f'http://{ELASTIC_HOST}:9200'

def get_es():
    return Elasticsearch(ELASTIC_URI)
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from modules.imdbApi.imdbapi_module import ImdbApiModule
from modules.es.es_module import EsModule

app = Flask(__name__)
api = Api(app)
CORS(app)

imdbApiController = ImdbApiModule.controller
api.add_resource(imdbApiController['searchMovie'], imdbApiController['searchMovie'].resource)
api.add_resource(imdbApiController['archiveMovie'], imdbApiController['archiveMovie'].resource)

esController = EsModule.controller
api.add_resource(esController['createIndex'], esController['createIndex'].resource)
api.add_resource(esController['getAllIndicies'], esController['getAllIndicies'].resource)
api.add_resource(esController['exactSearch'], esController['exactSearch'].resource)
api.add_resource(esController['singleFieldSearch'], esController['singleFieldSearch'].resource)
api.add_resource(esController['multiFieldSearch'], esController['multiFieldSearch'].resource)
api.add_resource(esController['advancedSearch'], esController['advancedSearch'].resource)
api.add_resource(esController['getMovieById'], esController['getMovieById'].resource)
api.add_resource(esController['getDistinctValues'], esController['getDistinctValues'].resource)
api.add_resource(esController['indexFolder'], esController['indexFolder'].resource)


API_KEY = 'k_3rlgY00a'


if __name__ == '__main__':
    app.run(debug=True)
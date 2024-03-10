from flask import Flask, jsonify
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
import os

from src.modules.api.api_module import ApiModule
from src.modules.es.es_module import EsModule
from src.modules.db.user.db_user_module import DbUserModule
from src.modules.db.index.db_index_module import DbIndexModule
from src.modules.db.database import db
from config import Config

from datetime import timedelta


def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db)

    api = Api(app)

    db_user_controller = DbUserModule.controller
    api.add_resource(db_user_controller['db_user'], db_user_controller['db_user'].resource)
    api.add_resource(db_user_controller['db_users'], db_user_controller['db_users'].resource)

    db_index_controller = DbIndexModule.controller
    api.add_resource(db_index_controller['db_index'], db_index_controller['db_index'].resource)
    api.add_resource(db_index_controller['db_indices'], db_index_controller['db_indices'].resource)
    api.add_resource(db_index_controller['db_index_by_name'], db_index_controller['db_index_by_name'].resource)

    apiController = ApiModule.controller
    api.add_resource(apiController['searchMovie'], apiController['searchMovie'].resource)
    api.add_resource(apiController['indexMovie'], apiController['indexMovie'].resource)
    api.add_resource(apiController['indexByFile'], apiController['indexByFile'].resource)

    esController = EsModule.controller
    api.add_resource(esController['createIndex'], esController['createIndex'].resource)
    api.add_resource(esController['deleteIndex'], esController['deleteIndex'].resource)
    api.add_resource(esController['getAllIndicies'], esController['getAllIndicies'].resource)
    api.add_resource(esController['exactSearch'], esController['exactSearch'].resource)
    api.add_resource(esController['singleFieldSearch'], esController['singleFieldSearch'].resource)
    api.add_resource(esController['multiFieldSearch'], esController['multiFieldSearch'].resource)
    api.add_resource(esController['advancedSearch'], esController['advancedSearch'].resource)
    api.add_resource(esController['getDocByImdbId'], esController['getDocByImdbId'].resource)
    api.add_resource(esController['getDistinctValues'], esController['getDistinctValues'].resource)
    api.add_resource(esController['getEditValues'], esController['getEditValues'].resource)
    api.add_resource(esController['indexFolder'], esController['indexFolder'].resource)
    api.add_resource(esController['editDoc'], esController['editDoc'].resource)
    api.add_resource(esController['deleteMovieByDocId'], esController['deleteMovieByDocId'].resource)
    api.add_resource(esController['getIndexMappingInfo'], esController['getIndexMappingInfo'].resource)
    api.add_resource(esController['getIndex'], esController['getIndex'].resource)
    api.add_resource(esController['getFieldsAsTextMap'], esController['getFieldsAsTextMap'].resource)


    @app.route('/test/')
    def test_page():
        # Access the app.config and convert it to a dictionary
        config_dict = {key: value for key, value in app.config.items()}
        # Filter out timedelta objects from the dictionary
        filtered_dict = {key: value for key, value in config_dict.items() if not isinstance(value, timedelta)}
        return jsonify(filtered_dict)
    
    return app
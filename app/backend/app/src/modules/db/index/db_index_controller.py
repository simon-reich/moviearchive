from flask_restful import Resource, reqparse
from src.modules.db.index.db_index_service import DbIndexService

index_args = reqparse.RequestParser()

class DbIndex(Resource):
    resource = '/db/index/<int:id>'

    def get(self, id):
        return DbIndexService.get_by_id(id)

    def update(self):
        pass

    def delete(self, id):
        return DbIndexService.delete_by_id(id)

class DbIndices(DbIndex):
    resource = '/db/index'
    
    def get(self):
        return DbIndexService.get_all()

    def post(self):
        index_args.add_argument("name", type=str)
        index_args.add_argument("schema", type=str)
        dto = index_args.parse_args()        
        return DbIndexService.create_index(dto)

class DbIndexByName(DbIndex):
    resource = '/db/index/<string:name>'

    def get(self, name):
        return DbIndexService.get_by_name(name)

    def update(self):
        pass

    def delete(self, name):
        return DbIndexService.delete_by_name(name)
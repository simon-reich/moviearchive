from flask_restful import Resource, reqparse
from src.modules.db.user.db_user_service import DbUserService

user_args = reqparse.RequestParser()

class DbUser(Resource):
    resource = '/db/user/<int:id>'

    def get(self, id):
        user = DbUserService.get_by_id(id)
        print(user)
    
    def update(self):
        pass

    def delete(self):
        pass

class DbUsers(DbUser):
    resource = '/db/users'
    
    def get(self):
        return DbUserService.get_all()

    def post(self):
        user_args.add_argument("username", type=str)
        user_args.add_argument("email", type=str)
        dto = user_args.parse_args()        
        return DbUserService.create_user(dto)
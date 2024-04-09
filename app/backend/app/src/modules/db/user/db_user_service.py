from src.modules.db.user.db_user_model import DbUserModel

class DbUserService:
    def get_by_id(id):
        return DbUserModel.get_by_id(id)
    
    def get_by_email(email):
        return DbUserModel.get_by_email(email)
    
    def get_all():
        users = DbUserModel.get_all()
        results = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email
            } for user in users]
        return {"count": len(results), "users": results}
    
    def create_user(user):
        new_user = DbUserModel.create(user)
        return {"message": f"user {new_user.username} {new_user.email} has been created successfully."}
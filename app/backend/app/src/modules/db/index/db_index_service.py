from src.modules.db.index.db_index_model import DbIndexModel
from src.modules.db.database import db

class DbIndexService:
    def get_by_id(id):
        return DbIndexModel.get_by_id(id)
    
    def get_by_name(name):
        return DbIndexModel.get_by_name(name)
    
    def get_all():
        indices = DbIndexModel.get_all()
        results = [
            {
                "id": index.id,
                "name": index.name,
                "schema": index.schema
            } for index in indices]
        return {"count": len(results), "indices": results}
    
    def create_index(index):
        new_index = DbIndexModel.create(index)
        return {"message": f"index {new_index.name} {new_index.id} has been created successfully."}
    
    def delete_by_id(id):
        return DbIndexModel.delete_by_id(id)
    
    def delete_by_name(name):
        return DbIndexModel.delete_by_name(name)

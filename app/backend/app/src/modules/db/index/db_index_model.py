from src.modules.db.database import db

class DbIndexModel(db.Model):
    __tablename__ = 'index'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    schema = db.Column(db.String(), nullable=False)


    def get_by_id(id):
        return DbIndexModel.query.get(id)

    def get_by_name(name):
        return DbIndexModel.query.filter_by(name=name).first()

    def get_all():
        return DbIndexModel.query.all()
    
    def create(index):
        new_index = DbIndexModel(
            name=index['name'], 
            schema=index['schema']
        )
        db.session.add(new_index)
        db.session.commit()
        return new_index


    def update(index):
        pass


    def delete_by_id(id):
        index = DbIndexModel.query.get(id)
        if index:
            db.session.delete(index)
            db.session.commit()
            return True  
        else:
            return False  
    

    def delete_by_name(name):
        index = DbIndexModel.query.filter_by(name=name).first()
        if index:
            db.session.delete(index)
            db.session.commit()
            return True  
        else:
            return False


    def __init__(self, name, schema):
        self.name = name
        self.schema = schema

    def __repr__(self):
        return f"<Index {id} {self.name} {self.schema}>"
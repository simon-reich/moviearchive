from src.modules.db.database import db

class DbUserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)


    def get_by_id(id):
        return DbUserModel.query.get(id)

    def get_by_email(email):
        return DbUserModel.query.filter_by(email=email).first()

    def get_all():
        return DbUserModel.query.all()
    
    def create(user):
        new_user = DbUserModel(
            username=user['username'], 
            email=user['email']
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user


    def update(user):
        pass


    def delete(id):
        user = DbUserModel.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True  
        else:
            return False  


    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f"<User {id} {self.username} {self.email}>"
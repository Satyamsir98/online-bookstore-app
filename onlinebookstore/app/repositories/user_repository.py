from app.extensions import db
from app.models.user_model import User  # Import the User model

class UserRepository:
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create_user(user):
        db.session.add(user)
        db.session.commit()
        
    @staticmethod
    def get_users_by_role(role):
        return User.query.filter_by(role=role).all()
    
    @staticmethod
    def get_all_users():
        return User.query.all()  # This will return all users

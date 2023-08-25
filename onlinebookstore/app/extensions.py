from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
# from flask_cors import CORS
from flask_bcrypt import Bcrypt



# Initialize extensions
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

# def init_extensions(app):
#     CORS(app)  # This allows requests from the Angular frontend

# Initialize the Bcrypt object
bcrypt = Bcrypt()

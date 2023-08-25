from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.extensions import db, ma, jwt
from .extensions import bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}}, supports_credentials= True)  
    # CORS(app, resources={r"/orderbp/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)
    CORS(app, resources={r"/*": {"origins": "*"}},supports_credentials= True)
    # CORS(app, resources={r"/orderbp/*": {"origins": "http://localhost:4200", "methods": ["GET", "POST", "PUT", "OPTIONS"]}})


    # Initialize extensions with the app
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Create the database tables (for initial setup)
    with app.app_context():
        db.create_all()

    return app

class Config:
    # Base configuration
    SECRET_KEY = 'supersecretkey'  # Change this in production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bookstore.db'  # SQLite database path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'superjwtsecretkey' 
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Token expires in 1 hour

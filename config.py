import os

class Config:
    # Database setup (replace with your MySQL credentials)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://root:123abc@localhost/codebuddy_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # To suppress warnings

    # JWT setup (secret key for encoding JWT tokens)
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-secret-key')  # Change this in production

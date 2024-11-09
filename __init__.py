from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialize the extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    # Create the Flask app instance
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Register routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app

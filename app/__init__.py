from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    # Enable CORS
    CORS(app)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)

    # Register routes
    from app.routes import todo_bp
    app.register_blueprint(todo_bp, url_prefix="/api/todos")

    return app

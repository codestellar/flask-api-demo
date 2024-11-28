from flask import Flask
from app.shared.db import db, ma
from app.shared.config import Config
from flask_cors import CORS

# Import Blueprints
from app.todo import todo_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    CORS(app)

    # Register Blueprints
    app.register_blueprint(todo_bp, url_prefix="/api/todos")

    return app

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

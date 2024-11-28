from flask import Blueprint

todo_bp = Blueprint("todo", __name__)

from app.todo.routes import todo_bp

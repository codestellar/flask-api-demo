from app.todo.models import Todo
from app.shared.db import db

class TodoService:
    @staticmethod
    def get_all_todos():
        return Todo.query.all()

    @staticmethod
    def get_todo_by_id(todo_id):
        return Todo.query.get(todo_id)

    @staticmethod
    def create_todo(data):
        todo = Todo(**data)
        db.session.add(todo)
        db.session.commit()
        return todo

    @staticmethod
    def update_todo(todo_id, data):
        todo = Todo.query.get(todo_id)
        if todo:
            for key, value in data.items():
                setattr(todo, key, value)
            db.session.commit()
        return todo

    @staticmethod
    def delete_todo(todo_id):
        todo = Todo.query.get(todo_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
        return todo

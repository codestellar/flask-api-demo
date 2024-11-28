from flask import Blueprint, request, jsonify
from app.todo.services import TodoService
from app.todo.schemas import todo_schema, todos_schema

todo_bp = Blueprint("todos", __name__)

@todo_bp.route("/", methods=["GET"])
def get_todos():
    todos = TodoService.get_all_todos()
    return jsonify(todos_schema.dump(todos))

@todo_bp.route("/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = TodoService.get_todo_by_id(todo_id)
    if not todo:
        return jsonify({"message": "Todo not found"}), 404
    return todo_schema.jsonify(todo)

@todo_bp.route("/", methods=["POST"])
def create_todo():
    data = request.json
    todo = TodoService.create_todo(data)
    return todo_schema.jsonify(todo), 201

@todo_bp.route("/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.json
    todo = TodoService.update_todo(todo_id, data)
    if not todo:
        return jsonify({"message": "Todo not found"}), 404
    return todo_schema.jsonify(todo)

@todo_bp.route("/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = TodoService.delete_todo(todo_id)
    if not todo:
        return jsonify({"message": "Todo not found"}), 404
    return jsonify({"message": "Todo deleted"})

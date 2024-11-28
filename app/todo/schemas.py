from app.shared.db import ma

class TodoSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "description", "completed")
        ordered = True

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

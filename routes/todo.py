from flask import request
from flask_smorest import Blueprint
from flask.views import MethodView
from database import db
from models.todo_model import Todo

todos_blp = Blueprint("todo", __name__, description = "Routes for items")

@todos_blp.route('/todo')
class TodoResource(MethodView):
    def get(self):
            id = request.args.get('id')
            if id is None:
                todos = Todo.query.all()
                return (todos)
            id - int(id)
            todo = Todo.query.filter_by(id = id).first()
            return (todo)

    def post(self):
        data = request.get_json()
        new_todo = Todo(
        title = data["title"],
        description = data["description"])
        try:
             db.session.add(new_todo)
             db.session.commit()
             return {"todo": "Todo Added Successfully"}
        except Exception as e:
             db.session.rollback()
             return {"Error": str(e)}
        

    def put(self):
        pass

    def delete(self):
        pass
from flask import request
from flask_smorest import Blueprint
from flask.views import MethodView
from database import db
from models.users_model import Users

user_blp = Blueprint("user",__name__, description = "Users Routes")

@user_blp.route("/user")
class UserResources(MethodView):
    def get(self):
        id = request.args.get('id')
        if id is None:
            users = Users.query.all()
        id = int(id)
        user = Users.query.filter_by(id=id).first()
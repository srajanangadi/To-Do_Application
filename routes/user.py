from flask import request, jsonify
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from database import db
from models.users_model import Users
from schemas.user_schema import UserGetSchema, UserPostSchema, MessageSchema, UserPutSchema

user_blp = Blueprint("user",__name__, description = "Users Routes")

@user_blp.route("/user")
class UserResources(MethodView):
    
    @user_blp.arguments(UserGetSchema, location='query')
    @user_blp.response(201, MessageSchema)
    def get(self, id):
        id = id.get('id')
        user = Users.query.filter_by(id=id).first()
        if user is None:
            abort(404, message="User")
        else:
            return jsonify({"username":user.username}), 200

    @user_blp.arguments(UserPostSchema)
    @user_blp.response(200, MessageSchema)
    def post(self, data):
        user_exists = Users.query.filter_by(username=data.get("username")).first()
        if user_exists:
            abort(400, message="Username already Exist")
        user=Users(username=data.get("username"),password = data.get("password"))
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({"msg":"User Registered Successfully","id":user.id}), 200
        except:
            db.session.rollback()
            abort(400, "Couldn't Register")

    @user_blp.arguments(UserPutSchema)
    @user_blp.response(200, MessageSchema)
    def put(self, data):
        user_exist = Users.query.filter_by(id=data.get('id')).first()
        if user_exist is None:
            abort(400, message="User Doesn't Exists")
        else:
            try:
                user_exist.username = data.get("username")
                user_exist.password = data.get("password")
                db.session.commit()
                return {"msg":"user Updated Successfully"}, 200
            except:
                abort(400, message="Internal Error")

    @user_blp.arguments(UserPutSchema)
    @user_blp.response(200, MessageSchema)
    def delete(self, data):
        user_exist = Users.query.filter_by(id = data.get('id')).first()
        if user_exist is None:
            abort(400, message="No user found to Delete")
        else:
            if user_exist.username != data.get('username') or user_exist.password != data.get('password'):
                abort(400, message="Invalid Password or Username")
            try:
                db.session.delete(user_exist)
                db.session.commit()
                return {"msg":"User Deleted Succefully"}, 200
            except:
                db.session.rollback()
                return {"msg": "Internal Error"}, 400
            
from flask import Blueprint, render_template, redirect, session, request
from models.todo_model import Todo
from models.users_model import Users
from database import db

pages_blp = Blueprint('pages', __name__, description = "Pages Routes")

@pages_blp.route("/login", method=["GET","POST"])
def login():

    if request.method == "POST":
        username=request.form.get("username")
        password=request.form.get("password")

        user = Users.query.filter_by(username=username, password=password).first

        if user:
            session["user_id"] = user.id
            return redirect("/todos")
        
        return "Invalid Username or Password"
    return render_template("login.html")
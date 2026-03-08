from flask import Flask, render_template, request, redirect,url_for
from models import Todo, Users
from database import db
from flask_smorest import Api
from routes.todo import todos_blp
from routes.user import user_blp

app=Flask(__name__)
app.config["API_TITLE"] = "My Store API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.route("/")
def home():
    return render_template("index.html")

api = Api(app)

api.register_blueprint(todos_blp)
api.register_blueprint(user_blp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)

# @app.route('/delete/<int:sno>')
# def delete(sno):
#     pass    

# @app.route('/update/<int:sno>', methods=["POST", "GET"])
# def update(sno):
#     if request.form.get('_method') == "PUT":
#         title = (request.form['title'])
#         description = (request.form['description'])
#         todo = Todo.query.filter_by(sno=sno).first()
#         todo.title = title
#         todo.description = description
#         db.session.add(todo)
#         db.session.commit()
#         return redirect(url_for("hello_world"))

#     todo = Todo.query.filter_by(sno=sno).first()
#     return render_template('update.html', todo=todo)

# @app.route('/login')
# def login():
#     return render_template('login.html')


# @app.route('/show')
# def products():
#     allTodo = Todo.query.all()
#     print(allTodo)
#     return f"This is the result of your query"
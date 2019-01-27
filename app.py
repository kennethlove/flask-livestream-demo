import os
import sqlite3

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import redirect
from flask import url_for

from flask_wtf.csrf import CSRFProtect

import forms
import models

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
CSRFProtect(app)


@app.route("/")
def index():
    return "Index"


@app.route("/hello/")
@app.route("/hello/<string:name>")
def hello(name="World"):
    context = {
        'name': name
    }
    return render_template("hello.html", **context)

# {"name": "Kenneth"} -> name="Kenneth"


@app.route("/api/v1/users")
def users():
    database_users = models.User.select()
    usernames = [
        {"username": user.username}
        for user in database_users
    ]
    return jsonify(usernames)


@app.route("/api/v1/usernames")
def usernames():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM user")
    database_users = c.fetchall()
    usernames = [
        {"id": user[0], "username": user[1]}
        for user in database_users
    ]
    return jsonify(usernames)


@app.route("/register", methods=("GET", "POST"))
def register():
    form = forms.NewUserForm()
    if form.validate_on_submit():
        models.User.create(
            username=form.username.data
        )
        return redirect(url_for("users"))
    return render_template("register.html", form=form)


models.db.connect()
models.db.create_tables([
    models.User,
])
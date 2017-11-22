from flask import Flask, render_template, redirect, url_for, session, request, flash
import os
from utils import api, db

USER_SESSION = "logged_in"

app = Flask(__name__)
app.secret_key = os.urandom(16)

def is_null(username, password, confpw):
    return username == "" or password == "" or confpw == ""

def add_session(username, password):
    if is_null(username, password, "filler"):
            flash("Username or password is blank")
            return False
    if(db.login(username, password)):
        session[USER_SESSION] = username
        return True
    else:
        flash("Incorrect login credentials")
        return False

@app.route("/")
def root():
    return render_template("home.html", top_songs = api.get_top_songs(), in_session = USER_SESSION in session)

@app.route("/login", methods=["GET", "POST"])
def login():
    if (request.method == "GET"):
        return render_template("login.html")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if add_session(username, password):
            return redirect(url_for("home"))
        return render_template("login.html")     

@app.route("/create", methods=["GET", "POST"])
def create():
    if !request.method == "GET":
        username = request.form["username"]
        password = request.form["password"]
        confirm_passsword = request.form["confirm_password"]
        if is_null(username, password, confirm_password):
            flash("A field was left empty")
        elif password != confirm_password:
            flash("Password and password confirmation do not match")
        else:
            if !create_account(username, password):
                flash("Username taken")
            else:
                return redirect(url_for("login"))
    return render_template("create.html")

@app.route("/profile")
def profile():
    pass

@app.route("/song")
def song():
    pass

@app.route("/artist")
def artist():
    pass

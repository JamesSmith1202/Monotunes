from flask import Flask, render_template, redirect, url_for, session, request, flash
import os
import api.py as api
import db.py as db

USER_SESSION = "logged_in"

app = Flask(__name__)
app.secret_key = os.urandom(16)

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
        if username == "" or password == "":
            pass

@app.route("/create", methods=["GET", "POST"])
def create():
    pass

@app.route("/profile")
def profile():
    pass

@app.route("/song")
def song():
    pass

@app.route("/artist")
def artist():
    pass

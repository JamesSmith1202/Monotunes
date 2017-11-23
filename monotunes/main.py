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
    if(db.login(username, password)):#if credentials match up in the db...
        session[USER_SESSION] = username
        return True
    else:
        flash("Incorrect login credentials")
        return False

@app.route("/")
def root():
    return render_template("home.html", top_songs = api.get_top_songs())

@app.route("/login", methods=["GET", "POST"])
def login():
    if USER_SESSION in session:
        return redirect(url_for("/"))
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
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_passsword = request.form["confirm_password"]
        if is_null(username, password, confirm_password):
            flash("A field was left empty")
        elif password != confirm_password:
            flash("Password and password confirmation do not match")
        else:
            if not create_account(username, password):
                flash("Username taken")
            else:
                return redirect(url_for("login"))
    return render_template("create.html")

@app.route("/profile", methods = ["GET", "POST"])
def profile():
    if (request.method == "GET"):
        if not USER_SESSION in session:
            return redirect(url_for("/login")) 
        return render_template("profile.html", username = session[USER_SESSION], favorites = db.get_favorites(username))
    db.remove_favorite(session[USER_SESSION], request.form["songID"])#must be a post request so remove the desired song
    return redirect(url_for("/profile"))

@app.route("/song", methods = ["GET", "POST"])
def song(title, artist):
    if request.method == "GET":
        id = api.get_song_id(title, artist)
        if id == 0:#if the song was not found
            return render_template("error.html", title = title, artist = artist)
        return render_template("song.html", title = title, artist = artist, lyrics = get_lyrics(id), id = id)#return page
    if "favorite" in request.form:#if they want to add to favorites
        if USER_SESSION in session:#check if user in session
            db.add_favorite(session[USER_SESSION], request.form["favorite"])#add the song to their fav
            return render_template("song.html", title = title, artist = artist, lyrics = get_lyrics(id), id = id)#re render the page
            flash("Song has been added to your favorites")
        else:
            return redirect(url_for("login"))#if they arent logged in, then send them to the login page
    elif "search_artist" in request.form:#if they wanted to search by artist
        return redirect(url_for("/artist", artits = request.form["search_artist"]))#send them to the artist page
    return redirect(url_for("/song", title = request.form["title"], artist = request.form["artist"]#re render the page by sending another request with the form info

@app.route("/artist")
def artist():
    pass

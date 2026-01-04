import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///games.db")

@app.after_request
def after_request(response):
    
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/login", methods=["GET", "POST"])
def login():

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("apology.html", message="Senha incorreta!", cor="danger")

        elif not request.form.get("password"):
            return render_template("apology.html", message="Senha incorreta!", cor="danger")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("apology.html", message="invalid username and/or password")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        caixa = request.form.get("caixa")
        tipo = db.execute("SELECT * FROM games WHERE nome LIKE ?", f"%{caixa}%")

        return render_template("busca.html", games=tipo)

    else:
        return render_template("index.html")

@app.route("/logout")
@login_required
def logout():

    session.clear()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username").strip():
            return render_template("apology.html", message="invalid username")

        if not request.form.get("password").strip():
            return render_template("apology.html", message="The passwords do not match")

        if not request.form.get("confirmation").strip():
            return render_template("apology.html", message="The passwords do not match")

        userrow = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if userrow:
            return render_template("apology.html", message="Username already taken")

        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("apology.html", message="passwords do not match")
        hashpass = generate_password_hash(request.form.get("password"))
        novo_id = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hashpass)
        session["user_id"] = novo_id
        return redirect("/")

    else:
        return render_template("register.html")




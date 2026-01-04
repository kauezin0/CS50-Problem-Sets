import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    linhas = db.execute("SELECT symbol, shares FROM transactions WHERE user_id = ?", session["user_id"])

    resumo_acoes = {}
    for linha in linhas:
        simbolo = linha["symbol"]
        quantidade = linha["shares"]

        if simbolo not in resumo_acoes:
            resumo_acoes[simbolo] = quantidade
        else:
            resumo_acoes[simbolo] += quantidade

    usuario = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    dinheiro_vivo = usuario[0]["cash"]

    tabela_final = []
    total_patrimonio = dinheiro_vivo

    for simbolo, quantidade in resumo_acoes.items():

        if quantidade > 0:
            dados = lookup(simbolo)
            valor_total_daquela_acao = dados["price"] * quantidade


            item = {"symbol": simbolo, "name": dados["name"], "shares": quantidade, "price": dados["price"], "total": valor_total_daquela_acao}
            tabela_final.append(item)


            total_patrimonio += valor_total_daquela_acao


    return render_template("index.html", portfolio=tabela_final, cash=dinheiro_vivo, total=total_patrimonio)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":

        #Seguranca

        if not request.form.get("symbol"):
                return apology("must provide symbol")

        if not request.form.get("shares"):
            return apology("must provide share")

        symbol = request.form.get("symbol")
        symbolv = lookup(symbol)

        if symbolv is None:
            return apology("invalid")

        shares_input = request.form.get("shares")

        if not shares_input or not shares_input.isdigit():
            return apology("invalid number of shares")

        shares = int(shares_input)

        #ve se tem dinheiro

        custa = symbolv["price"] * shares
        consulta = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        linha = consulta[0]["cash"]

        if linha < custa:
            return apology("Don't have money")
        elif linha >= custa:
            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", custa, session["user_id"])
            db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], symbolv["symbol"], shares, symbolv["price"])
            return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    linhas = db.execute("SELECT * FROM transactions WHERE user_id = ? ORDER BY timestamp", session["user_id"])

    return render_template("history.html", transacoes=linhas)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():

    if request.method == "POST":

        symbol = request.form.get("symbol")
        if not symbol:
            return apology("invalid")

        quote1 = lookup(symbol)

        if quote1 == None:
            return apology("invalid")

        return render_template("quoter.html", estoque=quote1)

    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # verificacao de campo vazio

    if request.method == "POST":
        if not request.form.get("username").strip():
            return apology("must provide username")

        if not request.form.get("password").strip():
            return apology("must provide password")

        if not request.form.get("confirmation").strip():
            return apology("must provide password confirmation")

    #verifica se o user existe

        userrow = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if userrow:
            return apology("username already taken")

    #verifica senha e a transforma em hash


        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match") # O robô EXIGE este retorno
        hashpass = generate_password_hash(request.form.get("password"))
        novo_id = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get("username"), hashpass)
        session["user_id"] = novo_id
        return redirect("/")

    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    if request.method == "POST":
        if not request.form.get("symbol").strip():
            return apology("must provide symbol")

        if not request.form.get("shares").strip():
            return apology("must provide password")

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        rows = db.execute("SELECT SUM(shares) AS total FROM transactions WHERE user_id = ? AND symbol = ?", session["user_id"], symbol)
        total_acoes = rows[0]["total"]


        if not total_acoes or int(shares) > total_acoes:
            return apology("You do not have enough shares.")

        dados_atuais = lookup(symbol)
        valor_total_venda = dados_atuais["price"] * int(shares)

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", valor_total_venda, session["user_id"])

        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)", session["user_id"], symbol, -int(shares), dados_atuais["price"])

        return redirect("/")

    else:
        acoes = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])
        return render_template("sell.html", acoes=acoes)


@app.route("/cash", methods=["GET", "POST"])
@login_required
def addcash():
    if request.method == "POST":
        cashe = request.form.get("cash")
        if not cashe:
            return apology("must provide cash")

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", cashe, session["user_id"])

        return redirect("/")

    else:

        return render_template("adicionarcash.html")

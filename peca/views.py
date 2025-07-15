from flask import render_template, request, make_response, jsonify

from peca import app, db
from peca.models import Product


@app.route("/", methods=["GET", "POST"])
def base():
    dados = Product.query.all()
    if request.method == "GET":
        print("")
    if request.method == "POST":
        name = request.form["name"]
        type = request.form["tipo"]
        produtos = Product(name=name, tipo=type)

        db.session.add(produtos)
        db.session.commit()

    return render_template("base.html", dados=dados)


@app.route("/index")
def index():
    dados = db.Query.all()
    return render_template("index.html", dados=dados)


def select_dados():
    return

from flask import render_template, request, make_response

from peca import app, db
from peca.models import Product


@app.route("/", methods=["GET", "POST"])
def base():
 
    if request.method == "GET":
        print("")
    if request.method == "POST":
        name = request.form['name']
        type = request.form['tipo']
        produtos = Product(name=name, tipo= type)

        db.session.add(produtos)
        db.session.commit()

    return render_template("base.html")


@app.route("/index")
def index():
    return render_template("index.html")


def select_dados():
    return

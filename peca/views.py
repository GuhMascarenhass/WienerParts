from flask import render_template, request, make_response, jsonify, flash

from peca import app, db
from peca.models import Product, Form_product


@app.route("/", methods=["GET", "POST"])
def base():
    dados = Product.query.all()
    form = Form_product(request.form)
    if request.method == "GET":
        print("")
    if request.method == "POST" and form.validate():
        peca = Product(name=form.name.data, tipo=form.type.data)
        db.session.add(peca)
        flash("Peca salva com sucesso!!")
        db.session.commit()

    return render_template("base.html", dados=dados, form=form)


@app.route("/index")
def index():
    dados = db.Query.all()
    return render_template("index.html", dados=dados)


def select_dados():
    return

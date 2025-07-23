from flask import render_template, request, flash, redirect
from peca import app, db
from peca.models import Product, Form_product


@app.route("/")
def home():
    form = Form_product(request.form)
    dados_banco = Product.query.all()
    return render_template("base.html", dados=dados_banco, form=form)


@app.route("/enviar", methods=["GET", "POST"])
def create_product():
    form = Form_product(request.form)

    if request.method == "GET":
        print("")
    if request.method == "POST" and form.validate():
        peca = Product(name=form.name.data, tipo=form.type.data)
        db.session.add(peca)
        flash("Peca salva com sucesso!!")
        db.session.commit()

    return redirect("/")


@app.route("/update", methods=["POST"])
def update_product():
    return


@app.route("/delete/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    id_delete = Product.query.get(product_id)
    db.session.delete(id_delete)
    db.session.commit()
    return redirect("/")

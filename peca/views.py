from flask import render_template, request, flash, redirect
from peca import app, db
from peca.models import Product, Form_product


@app.route("/")
def home():
    form = Form_product(request.form)
    dados_banco = Product.query.all()
    return render_template("crudProd.html", dados=dados_banco, form=form)


@app.route("/enviar", methods=["GET", "POST"])
def create_product():
    form = Form_product(request.form)
    if request.method == "POST" and form.validate():
        peca = Product(name=form.name.data, tipo=form.type_field.data)
        db.session.add(peca)
        db.session.commit()

    return redirect("/")


@app.route("/update/<int:product_id>", methods=["POST", "GET"])
def update_product(product_id):
    produto = Product.query.get_or_404(product_id)
    if request.method == "POST":
        form = Form_product(request.form)
        if form.validate():
            produto.name = form.name.data
            produto.tipo = form.type_field.data
            db.session.commit()
            return redirect("/")
    else:
        form = Form_product(obj=produto)
        form.type_field.data = produto.tipo
    return render_template("editar.html", form=form, produto=produto)


@app.route("/delete/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    id_delete = Product.query.get(product_id)
    db.session.delete(id_delete)
    db.session.commit()
    return redirect("/")

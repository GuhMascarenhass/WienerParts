from peca import db
from wtforms import Form, StringField, SubmitField, validators
from flask_wtf import FlaskForm, CSRFProtect


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    tipo = db.Column(db.String(50))


class Form_product(FlaskForm):
    name = StringField("Nome da peça", [validators.Length(min=3, max=40)])
    type = StringField("Tipo da peça", [validators.Length(min=3, max=40)])
    send = SubmitField("Salvar")

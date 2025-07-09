from peca import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50))
    tipo = db.Column(db.String(50))

from erpdam2 import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    description = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey("product_category.id"))
    transactions = db.relationship("ProductTransaction", back_populates="product")

    def __init__(self, name, description, quantity, price, picture, category_id=None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.picture = picture
        self.category_id = category_id

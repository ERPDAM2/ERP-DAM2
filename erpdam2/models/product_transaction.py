from erpdam2 import db


class ProductTransaction(db.Model):
    __tablename__ = "product_transaction"

    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), primary_key=True)
    transaction_id = db.Column(
        db.Integer, db.ForeignKey("transactions.id"), primary_key=True
    )
    transaction = db.relationship("Transaction", back_populates="products")
    product = db.relationship("Product", back_populates="transactions")

    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

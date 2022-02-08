from erpdam2 import db
import datetime


products = db.Table(
    "products_transactions",
    db.Column("product_id", db.Integer, db.ForeignKey("products.id"), primary_key=True),
    db.Column(
        "transaction_id", db.Integer, db.ForeignKey("transactions.id"), primary_key=True
    ),
)


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    products = db.relationship(
        "Product",
        secondary=products,
        lazy="subquery",
        backref=db.backref("transactions", lazy=True),
    )
    provider_id = db.Column(db.Integer, db.ForeignKey("contacts.id"), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(8), nullable=False, default="purchase")

    def __init__(
        self,
        id_product,
        id_provider,
        price,
        quantity,
        transaction_type="purchase",
    ):
        self.id_product = id_product
        self.id_provider = id_provider
        self.price = price
        self.quantity = quantity
        self.transaction_type = transaction_type

    @staticmethod
    def from_sale(
        id_product,
        id_provider,
        price,
        quantity,
    ):
        return Transaction(id_product, id_provider, price, quantity, "sale")

    @staticmethod
    def from_purchase(
        id_product,
        id_provider,
        price,
        quantity,
    ):
        return Transaction(id_product, id_provider, price, quantity)

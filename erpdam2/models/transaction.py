from erpdam2 import db
import datetime
from erpdam2.models import BaseClass


class Transaction(BaseClass):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey("contacts.id"), nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    transaction_type = db.Column(db.String(8), nullable=False, default="purchase")
    products = db.relationship("ProductTransaction", back_populates="transaction")

    def __init__(
        self,
        id_provider,
        price,
        quantity,
        transaction_type="purchase",
    ):
        self.id_provider = id_provider
        self.price = price
        self.quantity = quantity
        self.transaction_type = transaction_type

    @staticmethod
    def get_all_from_provider_id(id):
        return Transaction.query.filter(Transaction).filter(provider_id=id)

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

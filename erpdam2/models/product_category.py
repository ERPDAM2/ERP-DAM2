from erpdam2 import db
from erpdam2.models import BaseClass


class ProductCategory(BaseClass):
    __tablename__ = "product_category"

    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(
        db.Integer, db.ForeignKey("product_category.id"), nullable=True
    )
    name = db.Column(db.String(50), nullable=False)
    subcategories = db.relationship(
        "ProductCategory", backref=db.backref("parent", remote_side=[id])
    )
    products = db.relationship("Product", backref="category", lazy=True)

    def __init__(self, name, parent_id=None):
        self.name = name

from flask import Blueprint

products = Blueprint("products", __name__)


@products.route("/products", methods=["GET", "POST"])
def productsRoute():
    return ""

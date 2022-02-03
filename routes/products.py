from flask import Blueprint, request

products = Blueprint("products", __name__)

@products.route("/products", methods=["GET", "POST"])
def productsMethod():
    return ""

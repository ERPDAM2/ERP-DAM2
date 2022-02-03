from flask import Blueprint, request

products = Blueprint("products", __name__)

@products.route("/products", methdos=["GET", "POST"])
def products():
    return ""

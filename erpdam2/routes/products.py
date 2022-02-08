from turtle import title
from flask import Blueprint, render_template
from ..View.forms import RegisterSale

products = Blueprint("products", __name__)


@products.route("/sales", methods=["GET", "POST"])
def sales():
    form = RegisterSale()

    return render_template("test.html", form=form, title="Sales")

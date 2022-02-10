<<<<<<< HEAD
from flask import Blueprint, render_template
from erpdam2.View.forms import RegisterProduct

products = Blueprint("products", __name__)

@products.route("/products/add", methods=["GET", "POST"])
def productsRoute():
    form = RegisterProduct()
    
    return render_template("testAltaProductos.html", form=form, title="Alta producto")
=======
from turtle import title
from flask import Blueprint, render_template
from ..View.forms import RegisterSale

products = Blueprint("products", __name__)


@products.route("/sales", methods=["GET", "POST"])
def sales():
    form = RegisterSale()

    return render_template("test.html", form=form, title="Sales")
>>>>>>> b88b761919efcb9365cf6bb24ead0fb2ce1e0f38

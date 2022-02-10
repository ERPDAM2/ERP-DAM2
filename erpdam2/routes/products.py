from flask import Blueprint, render_template
from erpdam2.View.forms import RegisterProduct

products = Blueprint("products", __name__)

@products.route("/products/add", methods=["GET", "POST"])
def productsRoute():
    form = RegisterProduct()
    
    return render_template("testAltaProductos.html", form=form, title="Alta producto")
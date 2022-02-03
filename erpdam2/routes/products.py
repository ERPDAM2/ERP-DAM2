
from flask import Blueprint, render_template
from erpdam2.View.forms import RegisterProduct
from erpdam2.models.user import Product

products = Blueprint("products", __name__)

@products.route("/products/add", methods=["GET", "POST"])
def productsRoute():
    form = RegisterProduct()

    if (form.validate_on_submit()):
        product = Product(id=form.id_product.data, name=form.name_product.data, 
                          description=form.description.data, quantity=form.quantity.data, 
                          price=form.price.data, picture=form.picture.data)
    
    
    return render_template("testAltaProductos.html", form=form, title="Alta producto")


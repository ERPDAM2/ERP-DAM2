from flask import Blueprint, render_template, request
from erpdam2.View.forms import RegisterForm
from erpdam2.models.user import User

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    
    if(form.validate_on_submit()):
        
    
    return render_template("test.html", form=form, title="Register")
    


@users.route("/login", methods=["GET", "POST"])
def login():
    return ""


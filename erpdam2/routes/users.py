
from flask import Blueprint, render_template, request
from erpdam2.View.forms import RegisterForm
from erpdam2.models.user import User

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    
    if(form.validate_on_submit()):
        user = User(email=form.email.data, username=form.username.data, 
                    first_name=form.first_name.data, last_name= form.last_name.data,
                    password=form.password.data)
        
    
    return render_template("test.html", form=form, title="Register")
    


@users.route("/login", methods=["GET", "POST"])
def login():
    return ""


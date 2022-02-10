from audioop import add
import email
from flask import Blueprint
#from turtle import title
from flask import Blueprint, render_template, request,redirect,url_for
from ..View.forms import RegisterContact
from .. import db
#from . import auth
from .. models import contact

clients = Blueprint("clients", __name__)


@clients.route("/clients", methods=["GET", "POST"])
def clientsMethod():
     form = RegisterContact()
     if form.validate_on_submit():
         contactP=contact(
             email = form.email.data,
             phone=form.phone.data,
             picture=form.picture.data,
             address=form.address.data,
             company_name=form.company_name.data,
             first_name=form.first_name.data,
             last_name=form.last_name.data )
        
   
     return render_template("test.html", form=form, title="RegisterClient")

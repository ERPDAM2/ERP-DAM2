from flask import Blueprint, request

users = Blueprint("users", __name__)

@users.route("/register", methods=["GET", "POST"])
def register():
    
    if(request.method == "GET"):
        return "Prueba"
    return "<h1>Funciona</h1>"

@users.route("/login", methods=["GET", "POST"])
def login():
    return "<h1>Inicia sesión</h1>"

from flask import Blueprint, request

users = Blueprint("users", __name__)


@users.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "GET":
        return "Prueba"


@users.route("/login", methods=["GET", "POST"])
def login():
    return ""

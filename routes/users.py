from flask import Blueprint

users = Blueprint("users", __name__)

@users.route("/testusers")
def testusers():
    return "<h1>Funciona</h1>"
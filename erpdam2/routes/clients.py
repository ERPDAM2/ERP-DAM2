from flask import Blueprint

clients = Blueprint("clients", __name__)


@clients.route("/clients", methods=["GET", "POST"])
def clientsRoute():
    return ""

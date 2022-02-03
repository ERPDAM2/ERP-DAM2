from flask import Blueprint, request

clients = Blueprint("clients", __name__)

@clients.route("/clients", methods=["GET", "POST"])
def clientsMethod():
    return ""
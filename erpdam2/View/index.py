#! /usr/bin/env python
# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:
# -*- coding: utf-8 -*-
import json
file = open('static/json/countries.json', 'r')
data = file.read()

countries = json.loads(data)

countriesCode = []
countriesName = []

for i in countries:   
    countriesCode+= i['alpha2'].split('\n')
    countriesName += i['name'].split('\n')

from flask import Flask, render_template, redirect, url_for

productosPlaceholder = ["Producto1", "Producto2", "Producto3 ", "Producto4", "Producto5"]

#authorized = False
authorized = True

index = Flask(__name__)


@index.route("/")
def Index():
    return render_template("index.html", auth=authorized)


@index.route("/validator", methods=["POST"])
def validator():
   # if request.methods == "POST":
    #    user = request.form["User"]
    #    password = request.form["Password"]
    return redirect(url_for("Index"))


@index.route("/productos")
def productos():
    return render_template("productos.html", productos=productosPlaceholder)


@index.route("/configuration")
def configuration():
    return render_template("configuration.html", paises=countriesName)

@index.route("/createuser")
def create_user():
    return render_template("create_user.html")

@index.route("/clients")
def configurationClients():
    return render_template("clients.html")

@index.route("/addClients")
def configurationAddClients():
    return render_template("addClients.html")

if __name__ == "__main__":
    index.run(port=3000, debug=True)
   
    



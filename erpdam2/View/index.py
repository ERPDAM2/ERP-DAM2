#! /usr/bin/env python
# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, url_for

productosPlaceholder = ["Producto1", "Producto2", "Producto3", "Producto4", "Producto5"]

# authorized = True

index = Flask(__name__)


@index.route("/")
def Index():
    return render_template("index.html")


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
    return render_template("configuration.html")


if __name__ == "__main__":
    index.run(port=3000, debug=True)

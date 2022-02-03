import imp
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes.users import users
from routes.products import products
from routes.clients import clients

PORT = 3000
app = Flask(__name__)
db = SQLAlchemy(app)

app.register_blueprint(users)
app.register_blueprint(products)
app.register_blueprint(clients)

@app.route("/")
def main_page():
    return render_template("./index.html")

if(__name__=="__main__"):
    app.run(port= PORT)
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from erpdam2.config import ConfigTest
from erpdam2.routes.users import users
from erpdam2.routes.products import products
from erpdam2.routes.clients import clients

app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager()

app.register_blueprint(users)
app.register_blueprint(products)
app.register_blueprint(clients)

app.config.from_object(ConfigTest())


@app.route("/")
def main_page():
    return render_template("./index.html")

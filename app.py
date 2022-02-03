from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import ConfigTest
from routes.users import users
from routes.products import products
from routes.clients import clients

PORT = 3000
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


if (__name__ == "__main__"):
    app.run(port=PORT)

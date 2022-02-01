from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes.users import users

PORT = 3000
app = Flask(__name__)
db = SQLAlchemy(app)

app.register_blueprint(users)

@app.route("/")
def main_page():
    return render_template("./index.html")

if(__name__=="__main__"):
    app.run(port= PORT)
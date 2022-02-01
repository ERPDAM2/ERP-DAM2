from flask import Flask
from flask_sqlalchemy import SQLAlchemy

PORT = 3000
app = Flask(__name__)
db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

if(__name__=="__main__"):
    app.run(port= PORT)
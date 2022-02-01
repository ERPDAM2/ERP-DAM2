from flask import Flask

PORT = 3000
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello world</p>"

if(__name__=="__main__"):
    app.run(port= PORT)
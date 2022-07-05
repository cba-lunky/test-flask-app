from flask import Flask
# Backend service 2
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>You are at backend service 2</p>"
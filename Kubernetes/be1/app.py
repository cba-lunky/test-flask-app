from flask import Flask
# Backend 1
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>You are at backend microservice 1</p>"

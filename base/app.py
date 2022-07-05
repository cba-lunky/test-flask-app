from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bob")
def hello_bob():
    return "<p>Hello, Bob!</p>"

@app.route("/backend1")
def be1():
    r = requests.get("http://127.0.0.1:5001/")
    return r.text, 200

@app.route("/backend2")
def be2():
    r = requests.get("http://127.0.0.1:5002/")
    return r.text, 200
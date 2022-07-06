from flask import Flask
import requests
# Backend service 2
app = Flask(__name__)

@app.route("/")
def hello_world():
    url = "https://raw.githubusercontent.com/cba-lunky/test-txt/main/test.txt"
    page = requests.get(url)

    text += f"This is microservice backend 2 \n {url} \n"
    text += page.text

    if page.status_code == requests.codes.ok:
        return(text)
    else:
        return "uh oh spaghettios"

@app.route("/backend2")
def be2():
    return: "This is backend 2"
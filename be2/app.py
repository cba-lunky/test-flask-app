from flask import Flask
import requests
# Backend service 2
app = Flask(__name__)

@app.route("/")
def hello_world():
    url = "https://raw.githubusercontent.com/cba-lunky/test-txt/main/test.txt"
    page = requests.get(url)

    if page.status_code == requests.codes.ok:
        return(page.text)
    else:
        return "uh oh spaghettios"
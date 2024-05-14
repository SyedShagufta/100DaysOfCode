import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/<name>")
def home_page(name):
    ENDPOINT_AGIFY = f"https://api.agify.io?name={name}"
    response = requests.get(ENDPOINT_AGIFY).json()
    ENDPOINT_GENDERIZE = f"https://api.genderize.io?name={name}"
    response1 = requests.get(ENDPOINT_GENDERIZE).json()
    return render_template("index.html", name=name, age=response["age"], gender=response1["gender"])


if __name__ == '__main__':
    app.run()

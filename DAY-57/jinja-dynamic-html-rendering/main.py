from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    current_year = 2024
    my_name = "SOFIA"
    return render_template("index.html", CURRENT_YEAR=current_year, MY_NAME=my_name)


if __name__ == "__main__":
    app.run()



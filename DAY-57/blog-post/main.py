import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_blog():
    blog_url = "https://api.npoint.io/48c73beed1dc13191fc9"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run()

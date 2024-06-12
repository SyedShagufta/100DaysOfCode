import requests
from flask import Flask, render_template

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/18f49b80c208c8ea9e22").json()


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def show_post(index):
    requested_blog = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_blog = blog_post
    return render_template("post.html", post=requested_blog)


if __name__ == '__main__':
    app.run()

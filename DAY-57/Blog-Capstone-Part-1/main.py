from flask import Flask, render_template

from post import Post

app = Flask(__name__)

post_obj = Post()


@app.route('/')
def home():
    return render_template("index.html", posts=post_obj.get_posts())


@app.route('/blog/<int:id_num>')
def blog(id_num):
    return render_template("post.html", posts=post_obj.get_posts(), num=id_num)


if __name__ == "__main__":
    app.run(debug=True)

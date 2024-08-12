from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


class PostForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired()])
    sub_title = StringField(label='Subtitle', validators=[DataRequired()])
    author_name = StringField(label='Author Name', validators=[DataRequired()])
    url_img = StringField(label='Background img', validators=[DataRequired()])
    body = CKEditorField(label='Body', validators=[DataRequired()])
    submit = SubmitField(label='Submit', validators=[DataRequired()])


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = list(db.session.query(BlogPost).all())
    return render_template("index.html", all_posts=posts)


# TODO: Add a route so that you can click on individual posts.
@app.route('/posts/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        sub_title = request.form.get('sub_title')
        author_name = request.form.get('author_name')
        url_img = request.form.get('url_img')
        body = request.form.get('body')

        # Get the current date and format it
        current_date = datetime.now()
        formatted_date = current_date.strftime("%B %d, %Y")

        # Create a new blog post record
        new_create_post = BlogPost(
            title=title,
            subtitle=sub_title,
            author=author_name,
            img_url=url_img,
            body=body,
            date=formatted_date  # Assuming your model has a date_posted field
        )

        # Add the new post to the database session and commit
        db.session.add(new_create_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)


# TODO: edit_post() to change an existing blog post

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)

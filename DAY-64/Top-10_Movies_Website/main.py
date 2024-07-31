from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    add_movie = SubmitField(label="Add Movie")


# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-website-database.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(400), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(400), nullable=False)
    img_url: Mapped[str] = mapped_column(String(300), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(desc(Movies.ranking))).scalars()
    return render_template("index.html", movies_list=result)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        movie_id = request.form["id"]
        movie_to_update = db.get_or_404(Movies, movie_id)
        movie_to_update.rating = request.form["new_rating"]
        movie_to_update.review = request.form["new_review"]
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movies, movie_id)
    return render_template('edit.html', movie=movie_selected)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movies, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add")
def add():
    form = AddForm()
    if form.validate_on_submit():
        print("validated")
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

SEARCH_URL = "https://www.omdbapi.com/?"
API_KEY = "YOUR_API_KEY"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


class EditForm(FlaskForm):
    new_rating = StringField(label="Your Rating out of 10 e.g. 7.5", validators=[DataRequired()])
    new_review = StringField(label="Your Review", validators=[DataRequired()])
    done_btn = SubmitField(label="Done")


class AddForm(FlaskForm):
    movie_title = StringField(label="Movie Title", validators=[DataRequired()])
    add_movie = SubmitField(label="Add Movie")


# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-website-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(400), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(400), nullable=True)
    img_url: Mapped[str] = mapped_column(String(300), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating)).scalars().all()
    for i in range(len(result)):
        result[i].ranking = len(result) - i
    db.session.commit()
    return render_template("index.html", movies_list=result)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get("id")
    movie_to_update = db.get_or_404(Movies, movie_id)
    if edit_form.validate_on_submit():
        movie_to_update.rating = float(edit_form.new_rating.data)
        movie_to_update.review = edit_form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_to_update, form=edit_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = db.get_or_404(Movies, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        movie_title = form.movie_title.data
        response = requests.get(SEARCH_URL, params={"apikey": API_KEY, "t": movie_title})
        if response.status_code == 200:
            data = response.json()
            if data['Response'] == 'True':
                title = data["Title"]
                year = data["Year"]
                description = data["Plot"]
                img_url = data["Poster"]
                new_movie = Movies(title=title, year=int(year), description=description, img_url=img_url)
                db.session.add(new_movie)
                db.session.commit()
                return redirect(url_for('edit', id=new_movie.id))
            else:
                return render_template('add.html', form=form, error="Movie not found.")
        else:
            return render_template('add.html', form=form, error="Failed to fetch movie data.")
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

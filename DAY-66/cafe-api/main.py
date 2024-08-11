from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

actual_api_key = "SofiaTopSecretAPIKey"


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random')
def random_fun():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(cafes)
    # return jsonify(
    #     id=random_cafe.id,
    #     name=random_cafe.name,
    #     map_url=random_cafe.map_url,
    #     image_url=random_cafe.img_url,
    #     location=random_cafe.location,
    #     has_sockets=random_cafe.has_sockets,
    #     has_toilet=random_cafe.has_toilet,
    #     has_wifi=random_cafe.has_wifi,
    #     can_take_calls=random_cafe.can_take_calls,
    #     seats=random_cafe.seats,
    #     coffee_price=random_cafe.coffee_price
    # )
    return jsonify(cafe=random_cafe.to_dict())


# HTTP GET - Read Record
@app.route('/all')
def all_cafes():
    cafes = db.session.query(Cafe).all()
    get_all_cafes = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=get_all_cafes)


@app.route('/search')
def find_cafe():
    loc = request.args.get("loc")
    wanted_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if not wanted_cafes:
        return jsonify(error={
            "Not Found": "Sorry, we don't have a cafe at that location."
        })
    wanted_cafes_loc = [cafe.to_dict() for cafe in wanted_cafes]
    return jsonify(wanted_cafes_loc)


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=["PATCH"])
def patch_new_cafe(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = db.session.get(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully Updated the price of the Cafe."}), 200
    else:
        return jsonify(error={
            "Not Found": "Sorry a Cafe with that id is not found in the database"
        }), 400


# HTTP DELETE - Delete Record
@app.route('/report-closed/<int:delete_cafe_id>', methods=['DELETE'])
def delete_cafe(delete_cafe_id):
    given_api_key = request.args.get("api-key")
    cafe_to_delete = db.session.get(Cafe, delete_cafe_id)
    if cafe_to_delete and given_api_key == actual_api_key:
        db.session.delete(cafe_to_delete)
        db.session.commit()
        return jsonify(response={"success": "Successfully Updated the price of the Cafe."}), 200
    elif given_api_key != actual_api_key:
        return jsonify(error={
            "Not Found": "Sorry, you are not authorized to make the request!"
        }), 400
    else:
        return jsonify(error={
            "Not Found": "Sorry a Cafe with that id is not found in the database!"
        }), 400


if __name__ == '__main__':
    app.run(debug=True)

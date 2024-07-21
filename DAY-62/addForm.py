from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, ValidationError


def check_url(form, field):
    starts_with = field.data[0:4]
    print(starts_with)
    if starts_with != "http":
        raise ValidationError("Invalid URL")


class AddForm(FlaskForm):
    cafe_name = StringField(label="Cafe Name", validators=[DataRequired()])
    cafe_location = StringField(label="Cafe Location on Google Maps (URL)", validators=[DataRequired(), check_url])
    opening_time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired()])
    closing_time = StringField(label="Closing Time e.g. 5.30PM", validators=[DataRequired()])
    coffee_rating = SelectField(label="Coffee Rating", choices=[
        ('☕', '☕'),
        ('☕☕', '☕☕'),
        ('☕☕☕', '☕☕☕'),
        ('☕☕☕☕', '☕☕☕☕'),
        ('☕☕☕☕☕', '☕☕☕☕☕')
    ], validators=[DataRequired()])

    wifi_strength_rating = SelectField(label="Wifi Strength Rating", choices=[
        ('✘', '✘'),
        ('💪', '💪'),
        ('💪💪', '💪💪'),
        ('💪💪💪', '💪💪💪'),
        ('💪💪💪💪', '💪💪💪💪'),
        ('💪💪💪💪💪', '💪💪💪💪💪')
    ], validators=[DataRequired()])

    power_socket_availability = SelectField(label="Power Socket Availability", choices=[
        ('✘', '✘'),
        ('🔌', '🔌'),
        ('🔌🔌', '🔌🔌'),
        ('🔌🔌🔌', '🔌🔌🔌'),
        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'),
        ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')
    ], validators=[DataRequired()])

    submit = SubmitField(label="Submit")

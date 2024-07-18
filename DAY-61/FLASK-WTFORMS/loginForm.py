from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError


def check_password_length(form, field):
    if len(field.data) < 5:
        raise ValidationError("Password must be greater than 5 characters")


class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="password", validators=[DataRequired(), check_password_length])
    login = SubmitField(label="login")

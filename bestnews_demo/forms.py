from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, validators
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from .model import User


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        [validators.Length(min=4, max=25)],
        render_kw={"class": "form-control"},
    )
    
    password = PasswordField(
        "Password", [validators.DataRequired()], render_kw={"class": "form-control"}
    )
    submit = SubmitField("Send", render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        [validators.Length(min=4, max=25)],
        render_kw={"class": "form-control"},
    )
    email = StringField(
        "Email Address",
        [validators.Length(min=6, max=35), Email()],
        render_kw={"class": "form-control"},
    )
    password = PasswordField(
        "Password", [validators.DataRequired()], render_kw={"class": "form-control"}
    )
    password2 = PasswordField('Repeate Password', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField("Send", render_kw={"class": "btn btn-primary"})
    def validate_username(self, username):
        users_count = User.query.filter_by(username=username.data).first()
        if users_count:
            raise ValidationError('The user with this name is already registered.')

    def validate_email(self, email):
        users_count = User.query.filter_by(email=email.data).first()
        if users_count:
            raise ValidationError(
                'The user with this email is already registered.'
            )

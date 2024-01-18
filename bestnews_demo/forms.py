from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)], render_kw={"class": "form-control"})
    email = StringField('Email Address', [validators.Length(min=6, max=35), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Password', [
        validators.DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Send', render_kw={"class":"btn btn-primary"})




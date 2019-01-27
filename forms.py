from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators


class NewUserForm(FlaskForm):
    username = StringField('Username', [
        validators.Length(max=40, min=2)
    ])
    accept_coc = BooleanField('I accept the CoC', [
        validators.InputRequired()
    ])
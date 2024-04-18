from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectField, MultipleFileField, DateField, PasswordField)
from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired

class RegisterForm(FlaskForm):
    email = StringField("Email",  validators=[DataRequired(), Email()])
    name = StringField('Display Name', validators=[InputRequired(), Length(max=100)])
    password = PasswordField('Enter Password', [InputRequired(), Length(min=10), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField("Confirm password", validators=[InputRequired()])
    agree = BooleanField("Agree", false_values=None, validators=[InputRequired()])

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(),Length(max=100), Email(message='Please enter a valid ')])
    password = PasswordField('Enter Password', [InputRequired(), Length(min=10), EqualTo('confirm', message='Passwords must match')])

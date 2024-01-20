from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectField, MultipleFileField, DateField)
from wtforms.validators import InputRequired, Length, Email


class RegisterForm(FlaskForm):
    firstName = StringField('First Name', validators=[InputRequired(),Length(max=100)])
    lastName = StringField('Last Name', validators=[InputRequired(),Length(max=100)])
    email = StringField('Email', validators=[InputRequired(),Length(max=100), Email()])

class ReportViolations(FlaskForm):
    reportID = IntegerField('Price', validators=[InputRequired()])



from flask_wtf import FlaskForm
from wtforms import (SelectField)
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import InputRequired, Length, Email




class AddTable(FlaskForm):
    tableType = SelectField('Table Data',
                       choices=['','actor_type','actors','counties', 'orgs', 'states', 'vio_category', 'violations'],
                       validators=[InputRequired()])
    csvFile = FileField('Upload csv file')



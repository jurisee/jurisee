from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectField, MultipleFileField, DateField)
from wtforms.validators import InputRequired, Length, Email


class IntakeForm(FlaskForm):
    submitterId = IntegerField('Price', validators=[InputRequired()])
    firstName = StringField('First Name', validators=[InputRequired(),Length(max=100)])
    lastName = StringField('Last Name', validators=[InputRequired(),Length(max=100)])
    email = StringField('Email (so we can contact you)', validators=[InputRequired(),Length(max=100), Email()])
    phoneNum = StringField('Phone Number (if you wish to provide)', validators=[InputRequired(),Length(max=100)])
    skills = TextAreaField("Please identify any skills that you wish to share that might be valuable to Juri See's mission",
                                validators=[InputRequired(),
                                            Length(max=2000)])
    caseNum = StringField('Case Number', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    stillActive = BooleanField("Is your case still active?",false_values=None)
    states = SelectField('State',
                       choices=[],
                       validators=[InputRequired()])
    counties = SelectField('County',
                       choices=[],
                       validators=[InputRequired()])
    court = SelectField('Court',
                       choices=['','Appellate', 'Appellate Terms' 'Civil', 'Court of Appeals', 'County','Criminal','Family','Supreme'],
                       validators=[InputRequired()])
    caseNum = StringField('Case Number', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField("Please provide a short summary of your case and how it fits Juri See's mission",
                                validators=[InputRequired(),
                                            Length(max=2000)])
    dateLastAction = DateField('What is the date of the last action (motion filed, court appearance, etc.)?', format='%Y-%m-%d')
    dateLastOrder = DateField('What is the date of the last written decision by the court?', format='%Y-%m-%d')

class ReportViolations(FlaskForm):
    reportID = IntegerField('Price', validators=[InputRequired()])



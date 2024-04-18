from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectField, MultipleFileField, DateField, HiddenField)
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

class CourtWatchForm(FlaskForm):
    judgeId = HiddenField()
    afcId = HiddenField()
    evalId = HiddenField()
    opLawyerId = HiddenField()
    effectedLawyerId = HiddenField()
    summary = TextAreaField('Please describe any relevant events (approx 500 words limit)',validators=[InputRequired(), Length(max=2500)])
    caseNum = StringField('Case Number', validators=[InputRequired(),
                                             Length(min=5, max=100)])
    approxDate = DateField('Court Date', format='%Y-%m-%d')
    states = SelectField('State',
                       choices=[],
                       validators=[InputRequired()])
    county = SelectField('County',
                       choices=[], validators=[InputRequired()])
    court = SelectField('Court',
                       choices=['','Appellate', 'Appellate Terms', 'Civil', 'Court of Appeals', 'County','Criminal','Family','Supreme'], validators=[InputRequired()])
    gender = SelectField("Effected Person's Gender",
                       choices=['','Man', 'Woman','Non-Binary', 'Prefer not to say'], validators=[InputRequired()])
    race = SelectField("Effected Person's Race",
            choices=['','Asian', 'Black', 'Native American or Alaskan Native', 'Native Hawaiian or other Pacific Islander', 'White', 'Mixed', 'Prefer not to say'], validators=[InputRequired()])
    ethnicity = SelectField("Effected Person's Ethnicity",
            choices=['','Hispanic or Latino', 'Other','Prefer not to say'], validators=[InputRequired()])
    highIncome = BooleanField('Is the other party high income (exceeding $450,000 in annual income etc?)', false_values=None)
    highWealth = BooleanField("Is the other party high wealth (over $5-10 million in self or family assets)", false_values=None)
    eighteenB = BooleanField("Is the effected person assigned an 18b lawyer?", false_values=None)
    proSe = BooleanField("Is the effected person Pro Se?", false_values=None)











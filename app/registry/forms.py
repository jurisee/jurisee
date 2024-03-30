from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField,RadioField, SelectField, MultipleFileField, SelectMultipleField, widgets, HiddenField
from wtforms.validators import InputRequired, URL, Length, Email, DataRequired
from wtforms.widgets import EmailInput



class ReportForm(FlaskForm):
    submitterId = HiddenField()
    reportType = HiddenField()
    caseNum = StringField('Case Number', validators=[InputRequired(),
                                             Length(min=5, max=100)])
    badActorId = HiddenField()
    badActorType = SelectField('Offender Role',
                       choices=[],
                       validators=[InputRequired()])
    states = SelectField('State',
                       choices=[],
                       validators=[InputRequired()])
    county = SelectField('County',
                       choices=[], validators=[InputRequired()])
    court = SelectField('Court',
                       choices=['','Appellate', 'Appellate Terms' 'Civil', 'Court of Appeals', 'County','Criminal','Family','Supreme'], validators=[InputRequired()])
    gender = SelectField('Gender',
                       choices=['','Man', 'Woman','Non-Binary', 'Prefer not to say'], validators=[InputRequired()])
    race = SelectField('Race',
            choices=['','Asian', 'Black', 'Native American or Alaskan Native', 'Native Hawaiian or other Pacific Islander', 'White', 'Mixed', 'Prefer not to say'], validators=[InputRequired()])
    ethnicity = SelectField('Ethnicity',
            choices=['','Hispanic or Latino', 'Other','Prefer not to say'], validators=[InputRequired()])
    highIncome = BooleanField('Is the other party high income (exceeding $450,000 in annual income etc?)', false_values=None)
    highWealth = BooleanField("Is the other party high wealth (over $5-10 million in self or family assets)", false_values=None)
    eighteenB = BooleanField("Are you (or person effected) assigned an 18b lawyer?", false_values=None)
    proSe = BooleanField("Are you (or person effected) Pro Se?", false_values=None)

class AddViolationsForm(FlaskForm):
    submitterId = IntegerField('Price', validators=[InputRequired()])
    reportType = SelectField('Report Type',
                       choices=['','Report', 'Grievance', 'Courtwatch'],
                       validators=[InputRequired()])
    violations = SelectMultipleField('Select all that apply',
                       choices=[], option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False))
    title = StringField('Title')
    summary = TextAreaField('Please describe related events (approx 500 words limit)',validators=[InputRequired(), Length(max=2500)])
    hideSummary = BooleanField('Do not publish the description',false_values=None)
    evidence = MultipleFileField('Add Evidence')

class AddViolationForm(FlaskForm):
    violation  = StringField('Violation', validators=[InputRequired(),
                                             Length(max=150)])
    violationTypeId  = StringField('Violation Type', validators=[InputRequired(),
                                             Length(max=100)])


class AddActorForm(FlaskForm):
    fName  = StringField('First Name', validators=[InputRequired(),
                                             Length(max=100)])
    lName  = StringField('Last Name', validators=[InputRequired(),
                                             Length(max=100)])
    FUID  = StringField('FUID', validators=[InputRequired(),
                                             Length(max=100)])
    licenseNum  = StringField('License Number', validators=[InputRequired(),
                                             Length(max=100)])
    email = StringField('Email', validators=[InputRequired(), Email()])


class AddOrgForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(),
                                             Length(max=100)])
    address1 = StringField('Address Line 1', validators=[InputRequired(),
                                             Length(max=100)])
    address2 = StringField('Address Line 2', validators=[Length(max=100)])
    city = StringField('City', validators=[InputRequired(),
                                             Length(max=100)])
    states = SelectField('State',
                       choices=[],
                       validators=[InputRequired()])
    zipcode = IntegerField('Zip Code', validators=[InputRequired(Length(max=50))])
    phone = StringField('Phone', validators=[InputRequired(),
                                    Length(max=50)])
    orgEmail = StringField('Organizational Email', validators=[InputRequired(), Email()])
    website = StringField('Website', validators=[InputRequired(Length(max=50))])
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, BooleanField,RadioField, SelectField, MultipleFileField, SelectMultipleField, widgets, HiddenField
from wtforms.validators import InputRequired, URL, Length, Email, DataRequired
from wtforms.widgets import EmailInput



class ReportForm(FlaskForm):
    submitterId = HiddenField()
    reportType = HiddenField()
    title = StringField('Title', validators=[InputRequired(),Length(min=10, max=100)])
    summary = TextAreaField('Summary',validators=[InputRequired(), Length(max=2000)])
    hideSummary = BooleanField(false_values=None)
    caseNum = StringField('Case Number', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    badActorId = HiddenField()
    badActorType = SelectField('Offender Role',
                       choices=[],
                       validators=[InputRequired()])
    states = SelectField('State',
                       choices=[],
                       validators=[InputRequired()])
    county = SelectField('County',
                       choices=['','Appellate', 'Appellate Terms' 'Civil', 'Court of Appeals', 'County','Criminal','Family','Supreme'])
    court = SelectField('Court',
                       choices=['','Appellate', 'Appellate Terms' 'Civil', 'Court of Appeals', 'County','Criminal','Family','Supreme'])
    evidence = MultipleFileField('Add Evidence')

class AddViolationsForm(FlaskForm):
    submitterId = IntegerField('Price', validators=[InputRequired()])
    caseNum = StringField('Case Number', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    reportType = SelectField('Report Type',
                       choices=['','Report', 'Grievance', 'Courtwatch'],
                       validators=[InputRequired()])
    violations = SelectMultipleField('Select all that apply',
                       choices=[], option_widget=widgets.CheckboxInput(), widget=widgets.ListWidget(prefix_label=False))
    summary = TextAreaField('Please describe related events',validators=[InputRequired(), Length(max=2000)])
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
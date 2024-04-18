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

class CourtWatchForm(FlaskForm):
    judgeName = StringField('Judge Name', validators=[InputRequired(),Length(max=100)])
    afcName = StringField('Attorney for Child', validators=[InputRequired(),Length(max=100)])
    ocName = StringField('Oposing Counsel', validators=[InputRequired(),Length(max=100)])
    slcName = StringField('Supported Litigant Counsel', validators=[InputRequired(),Length(max=100)])
    description = StringField('Description', validators=[InputRequired(), Length(max=2000)])
    noNotice = BooleanField("Ex-parte orders signed by Judge without notice to affected party",false_values=None)
    noEvidence = BooleanField("Ex-parte removal of rights without evidence", false_values=None)
    noHarm = BooleanField("Ex-parte removal of rights without exigent circumstances or imminent harm", false_values=None)
    noImmediateTrial = BooleanField("Ex-parte removal of rights without immediate trial/evidentiary hearing", false_values=None)
    renewedNoTrial = BooleanField("Ex-parte order automatically renewed without trial or evidence presented", false_values=None)
    offRecord = BooleanField("Off-record, lawyer only sessions held in which significant custodial decisions are made", false_values=None)
    exParteComm = BooleanField("Judge engaged in ex parte communications", false_values=None)
    afcExParte = BooleanField("AFC engaged in ex parte communications", false_values=None)
    expertEngaged = BooleanField("Court appointed “expert” engaged in ex parte communications", false_values=None)

    knowsCase = BooleanField("Judge demonstrates inappropriate knowledge of the case before them", false_values=None)
    disregard = BooleanField("Judge demonstrates lack of knowledge or disregard of relevant law", false_values=None)
    disrespect = BooleanField("Judge speaks disrespectfully to litigant", false_values=None)
    noSpeak = BooleanField("Judge does not allow a litigant to speak or doesn’t allow their position on the record", false_values=None)
    unequalTime = BooleanField("Judge does not provide equal time between litigants", false_values=None)
    oRMatters = BooleanField("Judge goes off-record for matters of substance / consequence", false_values=None)
    judgeFavor = BooleanField("Judge demonstrates extreme favor for one litigant over the other", false_values=None)
    judgeBias = BooleanField("Judge demonstrates (including but not limited to) bias or prejudice (based upon "
                             "age, race, creed, color, sex, sexual orientation, gender identity, gender expression, "
                             "religion, national origin, disability, marital status or socioeconomic status)",
                             false_values=None)
    courtBias = BooleanField("Judge allows legal professionals and court appointees to demonstrate bias or prejudice "
                              "(based upon age, race, creed, color, sex, sexual orientation, gender identity, "
                              "gender expression, religion, national origin, disability, marital status or "
                              "socioeconomic status)", false_values=None)
    access = BooleanField("Judge attempts to get litigant to settle with restricted access to your children", false_values=None)
    biasTrial = BooleanField("Judge states litigant can have trial but they have already decided negatively against them", false_values=None)
    contempt = BooleanField("Judge threatens contempt for issues that are known to not be your fault", false_values=None)
    restrainingOrder = BooleanField("Judge threatens restraining orders for raising objections, not settling, etc.")
    accessChildren = BooleanField("AFC threatens your access to your children if you report issues", false_values=None)
    afcConcerns = BooleanField("AFC states your objections or concerns for children are reason to speak negatively to the court about you", false_values=None)
    evaluator = BooleanField("Evaluator threatens your access to you children", false_values=None)
    evaluatorConcerns = BooleanField("Evaluator states that your objections are cause for them to find negatively against you", false_values=None)
    afcThreats = BooleanField("AFC threatens contempt for fees you cannot pay", false_values=None)
    judgeThreats = BooleanField("Judge threatens contempt for fees you cannot pay", false_values=None)
    evaluatorThreats = BooleanField("Evaluator threatens bad decision for fee", false_values=None)

    docketNum = BooleanField("Ex-parte order is filed without proper assignment of Docket #s", false_values=None)
    improperCase = BooleanField("Court proceedings are begun by an improperly “reinstated” case instead of proper initiation", false_values=None)
    noExperation = BooleanField("No expirations is given on temporary orders", false_values=None)
    notInformed = BooleanField("Litigant not informed of court appearances", false_values=None)
    noPurpose = BooleanField("Litigant is not notified of purpose of court appearance", false_values=None)
    lockedOut = BooleanField("Litigant locked out of court rooms during appearance", false_values=None)
    noRight = BooleanField("Litigant denied right to attend off-record session when requested", false_values=None)
    obstructed = BooleanField("Litigant denied or obstructed from access to the record", false_values=None)
    redAltered = BooleanField("Court records are altered without citation of cause", false_values=None)
    transcripts = BooleanField("Court transcripts are altered without citation of cause", false_values=None)
    apperance = BooleanField("Court appearance is not recorded on the docket", false_values=None)
    inaccurate = BooleanField("Court appearance is intentionally or grossly inaccurate on the docket", false_values=None)
    changesMade = BooleanField("Custodial changes made with OSC or TOP without petition filed in 10 days", false_values=None)
    fClaims = BooleanField("[FRIVIKOUS CLAIMS]", false_values=None)
    threatened = BooleanField("Judge asks Bailiff to threaten litigant", false_values=None)
    trialWO = BooleanField("Judge holds trial without litigant there", false_values=None)









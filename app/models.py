from app.extensions import db
from app.extensions import ma
from datetime import datetime


#hold table for news articles
class Article(db.Model):
    id:int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title:str = db.Column(db.String(150))
    author:str = db.Column(db.String(150))
    content:str = db.Column(db.Text)
    date_created:str = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Article "{self.id}">'

#start registry tables
class Actors(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fName = db.Column(db.String(150))
    lName = db.Column(db.String(150))
    FUID = db.Column(db.String(50))
    licenseNum = db.Column(db.String(50))
    email = db.Column(db.String(50))
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    reports = db.relationship('Report', backref='actor')
    orgs = db.relationship('ActorOrgs', backref='actor')
    
    def __repr__(self):
        return '<Actors %s>' % self.id

class ActorsSchema(ma.Schema):
    class Meta:
        fields = ("id", "fName", "lName", "FUID", "licenseNum")
        model = Actors

actor_schema = ActorsSchema()
actors_schema = ActorsSchema(many=True)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    submitterId = db.Column(db.Integer)
    reportType = db.Column(db.String(100), nullable=False)
    reportCategory = db.Column(db.Integer, db.ForeignKey('vio_category.id'))
    title = db.Column(db.String(100))
    summary = db.Column(db.Text)
    hideSummary = db.Column(db.Boolean)
    caseNum = db.Column(db.String(100))
    badActorId = db.Column(db.Integer, db.ForeignKey('actors.id'))
    actorType = db.Column(db.Integer, db.ForeignKey('actor_type.id'))
    states = db.Column(db.Integer, db.ForeignKey('states.id'))
    county = db.Column(db.Integer, db.ForeignKey('counties.id'))
    court = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    sent = db.Column(db.Boolean, default=False)
    published = db.Column(db.Boolean, default=False)
    highIncome = db.Column(db.Boolean, default=False)
    highWealth = db.Column(db.Boolean, default=False)
    eighteenB = db.Column(db.Boolean, default=False)
    proSe = db.Column(db.Boolean, default=False)
    violations = db.relationship('ReportViolations', backref='report')
    
    def __repr__(self):
        return f'<Report "{self.id}">'

class ActorType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actorType = db.Column(db.String(100), nullable=False)
    reports = db.relationship('Report', backref='role')

    def __repr__(self):
        return f'<ActorType "{self.id}">'

class ReportViolations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reportId = db.Column(db.Integer, db.ForeignKey('report.id'))
    violationId = db.Column(db.Integer, db.ForeignKey('violations.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ReportViolations "{self.id}">'

class ViolationsSum(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reportId = db.Column(db.Integer, nullable=False)
    vioCategoryId = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ReportVSum "{self.id}">'

class Violations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    violation = db.Column(db.String(100), nullable=False)
    violationTypeId = db.Column(db.Integer)
    reportViolations = db.relationship('ReportViolations', backref='violation')

    def __repr__(self):
        return f'<Violations "{self.id}">'

class VioCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(100), nullable=False)
    reports = db.relationship('Report', backref='category')

    def __repr__(self):
        return f'<VioCategory "{self.id}">'

class Orgs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    address1 = db.Column(db.String(150))
    address2 = db.Column(db.String(150))
    city = db.Column(db.String(150))
    state = db.Column(db.String(4))
    zipcode = db.Column(db.Integer)
    phone = db.Column(db.String(50))
    orgEmail = db.Column(db.String(50))
    website = db.Column(db.String(150))
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    actorOrgs = db.relationship('ActorOrgs', backref='orgs')

    def __repr__(self):
        return f'<Orgs "{self.id}">'


class ActorOrgs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actorId = db.Column(db.Integer, db.ForeignKey('actors.id'))
    orgId = db.Column(db.Integer, db.ForeignKey('orgs.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<ActorOrgs "{self.id}">'

#start for dynamic form choices
class States(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    abbrv = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean())
    reports = db.relationship('Report', backref='state')

    def __repr__(self):
        return f'<States "{self.id}">'
     
class Counties(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    county = db.Column(db.String(100), nullable=False)
    state = db.Column(db.Integer,nullable=False)
    reports = db.relationship('Report', backref='counties')

    def __repr__(self):
        return f'<Counties "{self.id}">'



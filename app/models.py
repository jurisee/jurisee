from app.extensions import db
from app.extensions import ma
from datetime import datetime
from sqlalchemy.orm import relationship

#hold table for news articles
class Article(db.Model):
    id:int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title:str = db.Column(db.String(150))
    author:str = db.Column(db.String(150))
    content:str = db.Column(db.Text)
    date_created:str = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Article "{self.title}">'

#start registry tables
class Actors(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fName = db.Column(db.String(150))
    lName = db.Column(db.String(150))
    FUID = db.Column(db.String(50))
    licenseNum = db.Column(db.String(50))
    email = db.Column(db.String(50))
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Actors %s>' % self.id

class ActorsSchema(ma.Schema):
    class Meta:
        fields = ("id", "fName", "lName", "FUID", "licenseNum")
        model = Actors

actor_schema = ActorsSchema()
actors_schema = ActorsSchema(many=True)

class ActorType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actorType = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<ActorType "{self.title}">'

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    submitterId = db.Column(db.Integer)
    reportType = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.Text)
    hideSummary = db.Column(db.Boolean)
    caseNum = db.Column(db.String(100))
    badActorId = db.Column(db.Integer)
    badActorType = db.Column(db.Integer, db.ForeignKey("db.ActorType.id"))
    states = db.Column(db.String(100))
    county = db.Column(db.String(100))
    court = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    sent = db.Column(db.Boolean, default=False)
    published = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Report "{self.title}">'

class ReportViolations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reportId = db.Column(db.Integer, nullable=False)
    violationId = db.Column(db.Integer, nullable=False)
    vioCatId = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ReportViolations "{self.title}">'

class ViolationsSum(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reportId = db.Column(db.Integer, nullable=False)
    vioCategoryId = db.Column(db.Integer, nullable=False)
    summary = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ReportVSum "{self.title}">'

class Violations(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    violation = db.Column(db.String(100), nullable=False)
    violationTypeId = db.Column(db.Integer)

    def __repr__(self):
        return f'<Violations "{self.title}">'

class VioCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(100), nullable=False)

   # def __repr__(self):
   #     return f'<VioCategory "{self.title}">'

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

    def __repr__(self):
        return f'<Orgs "{self.title}">'


#start for dynamic form choices
class States(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    abbrv = db.Column(db.String(10), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean())

    def __repr__(self):
        return f'<States "{self.title}">'
     
class Counties(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    county = db.Column(db.String(100), nullable=False)
    state = db.Column(db.Integer,nullable=False) 

    def __repr__(self):
        return f'<Counties "{self.title}">'



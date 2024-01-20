from app.extensions import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    author = db.Column(db.String(150))
    content = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Article "{self.title}">'


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submitterId = db.Column(db.Integer)
    reportType = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.Text)
    hideSummary = db.Column(db.Boolean)
    caseNum = db.Column(db.String(100))
    badActorId = db.Column(db.Integer)
    badActorType = db.Column(db.String(100))
    states = db.Column(db.String(100))
    county = db.Column(db.String(100))
    court = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Report "{self.title}">'
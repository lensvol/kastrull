from app import app
from app import db

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, unique=True)
    color = db.Column(db.String(32))
    created_at = db.Column(db.DateTime)
    activities = db.relationship('Activity')

class Resource(db.Model):
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True)
    type = db.Column(db.String(255), index=True)
    status = db.Column(db.String(255), index=True)
    created_at = db.Column(db.DateTime)

class Activity(db.Model):
    __tablename__ = 'activities'
    id = db.Column(db.Integer, primary_key=True)
    date_start = db.Column(db.Date, index=True)
    date_end = db.Column(db.Date, index=True)
    created_at = db.Column(db.DateTime)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))

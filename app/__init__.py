import os
from flask import Flask
from flask import render_template
from flask import flash
from flask import request
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import json

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.before_first_request
def create_db():
    db.create_all()

from app import forms
from .models import Resource

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resources', methods=['GET', 'POST'])
def add_resource():
    form = forms.AddResourceForm(request.form)
    if request.method == 'POST':
        if form.validate():
            resource = Resource(name = form.name.data, type = form.type.data,
                                status = form.status.data, created_at = datetime.utcnow())
            db.session.add(resource)
            db.session.commit()
            flash('Resource added!')
    else:
        resources = Resource.query.all()
    return render_template('add_resource.html', form=form)

@app.route('/activities', methods=['GET', 'POST'])
def add_activity():
    return

@app.route('/projects', methods=['GET', 'POST'])
def add_project():
    return

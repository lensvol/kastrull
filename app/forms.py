from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import DataRequired, Length

class AddResourceForm(Form):
    name = TextField('Name', [Length(min=3, max=255)])
    type = TextField('Type/Job title', [Length(max=255)])
    status = TextField('Status/Competency level', [Length(max=255)])

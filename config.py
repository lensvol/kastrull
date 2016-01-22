import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SECRET_KEY = 'SECRET_KEY'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sm.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

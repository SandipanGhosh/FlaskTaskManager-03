# project/_config.py

import os

# grab the folder of this script
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
TESTING = False
CSRF_ENABLED = True
SECRET_KEY = 'myprecious'

# define full db path
DATABASE_PATH = os.path.join(basedir, DATABASE)

# db url
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
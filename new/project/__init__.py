## set up of our db file

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_mail import Mail,Message


login_manager=LoginManager()

app=Flask(__name__)
##app.config.update(
##    DEBUG=True,
##    #mail settings
##    MAIL_SERVER='smtp.google.com',
##    MAIL_PORT=587,
##    MAIL_USE_SSL=True,
##    MAIL_USERNAME='fypmailing@gmail.com',
##    MAIL_PASSWORD='project2019'
##    )

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'fypmailing@gmail.com'
app.config['MAIL_PASSWORD'] = 'project2019'
app.config['SECRET_KEY'] = 'mysecretkey'

mail = Mail(app)



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(APP_ROOT,'uploads')
EXCEL_FOLDER = os.path.join(APP_ROOT,'exports')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['EXCEL_FOLDER'] = EXCEL_FOLDER



CORS(app)

################# SQL DATABASE SECTION ##########

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)

Migrate(app,db)

login_manager.init_app(app)

login_manager.login_view ='login'

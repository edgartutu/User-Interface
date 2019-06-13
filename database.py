from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'medicine.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

class Medicine(db.Model):
    id = db.Column('Medicine_id',db.Integer,primary_key = True)
    Name = db.Column(db.String(100))
    Serial_number = db.Column(db.String(50))
    Expiry_date = db.Column(db.String(20))
    Manufacture_date = db.Column(db.String(20))

    def __init__(self,Name,Serial_number,Expiry_date,Manufacture_date):
        self.Name = Name
        self.Serial_number = Serial_number
        self.Expiry_date = Expiry_date
        self.Manufacture_date = Manufacture_date

    def json(self):
        return{'Name':self.Name,'Serial_number':self.Serial_number,'Expiry_date':self.Expiry_date,'Manufacture_date':self.Manufacture_date}
        

class Phone(db.Model):
    id = db.Column('Phone_id',db.Integer,primary_key = True)
    Phone_number = db.Column(db.String(10))
    Date = db.Column(db.String(20))
    Serial_number = db.Column(db.String(100))
    Response = db.Column(db.String(100))

    def __init__(self,Phone_number,Date,Serial_number,Response):
        self.Phone_number = Phone_number
        self.Date = Date
        self.Serial_number = Serial_number
        self.Response = Response

db.create_all()


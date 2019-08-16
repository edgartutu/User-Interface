# set up  db in __init__.py under my projects folder

from project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
      
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Admin(db.Model, UserMixin):
    email = db.Column(db.String(64), primary_key=True, unique=True, index=True)
    publicID = db.Column(db.String(100))
    password = db.Column(db.String(128))


    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):     
        return check_password_hash(self.password_hash,password)


class Product(db.Model):
    id = db.Column('Medicine_id',db.Integer,primary_key = True)
    Name = db.Column(db.String(100))
    Serial_number = db.Column(db.String(50))
    Expiry_date = db.Column(db.String(20))
    Manufacture_date = db.Column(db.String(20))
    status =db.Column(db.String(20))

    def __init__(self,Name,Serial_number,Expiry_date,Manufacture_date, status):
        self.Name = Name
        self.Serial_number = Serial_number
        self.Expiry_date = Expiry_date
        self.Manufacture_date = Manufacture_date
        self.status = status

    def json(self):
        return{'Name':self.Name,'Serial_number':self.Serial_number,'Expiry_date':self.Expiry_date,'Manufacture_date':self.Manufacture_date,'status':self.status}
        

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

    def json(self):
        return{'Phone_number':self.Phone_number,'Serial_number':self.Serial_number,'Date':self.Date,'Response':self.Response}

db.create_all()

from project import app, db
from project.models import Admin,Product,Phone
from flask_restful import Resource, Api
from flask import flash, redirect, render_template, request, url_for,make_response
from flask_login import login_user,login_required, logout_user
from .forms import LoginForm,ProposalForm,ProjectForm,Proposal_comment_Form
import functools
from project import db, login_manager,mail
from werkzeug.utils import secure_filename
import os
import datetime
from flask_login import login_user,login_required,logout_user
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from functools import wraps
import json
import random
from flask import send_file, send_from_directory, safe_join, abort
import flask_excel as excel
import pyexcel
import uuid
import time
from flask_mail import Message
from twilio import twiml


api = Api(app)

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
    
            return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
        try:
            
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = Admin.query.filter_by(publicID=data['public_id']).first()
            
        except:
            return make_response('Invalid Token',401,{'www-Authenticate':'Invalid Token"'})
        return f(current_user,*args,**kwargs)
    return decorated
    
class Login(Resource):
    def post(self):
        #auth = request.get_json()
        data = request.get_json()
        '''checking if authorization information is complete'''
        if not data or not data['username'] or not data['password']:
            return make_response('Could not verify1',401,{'www-Authenticate':'Basic realm-"login required!"'})
        admin = Admin.query.filter_by(email=data['username']).first()
        
        if not admin:
            return make_response('Could not verify2',401,{'www-Authenticate':'Basic realm-"login required!"'})       

        if admin.password == data['password']:
            token = jwt.encode({'public_id':admin.publicID,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60)},app.config['SECRET_KEY'])
            return jsonify({'token':token.decode('UTF-8'),'username':admin.publicID})
        return make_response('Could not verify3',401,{'www-Authenticate':'Basic realm-"login required!"'})

class Logout(Resource):
#    @token_required
##    @staticmethod
    @login_required
    def post(self,current_user):
        logout_user()
        flash('You were logged out. ')


class ResetPassword(Resource):
    def post(self):
        old_pass, new_pass = request.json.get('old_pass'), request.json.get('new_pass')
        user = Admin.query.filter_by(email=email).first()
        if user.password != old_pass:
            flash ('status: old password does not match.')
        user.password = new_pass
        db.session.commit()
        flash('status: password changed.')



         
class PostProduct(Resource):
#    @token_required
    def post(current_user):
       data = request.get_json()    
       Manufacture_date=data['Manufacture_date']
       Expiry_date=data['Expiry_date']
       Exp=datetime.datetime.strptime(Expiry_date, '%Y-%m-%d').strftime('%Y/%m/%d')
       Serial_number=data['Serial_number']
       Name=data['Name']
       date_now = datetime.datetime.today()
       date_exp = datetime.datetime.strptime(Expiry_date, "%Y-%m-%d")
       if date_now<=date_exp:
           status='Active'   
           pro = Product(Name=Name,Serial_number=Serial_number,Expiry_date=Exp,Manufacture_date=Manufacture_date,status=status)
           db.session.add(pro)
           db.session.commit()
           return pro.json()
       else:
           status='Inactive'
           pro = Product(Name=Name,Serial_number=Serial_number,Expiry_date=Exp,Manufacture_date=Manufacture_date,status=status)
           db.session.add(pro)
           db.session.commit()
           return pro.json()
            
         
class GetProduct(Resource):
#    @token_required
    def get(current_user):
        pro=Product.query.all()
        return [x.json() for x in pro]

class GetPhone(Resource):
#    @token_required
    def get(current_user):
        phone=Phone.query.all()
        return [x.json() for x in phone]

class Getby(Resource):
#    @token_required
    def get(current_user):
        data=request.get_json()
        Name=data['Name']
        pro=Product.query.filter_by(Name=Name).first()
        return [x.json() for x in pro]

class Request(Resource):
#    @token_required
    def get(current_user):
        data=request.get_json()
        number = request.data['Phone_number']
        message_body = request.data['Serial_number']
        p=Product.query.filter_by(message_body=message_body).first()
        product= p.Name
        make=p.Manufacture_date
        made=p.Expiry_date
        date_now = datetime.datetime.today()
        date_exp = datetime.strptime(made, "%d %B %Y")
        try:
            if date_now>=date_exp:
                resp = twiml.Response()
                resp.message('Hello {},: {} of serial{} was manufactured on {} and expired on {} therefore this product is expired'.format(number,product, message_body, make,made))
                return str(resp)
            else:
                resp = twiml.Response()
                resp.message('Hello {}, you product will expire on {} therefore your safe '.format(number, made))
                return str(resp)
        except Exception:
            return {"Error":"No requesting number"}
            
            
            
        
        
        
        
      

        
        
 

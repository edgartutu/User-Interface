from project import app, db
from project.models import Product,Phone
from flask_restful import Resource, Api
from flask import flash, redirect, render_template, request, url_for,make_response
from flask_login import login_user,login_required, logout_user
from .forms import LoginForm,RegisterForm,Proposal_submittion_Form
from project import db, login_manager,mail
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash,check_password_hash
import os
import functools
from flask_login import login_user,login_required,logout_user
import json
import logging
from flask import jsonify
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
import jwt
from functools import wraps
import datetime
from flask_mail import Message
from twilio import twiml
from twilio.twiml.messaging_response import Message, MessagingResponse

api = Api(app)
        
                
class SendSerial(Resource):
    #@token_required
    def post(current_user): 
        data=request.get_json()
        Phone_number = data['Phone_number']
        message_body = data['Serial_number']
        Response="None"
        date_=datetime.datetime.today()
        post_= Phone(Phone_number=Phone_number,Serial_number=message_body,Date=date_,Response=Response)
        db.session.add(post_)
        db.session.commit()
        p=Product.query.filter_by(Serial_number=message_body).first()
        product= p.Name
        make=p.Manufacture_date
        made=p.Expiry_date
        date_now = datetime.datetime.today()
        date_exp = datetime.datetime.strptime(made, "%d/%m/%Y")
        try:
            if date_now>=date_exp:
                resp = MessagingResponse()
                resp.message('Hello {}, {} of serial {} was manufactured on {} and expired on {} therefore this product is expired'.format(Phone_number,product, message_body, make,made))
                post_.Response='Hello {}, {} of serial {} was manufactured on {} and expired on {} therefore this product is expired'.format(Phone_number,product, message_body, make,made)
                db.session.commit()
                return str(resp)
            
            else:
                resp = MessagingResponse()
                resp.message('Hello {}, your product ({}) will expire on {} therefore your safe '.format(Phone_number,product,made))
                post_.Response= 'Hello {}, your product ({}) will expire on {} therefore your safe '.format(Phone_number,product,made)
                db.session.commit()
                return str(resp)
        except Exception:
            return {"Error":"No requesting number"}




            
            
                
                
        

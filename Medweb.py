from flask import Flask,render_template
from database import app,db
from database import Medicine,Phone
import datetime

from flask_restful import Resource,Api

api=Api(app)

class Med_call(Resource):
        
##    @app.route("/addmedicine/<string:Name>/<string:Serial_number>/<string:Expiry_date>/<string:Manufacture_date>",methods=['GET','POST'])
    def post(self,Name,Serial_number,Expiry_date,Manufacture_date):
##        if request.method == 'POST':
        x = Medicine(Name=Name,Serial_number=Serial_number,Expiry_date=Expiry_date,Manufacture_date=Manufacture_date)
        db.session.add(x)
        db.session.commit()
        return x.json() 
     
##    @app.route("/viewmed")
    def get(self,Name,Serial_number,Expiry_date,Manufacture_date):
        x = Medicine.query.filter_by(Name=Name).first()
        if x:
            return [x.json()]
        else:
            return{'medicine':'doesnt exist'},404
##    @app.route("/viewmed2")
    def del_med(self,Name,Serial_number,Expiry_date,Manufacture_date):
        x = Medicine.query.filter_by(Name=Name).first()
        db.session.delete(x)
        db.session.commit()
        

##    @app.route("/viewrequest")
    def requestphone(self,Name,Serial_number,Expiry_date,Manufacture_date):
        if service_request.name:
            Medicine.query.filter_by(Name=Name).first()

class ViewAll(Resource):

    def get (self):

        med=Medicine.query.all()

        return [k.json() for k in med]

api.add_resource(Med_call,'/addmedicine/<string:Name>/<int:Serial_number>/<string:Expiry_date>/<string:Manufacture_date>')
api.add_resource(ViewAll,'/medicine')
    

if __name__ == '__main__':
    app.run(debug='True')

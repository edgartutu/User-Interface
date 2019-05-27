from flask import Flask,render_template
from database import app,db
from database import Medicine,Phone
import datetime



@app.route("/")
def home():
    return "Hello"

    
@app.route("/addmedicine")
def addmed():
    x = Medicine('pan','1234567','12/1/2020','12345')
    db.session.add_all([x])
    db.session.commit()
    return 'x' ## i have added this to test my view function. have done away eith the errors in the code so go on and
                    ##add information to the database and then find a way how to represent it on the web.
     
@app.route("/viewmed")
def med():
    Medicine.query.all()
    print(Medicine.query.get(1))
    

@app.route("/viewrequest")
def requestphone():
    Phone.query.all()

    

if __name__ == '__main__':
    app.run(debug='True')

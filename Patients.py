from flask import Flask,request
import json
from flask_sqlalchemy import SQLAlchemy
# from models import db,Patient,Medication,Measurement

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/Patients'
db = SQLAlchemy(app)

class Patient(db.Model):
    Patient_ID = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(50))
    Last_Name = db.Column(db.String(50))
    Dob = db.Column(db.Date)
    def __init__(self, Patient_ID, First_Name, Last_Name, Dob):
        self.Patient_ID = Patient_ID
        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.Dob = Dob
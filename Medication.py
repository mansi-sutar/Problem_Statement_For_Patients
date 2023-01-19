from flask import Flask,request
import json
from flask_sqlalchemy import SQLAlchemy
# from models import db,Patient,Medication,Measurement

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/Patients'
db = SQLAlchemy(app)

class Medication(db.Model):
    Medication_ID = db.Column(db.Integer, primary_key=True)
    Patient_ID = db.Column(db.Integer, db.ForeignKey('patient.Patient_ID'))
    Medication_Name = db.Column(db.String(100))
    Dose = db.Column(db.String(50))
    Frequency = db.Column(db.Integer)
    Intake_Type = db.Column(db.String(100))
    def __init__(self, Medication_ID, Medication_Name,Patient_ID ,Dose, Frequency,Intake_Type):
        self.Medication_ID = Medication_ID
        self.Medication_Name = Medication_Name
        self.Patient_ID = Patient_ID
        self.Dose = Dose
        self.Frequency = Frequency
        self.Intake_Type = Intake_Type

from flask import Flask,request
import json
from flask_sqlalchemy import SQLAlchemy
# from models import db,Patient,Medication,Measurement

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/Patients'
db = SQLAlchemy(app)

class Allergies(db.Model):
    Allergy_ID = db.Column(db.Integer, primary_key=True)
    Patient_ID = db.Column(db.Integer, db.ForeignKey('patient.Patient_ID'))
    Name = db.Column(db.String(150))
    Allergy_type = db.Column(db.String(100))
    Reference_id = db.Column(db.Integer, db.ForeignKey('medication.Medication_ID') or db.ForeignKey('measurement.Measurement_ID'))
    def __init__(self, Allergy_ID, Patient_ID, Name,Allergy_type,Reference_id):
        self.Allergy_ID = Allergy_ID
        self.Patient_ID = Patient_ID
        self.Name = Name
        self.Allergy_type = Allergy_type
        self.Reference_id = Reference_id
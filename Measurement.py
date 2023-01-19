from flask import Flask,request
import json
from flask_sqlalchemy import SQLAlchemy
# from models import db,Patient,Medication,Measurement

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/Patients'
db = SQLAlchemy(app)

class Measurement (db.Model):
    Measurement_ID = db.Column(db.Integer, primary_key=True)
    Patient_ID = db.Column(db.Integer, db.ForeignKey('patient.Patient_ID'))
    Measurement_Name = db.Column(db.String(100))
    Unit = db.Column(db.String)
    Value = db.Column(db.Float)
    def __init__(self, Measurement_ID, Measurement_Name,Patient_ID, Unit, Value):
        self.Measurement_ID = Measurement_ID
        self.Measurement_Name = Measurement_Name
        self.Patient_ID = Patient_ID
        self.Unit = Unit
        self.Value = Value
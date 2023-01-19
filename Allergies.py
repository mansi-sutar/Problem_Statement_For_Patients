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

@app.route('/allergy_details')
def allergy_details():
    allergys = Allergies.query.all()
    output = []
    for allergy in allergys:
        allergy_data ={'Allergy_ID' : allergy.Allergy_ID,
                           'Patient_ID' : allergy.Patient_ID,
                           'Name' : allergy.Name,
                            'Allergy_type' : allergy.Allergy_type,
                            'Reference_id' : allergy.Reference_id }
        output.append(allergy_data)
    return { "Allergy " : output }

@app.route('/add_allergy',methods = ['POST'])
def add_allergy():
    allergy = Allergies( Allergy_ID = request.json['Allergy_ID'],
                         Patient_ID = request.json['Patient_ID'],
                         Name = request.json['Name'],
                         Allergy_type = request.json['Allergy_type'],
                         Reference_id = request.json['Reference_id'])
    db.session.add(allergy)
    db.session.commit()
    return "Allergy details added...!!!"

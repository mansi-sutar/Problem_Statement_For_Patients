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

@app.route('/medication_details')
def medication_details():
    medications = Medication.query.all()
    output = []
    for medication in medications:
        medications_data ={'Medication_ID' : medication.Medication_ID,
                           'Patient_ID' : medication.Patient_ID,
                           'Medication_Name' : medication.Medication_Name,
                           'Dose' : medication.Dose,
                           'Frequency' : medication.Frequency,
                           'Intake_Type' : medication.Intake_Type }
        output.append(medications_data)
    return { "Medications " : output }

@app.route('/add_medication',methods = ['POST'])
def add_medication():
    medications = Medication(Medication_ID = request.json['Medication_ID'],
                             Patient_ID = request.json['Patient_ID'],
                             Medication_Name = request.json['Medication_Name'],
                             Dose = request.json['Dose'],
                             Frequency = request.json['Frequency'],
                             Intake_Type = request.json['Intake_Type'])
    db.session.add(medications)
    db.session.commit()
    return "Medication details added...!!!"

@app.route('/delete_medication/<medication_id>',methods = ['DELETE'])
def delete_medication(medication_id):
    medication = Medication.query.get(medication_id)
    if medication is None:
        return "Id not found...!!!"
    db.session.delete(medication)
    db.session.commit()
    return "Medication deleted...!!!"

@app.route('/update_medication/<medication_id>',methods = ['PUT'])
def update_medication(medication_id):
   data = request.get_json()
   medication = Medication.query.get(medication_id)
   if medication is None:
       return "Id not found..!!!"
   if data.get('Medication_Name'):
       medication.Medication_Name = data['Medication_Name']
   if data.get('Dose'):
       medication.Dose = data['Dose']
   if data.get('Frequency'):
       medication.Frequency = data['Frequency']
   if data.get('Intake_Type'):
    medication.Intake_Type = data['Intake_Type']
   db.session.add(medication)
   db.session.commit()
   return "Medication details updated...!!!"



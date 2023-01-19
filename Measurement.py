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

@app.route('/add_measurement',methods = ['POST'])
def add_measurement():
    measurement = Measurement(Measurement_ID = request.json['Measurement_ID'],
                             Patient_ID = request.json['Patient_ID'],
                             Measurement_Name = request.json['Measurement_Name'],
                             Unit = request.json['Unit'],
                             Value = request.json['Value'])
    db.session.add(measurement)
    db.session.commit()
    return "Measurement details added...!!!"

@app.route('/measurement_details')
def measurement_details():
    measurements = Measurement.query.all()
    output = []
    for measurement in measurements:
        measurement_data ={'Measurement_ID' : measurement.Measurement_ID,
                           'Patient_ID' : measurement.Patient_ID,
                           'Measurement_Name' : measurement.Measurement_Name,
                           'Unit' : measurement.Unit,
                           'Value' : measurement.Value}
        output.append(measurement_data)
    return { "Measurements " : output }

@app.route('/delete_measurement/<measurement_id>',methods = ['DELETE'])
def delete_measurement(measurement_id):
    measurement = Measurement.query.get(measurement_id)
    if measurement is None:
        return "Id not found...!!!"
    db.session.delete(measurement)
    db.session.commit()
    return "Measurement deleted...!!!"

@app.route('/update_measurement/<measurement_id>',methods = ['PUT'])
def update_measurement(measurement_id):
   data = request.get_json()
   measurement = Measurement.query.get(measurement_id)
   if measurement is None:
       return "Id not found..!!!"
   if data.get('Measurement_Name'):
       measurement.Measurement_Name = data['Measurement_Name']
   if data.get('Unit'):
       measurement.Unit = data['Unit']
   if data.get('Value'):
       measurement.Value = data['Value']
   db.session.add(measurement)
   db.session.commit()
   return "Measurement details updated...!!!"


from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import InputRequired

###############################
###   App Calculator form   ###
###############################
class AddRecordForm(FlaskForm):
    bus_kms = FloatField("Bus (Kilometers)", [InputRequired()])
    bus_co2 = FloatField("Bus (CO2)")
    bus_type = SelectField("Bus (Type of Fuel)",
                           [InputRequired()],
                           choices=[
                               ('Bus Diesel', 'Bus Diesel'),
                               ('Bus CNG', 'Bus CNG'),
                               ('Bus Petrol', 'Bus Petrol'),
                               ('Bus No Fossil Fuel', 'Bus No Fossil Fuel')
                           ])
    car_kms = FloatField("Car (Kilometers)", [InputRequired()])
    car_co2 = FloatField("Car (CO2)")
    car_type = SelectField("Car (Type of Fuel)",
                           [InputRequired()],
                           choices=[
                               ('Car Petrol', 'Car Petrol'),
                               ('Car Diesel', 'Car Diesel'),
                               ('Car No Fossil Fuel', 'Car No Fossil Fuel')
                           ])
    plane_kms = FloatField("Plane (Kilometers)", [InputRequired()])
    plane_co2 = FloatField("Plane (CO2)")
    plane_type = SelectField("Plane (Type of Fuel)",
                           [InputRequired()],
                           choices=[
                               ('Plane Jet Fuel', 'Plane Jet Fuel'),
                               ('Plane No Fossil Fuel', 'Plane No Fossil Fuel')
                           ])
    ferry_kms = FloatField("Ferry (Kilometers)", [InputRequired()])
    ferry_co2 = FloatField("Ferry (CO2)")
    ferry_type = SelectField("Ferry (Type of Fuel)",
                             [InputRequired()],
                             choices=[
                                 ('Ferry Diesel', 'Ferry Diesel'),
                                 ('Ferry No Fossil Fuel', 'Ferry No Fossil Fuel')
                             ])
    motorbike_kms = FloatField("Motorbike (Kilometers)", [InputRequired()])
    motorbike_co2 = FloatField("Motorbike (CO2)")
    motorbike_type = SelectField("Motorbike (Type of Fuel)",
                             [InputRequired()],
                             choices=[
                                 ('Motorbike Petrol', 'Motorbike Petrol'),
                                 ('Motorbike No Fossil Fuel', 'Motorbike No Fossil Fuel')
                             ])
    scooter_kms = FloatField("Scooter (Kilometers)", [InputRequired()])
    scooter_co2 = FloatField("Scooter (CO2)")
    scooter_type = SelectField("Scooter (Type of Fuel)",
                                 [InputRequired()],
                                 choices=[
                                     ('Scooter No Fossil Fuel', 'Scooter No Fossil Fuel')
                                 ])
    bicycle_kms = FloatField("Bicycle (Kilometers)", [InputRequired()])
    bicycle_co2 = FloatField("Bicycle (CO2)")
    bicycle_type = SelectField("Bicycle (Type of Fuel)",
                               [InputRequired()],
                               choices=[
                                   ('Bicycle No Fossil Fuel', 'Bicycle No Fossil Fuel')
                               ])
    walk_kms = FloatField("Walk (Kilometers)", [InputRequired()])
    walk_co2 = FloatField("Walk (CO2)")
    walk_type = SelectField("Walk (Type of Fuel)",
                               [InputRequired()],
                               choices=[
                                   ('Walk No Fossil Fuel', 'Walk No Fossil Fuel')
                               ])
    submit = SubmitField("Submit")
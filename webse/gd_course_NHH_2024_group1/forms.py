from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField,  SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, NumberRange 
from webse.models import User
import requests
import json

class RegistrationForm(FlaskForm):
  username = StringField('Username', 
                         validators=[DataRequired(), Length(min=2, max=30)])
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password',
                      validators=[DataRequired(), EqualTo('password')])                                
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

  def validate_email(self, email):
      user = User.query.filter_by(email=email.data).first()
      if user:
          raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login') 

# Bus form
class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')])
  submit = SubmitField('Submit')

# Car form ("standard" car)
class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of fuel', [InputRequired()], 
    choices=[('Gasoline', 'Gasoline'),
             ('Diesel', 'Diesel'),
             ('Hybrid', 'Hybrid'),
             ('Electric', 'Electric'),
             ('Hydrogen', 'Hydrogen')])
  submit = SubmitField('Submit')

# Car form (connected to API)
class SpecificCarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  model = StringField("Model", [InputRequired()])
  submit = SubmitField('Submit')

# Plane form
class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of flight and class', [InputRequired()], 
    choices=[('Short-haul (Buisness)','Short-haul (Buisness)'),
             ('Long-haul (Economy)','Long-haul (Economy)'),
             ('Long-haul (Premium economy)', 'Long-haul (Premium economy)'),
             ('Long-haul (First-class)','Long-haul (First-class)'),
             ('International (Economy)', 'International (Economy)'),
             ('International (Premium economy)','International (Premium economy)'), 
             ('International (Buisness)', 'International (Buisness)'),
             ('International (First Class)','International (First Class)')])
  submit = SubmitField('Submit')

# Ferry form
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of ferry', [InputRequired()], 
    choices=[('Regular', 'Regular'),
             ('High-speed', 'High-speed')])
  submit = SubmitField('Submit')  

# Train form
class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'),
             ('Electric (Nordic)', 'Electric (Nordic)'),
             ('Electric (EU)', 'Electric (EU)')])
  submit = SubmitField('Submit')  

# Motorbike form
class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Engine size', [InputRequired()], 
    choices=[('≤125cc', '≤125cc'), ('125cc to 500cc', '125cc to 500cc'),('>500cc','>500cc')])
  submit = SubmitField('Submit')

# Bike form
class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

# Walk form
class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

#api
url = 'https://www.carboninterface.com/api'
headers = {'Authorization': 'Bearer Q6eGoxxENeS3vpIoXkKOw'}


class CarbonAPI:
    def __init__(self):
        req = requests.get(url + "/v1/auth", headers=headers)
        reqJson = req.json()
        ## If 404, throw error
        if (req.status_code == 404):
            print("Error: 404")
        else:
            print("API is working")
            print(reqJson)

    def allVehicleMakes(self):
        req = requests.get(url + "/v1/vehicle_makes", headers=headers)
        #print(req.json())
        return req.json()
    
    def getVehicleMake(self, id):
        if id is None:
            print("ID is required")

        req = requests.get(url + "/v1/vehicle_makes/" + id + "/vehicle_models", headers=headers)
        vehicle_models = req.json()

        unique_models = {}

        for model in vehicle_models:
            name = model["data"]["attributes"]["name"]
            year = model["data"]["attributes"]["year"]
            if name not in unique_models or unique_models[name]["year"] < year:
                unique_models[name] = {"year": year, "model": model}

        unique_vehicle_models = [model["model"] for model in unique_models.values()]

        return unique_vehicle_models
    
    def getEstimate(self, id, distance):
        if id is None:
            print("ID is required")

        data = {
            "vehicle_model_id": id,
            "type": "vehicle",
            "distance_unit": "km",
            "distance_value": int(distance)
        }

        formatedUrl = url + "/v1/estimates"

        req = requests.post(url=formatedUrl, json=data, headers=headers)
        return req.json()

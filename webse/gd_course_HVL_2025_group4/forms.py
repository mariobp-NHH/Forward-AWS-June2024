from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webse.models import User
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired

class RegistrationForm(FlaskForm):
  username = StringField('Username', 
                         validators=[DataRequired(), Length(min=2, max=30)])
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  institution = SelectField('Institution',
                              choices=[('company1', 'Company 1'),
                                       ('company2', 'Company 2'),
                                       ('Fantoft', 'Fantoft')],
                              validators=[DataRequired()])
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
class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Kerosene', 'Kerosene')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Electric', 'Electric'), ('Normal', 'Normal')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class ScooterForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Electric', 'Electric')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')  

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric')])
  days_used = SelectField(
    'Days used per week',
    choices=[(i, str(i)) for i in range(1, 8)],
    validators=[InputRequired()])
  submit = SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webse.models import User
from wtforms import  SubmitField,  SelectField,  FloatField, IntegerField
from wtforms.validators import InputRequired, NumberRange


class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])                                
  submit = SubmitField('Sign Up')

  def validate_username(self,username):
    user=User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('That username is taken.')
  
  def validate_email(self,email):
    email=User.query.filter_by(email=email.data).first()
    if email:
     raise ValidationError('That email is taken.')

class LoginForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')     

class BusForm(FlaskForm):
  kms=FloatField('Kilometers', [InputRequired()])
  fuel_type= SelectField('Type of fuel', [InputRequired()],
    choices=[('Diesel','Diesel'),('Biodiesel', 'Biodiesel'),('Electric', 'Electric')])
  submit=SubmitField('Submit') 

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Gasoline Small', 'Gasoline Small'), ('Diesel Campervan', 'Diesel Campervan'), ('Diesel Big', 'Diesel Big'), ('Diesel Medium', 'Diesel Medium'), ('Diesel Small', 'Diesel Small'), ('Electric Small', 'Electric Small'), ('Electric Medium', 'Electric Medium'), ('Electric Big', 'Electric Big')])
  passengers = IntegerField('Number of passengers', validators=[InputRequired(), NumberRange(min=1, max=5)])
  submit = SubmitField('Add') 

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric Nordic', 'Electric Nordic')])
  submit = SubmitField('Submit') 

class BybanenForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Electric', 'Electric')])
  submit = SubmitField('Submit')  

class ScooterForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Electric', 'Electric')])
  submit = SubmitField('Submit') 

class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric')])
  submit = SubmitField('Submit') 

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Travel class', [InputRequired()], 
    choices=[('Business', 'Business'), ('Economy Premium', 'Economy Premium'), ('Economy', 'Economy')])
  submit = SubmitField('Submit') 

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  
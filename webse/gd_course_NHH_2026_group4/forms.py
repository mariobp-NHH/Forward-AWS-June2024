from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webse.models import User


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


class BusForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Fuel type', choices=[
        ('Diesel', 'Diesel'),
        ('Electric/Hydrogen', 'Electric/Hydrogen')])
    submit = SubmitField('Submit')

class CarForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Fuel type', choices=[
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Hybrid', 'Hybrid'),
        ('Electric', 'Electric')])
    passengers = IntegerField('Number of passengers (including you)', 
        validators=[InputRequired(), NumberRange(min=1, max=8, message="Between 1 and 8 passengers")],
        default=1)
    submit = SubmitField('Submit')

class PlaneForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Flight class', choices=[
        ('Economy', 'Economy'),
        ('Business Class', 'Business Class')])
    submit = SubmitField('Submit')

class TrainForm(FlaskForm):
    kms = FloatField('Kilometers', validators=[InputRequired()])
    fuel_type = SelectField('Fuel type', choices=[
        ('Electric', 'Electric')])
    submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'),
             ('Electric', 'Electric')])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol'), 
             ('Electric', 'Electric')])
  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')  

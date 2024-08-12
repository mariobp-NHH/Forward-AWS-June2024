from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField,  SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, NumberRange 
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
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Biodiesel', 'Biodiesel')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Old Petrol', 'Old Petrol Car'), ('Old Diesel', 'Old Diesel Car'),('New Diesel', 'New Diesel Car'), ('New Petrol', 'New Petrol Car'), ('Small Electric', 'Small Electric Car'), ('Medium Electric', 'Medium Electric Car'), ('Large Electric', 'Large Electric Car')])
  submit = SubmitField('Submit')  

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
   choices=[('Long-haul Economy class', 'Long-haul Economy Class Plane'), ('Long-haul Business class', 'Long-haul Business Class Plane'), ('Long-haul First class', 'Long-haul First Class Plane'), ('Short-haul Economy class', 'Short-haul Economy Class Plane'), ('Short-haul Business class', 'Short-haul Business Class Plane'), ('Short-haul First class', 'Short-haul First Class Plane')])
  submit = SubmitField('Submit')
  
class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Diesel', 'Diesel'), ('Electric', 'Electric'),])
  submit = SubmitField('Submit')  

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
    choices=[('Petrol', 'Petrol')])
  submit = SubmitField('Submit')

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()], 
   choices=[('Diesel', 'Diesel'), ('Electric Nordic', 'Electric Nordic Train'), ('Electric European', 'Electric European Train')])

  submit = SubmitField('Submit')

class BicycleForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()], 
                            choices=[('No fossil fuel', 'No fossil fuel')])
    submit = SubmitField('Submit')  

class WalkForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()], 
                            choices=[('No fossil fuel', 'No fossil fuel')])
    submit = SubmitField('Submit')

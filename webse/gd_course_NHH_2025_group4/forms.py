from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField, StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, ValidationError
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
    choices=[('Diesel', 'Diesel')])
  submit = SubmitField('Submit')

class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  person = IntegerField('Persons')
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'),('LNG', 'LNG'), ('Electric', 'Electric'), ('Sports Car', 'Sports Car'),('Family Car', 'Family Car'),('Small Car', 'Small Car'),  ('No Fossil Fuel', 'No Fossil Fuel')])
  submit = SubmitField('Submit')

class PlaneForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Economy', 'Economy'),('Business/First','Business/First')])
  submit = SubmitField('Submit')

class TrainForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Diesel', 'Diesel'),('Electric','Electric'), ('Electric Norway','Electric Norway')])
  submit = SubmitField('Submit')

class FerryForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Fuel Oil', 'Fuel Oil')])
  submit = SubmitField('Submit')

class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Petrol', 'Petrol'),('No Fossil Fuel', 'No Fossil Fuel')])
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

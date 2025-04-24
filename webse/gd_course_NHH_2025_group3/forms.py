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
        raise ValidationError('This username is taken. Please choose a different one.')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('This email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')


class Form(FlaskForm):
  method = SelectField("Method of Transport", [InputRequired()],
                       choices=[("Car", "Car"), ("Bus", "Bus"), ('Train', 'Train'), ("Plane", "Plane"), ("Ferry", "Ferry"), ("Motorbike", "Motorbike"), ("Scooter", "Scooter"), ("Bicycle", "Bicycle"), ("Walk", "Walk")])
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Petrol', 'Petrol'), ('Biodiesel', 'Biodiesel'), ('Hybrid (gasoline)', 'Hybrid (gasoline)'), ('No Fossil Fuel', 'No Fossil Fuel')])
  passengers = IntegerField("Number of Passengers", default=1)
  submit = SubmitField('Submit')

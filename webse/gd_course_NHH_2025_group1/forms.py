from flask_wtf import FlaskForm
from wtforms import  SubmitField,  SelectField,  FloatField, StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, ValidationError
from webse.models import User

class BusForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Diesel', 'Diesel'),('Electric','Electric')])
  submit = SubmitField('Submit')


class CarForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'),('Electric','Electric')])
  submit = SubmitField('Submit')


class PlaneForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()],
        choices=[('Economy', 'Economy'), ('Business', 'Business'), ('First Class', 'First Class')])
    submit = SubmitField('Submit')


class FerryForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()],
        choices=[('Diesel', 'Diesel')])
    submit = SubmitField('Submit')


class MotorbikeForm(FlaskForm):
  kms = FloatField('Kilometers', [InputRequired()])
  fuel_type = SelectField('Type of Fuel', [InputRequired()],
    choices=[('Petrol','Petrol'),('Diesel', 'Diesel')])
  submit = SubmitField('Submit')


class TrainForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()],
        choices=[
            ('Diesel', 'Diesel'),
            ('Electric (Nordic)', 'Electric (Nordic)'),
            ('Electric (Europe excluding Nordic)', 'Electric (Europe excluding Nordic)')
        ])
    submit = SubmitField('Submit')


class VanForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()],
        choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric')])
    submit = SubmitField('Submit')


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

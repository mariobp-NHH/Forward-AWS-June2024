from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField,  SelectField, IntegerField
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
    kms = FloatField("Kilometers", validators=[InputRequired()])
    fuel_type = SelectField(
        "Type of Fuel",
        choices=[("Fossil fuel", "Fossil fuel"), ("Electric", "Electric")],
        validators=[InputRequired()],
    )
    submit = SubmitField("Submit")


class CarForm(FlaskForm):
    kms = FloatField("Kilometers", validators=[InputRequired()])
    size = SelectField(
        "Size of Car",
        choices=[("Normal", "Normal"), ("Small", "Small"), ("Large", "Large")],
        validators=[InputRequired()],
    )
    fuel_type = SelectField(
        "Type of Fuel",
        choices=[
            ("Petrol", "Petrol"),
            ("Diesel", "Diesel"),
            ("Hybrid", "Hybrid"),
            ("Electric", "Electric"),
        ],
        validators=[InputRequired()],
    )
    submit = SubmitField("Submit")


class TrainForm(FlaskForm):
    kms = FloatField("Kilometers", validators=[InputRequired()])
    fuel_type = SelectField(
        "Type of Fuel",
        choices=[("Fossil fuel", "Fossil fuel"), ("Electric", "Electric")],
        validators=[InputRequired()],
    )
    submit = SubmitField("Submit")


class PlaneForm(FlaskForm):
    kms = FloatField("Distance (in kilometers)", validators=[InputRequired()])
    flight_type = SelectField(
        "Type of Flight",
        choices=[
            ("Domestic flight", "Domestic flight"),
            ("Short-haul flight", "Short-haul flight"),
            ("Long-haul flight", "Long-haul flight"),
        ],
        validators=[InputRequired()],
    )
    submit = SubmitField("Submit")


class MotorbikeForm(FlaskForm):
    kms = FloatField("Kilometers", validators=[InputRequired()])
    fuel_type = SelectField(
        "Type of Fuel", choices=[("Petrol", "Petrol")], validators=[InputRequired()]
    )
    submit = SubmitField("Submit")


class WalkForm(FlaskForm):
    kms = FloatField("Kilometers", validators=[InputRequired()])
    fuel_type = SelectField(
        "Type of Fuel",
        choices=[("No Fossil Fuel", "No Fossil Fuel")],
        validators=[InputRequired()],
    )
    submit = SubmitField("Submit")


class BicycleForm(FlaskForm):
    kms = FloatField("Kilometers", validators=[InputRequired()])
    fuel_type = SelectField(
        "Type of Fuel",
        choices=[("No Fossil Fuel", "No Fossil Fuel")],
        validators=[InputRequired()],
    )
    submit = SubmitField("Submit")


class FerryForm(FlaskForm):
    kms = FloatField("Kilometers", validators=[InputRequired()])
    travel_option = SelectField(
        "Travel Option",
        choices=[
            ("Passenger", "Passenger"),
            ("Driver alone", "Driver alone"),
            ("Driver with passengers", "Driver with passengers"),
        ],
        validators=[InputRequired()],
    )
    passengers = IntegerField(
        "Number of Passengers", validators=[InputRequired()], default=0
    )
    submit = SubmitField("Submit")


# a form for deleting entires in the transport table
class DeleteForm(FlaskForm):
    submit = SubmitField("Delete")

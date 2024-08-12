from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField,  SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, NumberRange 
from webse.models import User

# Users Forms
class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators = [DataRequired(), Length(min=2, max=30)]
    )
    email = StringField(
        'Email',
        validators = [DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators = [DataRequired()]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators = [DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

#Validate username and email
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken. Please choose a different one.')
        
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('A user is already registered with that email. Please log in or choose a different one.')    

class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators = [DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators = [DataRequired()]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

# Carbon App Forms  
class WalkForm(FlaskForm):
    fuel = SelectField(
        choices=[('No Fuel', 'No Fuel')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')
    
class BikeForm(FlaskForm):
    fuel = SelectField(
        choices=[('Electric', 'Electric'),('No Fuel', 'No Fuel')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class CarForm(FlaskForm):
    fuel = SelectField(
        choices=[
            ('Diesel','Diesel'),
            ('Gas', 'Gas'),
            ('Electric','Electric (BEV)'),
            ('Electric & Gas','Plug-in Hybrid (PHEV)')
        ],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class BusForm(FlaskForm):    
    fuel = SelectField(
        choices=[('Diesel', 'Diesel')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class MotorcycleForm(FlaskForm):
    fuel = SelectField(
        choices=[('Gas', 'Gas')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class TrainForm(FlaskForm):
    fuel = SelectField(
        choices=[('Electric', 'Electric')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class TramForm(FlaskForm):
    fuel = SelectField(
        choices=[('Electric', 'Electric')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class MetroForm(FlaskForm):
    fuel = SelectField(
        choices=[('Electric', 'Electric')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class FerryForm(FlaskForm):
    fuel = SelectField(
        choices=[
            ('With_Car', 'With Car'),
            ('Without_Car', 'Without Car')
        ],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

class PlaneForm(FlaskForm):
    fuel = SelectField(
        choices=[('Domestic', 'Jetfuel (Kerosine)')],
        validators = [DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators = [DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

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
class RegForm(FlaskForm):
    transport = SelectField(
        choices=[
            ('Walking', 'Walking'),
            ('Bike', 'Bike'),
            ('Car', 'Car'),
            ('Motorcycle', 'Motorcycle'),
            ('Bus', 'Bus'),
            ('Plane', 'Plane'),
            ('Ferry', 'Ferry'),
            ('Train', 'Train'),
            ('Tram', 'Tram'),
            ('Metro', 'Metro')
        ],
        validators=[DataRequired()]
    )
    fuel = SelectField(
        choices=[
            ('Diesel', 'Diesel'),
            ('Gas', 'Gas'),
            ('Electric', 'Electric (BEV)'),
            ('Electric & Gas', 'Plug-in Hybrid (PHEV)'),
            ('No Fuel', 'No Fuel'),
            ('Diesel', 'Diesel'),
            ('Domestic', 'Jetfuel (Kerosine)'),
            ('Electric', 'Electric'),
            ('With_Car', 'With Car'),
            ('Without_Car', 'Without Car')
        ],
        validators=[DataRequired()]
    )
    kms = FloatField(
        'kms',
        validators=[DataRequired('Error: Input number'), NumberRange(0, 40075, 'Error: Input a positive number')]
    )
    submit = SubmitField('New Entry')

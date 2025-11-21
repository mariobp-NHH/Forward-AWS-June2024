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



class TransportForm(FlaskForm):
    transport = SelectField(
        'Transport Type',
        [InputRequired()],
        choices=[
            ('Bus', 'Bus'), ('Car', 'Car'),('Motorbike','Motorbike'),('Train','Train'),('Ferry','Ferry'),
            ('Plane Economy','Plane Economy'), ('Plane Business','Plane Business'),('Bybane','Bybane'),('Walking/Cycling','Walking/Cycling')])
    
    kms = FloatField(
        'Kilometers', 
        [InputRequired()])
    
    fuel_type = SelectField(
        'Type of fuel', 
        [InputRequired()],
        choices=[
            ('Diesel', 'Diesel'),('Petrol','Petrol'),('Electric','Electric'),('Human powered','Human powered'),('Jetfuel','Jetfuel'),('Fossil fuel','Fossil fuel')])
    
    passenger = FloatField(
        "Passengers",
        [InputRequired()],
        default=1,
    )

    submit=SubmitField('Submit')    


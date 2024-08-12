from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField,  SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from webse.models import User

# Users Forms
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

# Carbon App Forms  
class GenForm(FlaskForm):
    transport = SelectField('Mean of conveyance', [InputRequired()],
                            choices=[('Bus', 'Bus'), ('Car', 'Car'), ('Plane', 'Plane'), ('Boat', 'Boat'), 
                                     ('Motorbike', 'Motorbike'),
                                      ('Bicycle', 'Bicycle'), ('Walking', 'Walking'), ('Train', 'Train')])
    kms = FloatField('Kilometers', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()], 
                                choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('No Fossil Fuel', 'No Fossil Fuel'), 
                                         ('Gasoline','Gasoline'), ('Electric', 'Electric'), ('Jet fuel', 'Jet fuel'),
                                         ('CNG', 'CNG')])
    submit = SubmitField('Calculate')

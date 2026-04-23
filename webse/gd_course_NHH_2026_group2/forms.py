from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField, PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired, DataRequired, Email, EqualTo, Length, ValidationError
from webse.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('That username is already taken. Please choose a different one.')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('That email is already registered. Please use a different one.')
        
    def validate_password(self, password):
        if len(password.data) < 6:
            raise ValidationError('Password must be at least 6 characters long.')
   
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class BoatForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    seafood_kg = FloatField('Cargo Weight (kg)', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()],
                            choices=[('Diesel', 'Diesel / HFO'), ('LNG', 'LNG'), ('Electric', 'Electric / Zero Emission')])
    submit = SubmitField('Submit')

class PlaneForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    seafood_kg = FloatField('Cargo Weight (kg)', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()],
                            choices=[('Jet Fuel', 'Jet Fuel (Kerosene)'), ('SAF', 'SAF (Sustainable Aviation Fuel)')])
    submit = SubmitField('Submit')

class TruckForm(FlaskForm):
    kms = FloatField('Kilometers', [InputRequired()])
    seafood_kg = FloatField('Cargo Weight (kg)', [InputRequired()])
    fuel_type = SelectField('Type of Fuel', [InputRequired()],
                            choices=[('Diesel', 'Diesel'), ('LNG', 'LNG'), ('HVO', 'HVO (Biodiesel)'), ('Electric', 'Electric')])
    submit = SubmitField('Submit')
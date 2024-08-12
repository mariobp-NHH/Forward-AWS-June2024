from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webse.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=30)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    institution = SelectField(validators=[DataRequired(False)],
                       choices=[('Norwegian School of Economics (NHH)', 'Norwegian School of Economics (NHH)'),
                                ('Western Norway University of Applied Sciences (HVL)', 'Western Norway University of Applied Sciences (HVL)'),
                                ('Norwegian University of Life Sciences (NMBU)', 'Norwegian University of Life Sciences (NMBU)'),
                                ('University of Salamanca (USAL)', 'University of Salamanca (USAL)'),
                                ('Other', 'Other')])                                 
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

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    institution = SelectField(validators=[DataRequired(False)],
                       choices=[('Norwegian School of Economics (NHH)', 'Norwegian School of Economics (NHH)'),
                                ('Western Norway University of Applied Sciences (HVL)', 'Western Norway University of Applied Sciences (HVL)'),
                                ('Norwegian University of Life Sciences (NMBU)', 'Norwegian University of Life Sciences (NMBU)'),
                                ('Other', 'Other')])                      
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:            
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email: 
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

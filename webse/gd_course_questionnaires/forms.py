from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


#App Calculator. Questionnaires
class QuestionnaireForm_1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Bus', 'Bus'),
                                ('Car', 'Car'),
                                ('Plane', 'Plane'),
                                ('Ferry', 'Ferry'),
                                ('Scooter', 'Scooter'),
                                ('Bicycle', 'Bicycle'),
                                ('Motorbike', "Motorbike"),
                                ('Walk', 'Walk'),
                                ('Other', 'Other')])
    submit = SubmitField('Submit')

class QuestionnaireForm_1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Bus', 'Bus'),
                                ('Car', 'Car'),
                                ('Plane', 'Plane'),
                                ('Ferry', 'Ferry'),
                                ('Scooter', 'Scooter'),
                                ('Bicycle', 'Bicycle'),
                                ('Motorbike', "Motorbike"),
                                ('Walk', 'Walk'),
                                ('Other', 'Other')])
    submit = SubmitField('Submit')

class QuestionnaireForm_1_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Bus', 'Bus'),
                                ('Car', 'Car'),
                                ('Plane', 'Plane'),
                                ('Ferry', 'Ferry'),
                                ('Scooter', 'Scooter'),
                                ('Bicycle', 'Bicycle'),
                                ('Motorbike', "Motorbike"),
                                ('Walk', 'Walk'),
                                ('Other', 'Other')])
    submit = SubmitField('Submit')         

class QuestionnaireForm_1_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Bus', 'Bus'),
                                ('Car', 'Car'),
                                ('Plane', 'Plane'),
                                ('Ferry', 'Ferry'),
                                ('Scooter', 'Scooter'),
                                ('Bicycle', 'Bicycle'),
                                ('Motorbike', "Motorbike"),
                                ('Walk', 'Walk'),
                                ('Other', 'Other')])
    submit = SubmitField('Submit')

#Midway Conference (mc)
class QuestionnaireForm_mc_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_mc_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_mc_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')         

class QuestionnaireForm_mc_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit') 

class QuestionnaireForm_mc_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit') 

class QuestionnaireForm_mc_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit') 

#Hagesund Conference (ha)
class QuestionnaireForm_ha_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Veldig enig', 'Veldig enig'),
                                ('Enig', 'Enig'),
                                ('Være uenig', 'Være uenig'),
                                ('Sterkt uenig', 'Sterkt uenig')])
    submit = SubmitField('Submit')

class QuestionnaireForm_ha_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Veldig enig', 'Veldig enig'),
                                ('Enig', 'Enig'),
                                ('Være uenig', 'Være uenig'),
                                ('Sterkt uenig', 'Sterkt uenig')])
    submit = SubmitField('Submit')

class QuestionnaireForm_ha_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Veldig enig', 'Veldig enig'),
                                ('Enig', 'Enig'),
                                ('Være uenig', 'Være uenig'),
                                ('Sterkt uenig', 'Sterkt uenig')])
    submit = SubmitField('Submit')         

class QuestionnaireForm_ha_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Veldig enig', 'Veldig enig'),
                                ('Enig', 'Enig'),
                                ('Være uenig', 'Være uenig'),
                                ('Sterkt uenig', 'Sterkt uenig')])
    submit = SubmitField('Submit')     
    
# Chat Questionnaire
class ChatFormQuestionnaire(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')    

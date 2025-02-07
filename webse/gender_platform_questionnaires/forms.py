from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


#International Women's Day. Questionnaires
# Form questionnaire 1
class QuestionnaireForm_1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_1_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')         

class QuestionnaireForm_1_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit') 

# Form questionnaire 2  
class QuestionnaireForm_2_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_2_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_2_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')         

class QuestionnaireForm_2_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit') 

# Form questionnaire 3  
class QuestionnaireForm_3_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_3_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_3_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')         

class QuestionnaireForm_3_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

# Form questionnaire 4  
class QuestionnaireForm_4_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_4_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')

class QuestionnaireForm_4_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit')         

class QuestionnaireForm_4_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Strongly agree', 'Strongly agree'),
                                ('Agree', 'Agree'),
                                ('Disagree', 'Disagree'),
                                ('Stongly disagree', 'Strongly disagree')])
    submit = SubmitField('Submit') 

class ChatFormQuestionnaire(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')    
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class ChatForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

#Chapter 1
class ModulsForm_boa205_ch1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('kr 20 000',
                                 'kr 20 000'),
                                ('kr -20 000',
                                 'kr -20 000'),
                                ('kr 0',
                                 'kr 0')])
    submit = SubmitField('Send inn')  

class ModulsForm_boa205_ch1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('kr 5 000',
                                 'kr 5 000'),
                                ('Mer enn kr 5 000',
                                 'Mer enn kr 5 000'),
                                ('Mindre enn kr 5 000',
                                 'Mindre enn kr 5 000')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch1_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('kr -169 000',
                                 'kr -169 000'),
                                ('kr -145 000',
                                 'kr -145 000'),
                                ('kr -121 000',
                                 'kr -121 000')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch1_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('kr -245 000',
                                 'kr -245 000'),
                                ('kr -145 000',
                                 'kr -145 000'),
                                ('kr -45 000',
                                 'kr -45 000')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch1_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('kr -154 999',
                                 'kr -154 999'),
                                ('kr -145 000',
                                 'kr -145 000'),
                                ('kr -134 998',
                                 'kr -134 998')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch1_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('kr -145 000',
                                 'kr -145 000'),
                                ('kr -40 000',
                                 'kr -40 000'),
                                ('kr 23 000',
                                 'kr 23 000')])
    submit = SubmitField('Send inn')

class TableForm_boa205_ch1_t1(FlaskForm):
    renter = SelectField("Renter",
                       choices=[('0.05',
                                 '5%'),
                                ('0.07',
                                 '7%'),
                                ('0.03',
                                 '3%')])
    eierlonn = SelectField("Eierlønn",
                       choices=[('700000',
                                 'kr 700 000'),
                                ('800000',
                                 'kr 800 000'),
                                 ('600000',
                                 'kr 600 000')])
    salgsverdi = SelectField("Salgsverdi",
                       choices=[('100000',
                                 'kr 100000'),
                                ('90000',
                                 'kr 90 000'),
                                 ('110000',
                                 'kr 110 000')])
    ar = SelectField("År med avskrivninger",
                       choices=[('3',
                                 '3'),
                                ('4',
                                 '4'),
                                 ('5',
                                 '5')])
    submit = SubmitField('Send inn') 

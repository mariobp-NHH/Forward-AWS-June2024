from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class ChatForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

#Chapter 2
class SpotGo_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('An increase in competition in the spot market',
                                 'An increase in competition in the spot market'),
                                ('A decrease in competition in the spot market',
                                 'A decrease in competition in the spot market'),
                                ('It has no impact on the competition in the spot market',
                                 'It has no impact on the competition in the spot market')])
    submit = SubmitField('Submit')  

class SpotGo_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('It reduces competition in the spot market',
                                 'It reduces competition in the spot market'),
                                ('It fosters competition in the spot market',
                                 'It fosters competition in the spot market'),
                                ('It does not affect competition in the spot market',
                                 'It does not affect competition in the spot market')])
    submit = SubmitField('Submit')    

class SpotGo_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Allow all the green production capacity to participate in the GO market',
                                 'Allow all the green production capacity to participate in the GO market'),
                                ('Do not interfere in the GO market',
                                 'Do not interfere in the GO market'),
                                ('Allow only the new green production technology capacity to participate in the GO market',
                                 'Allow only the new green production technology capacity to participate in the GO market')])
    submit = SubmitField('Submit') 

class SpotGo_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('It activates the competition in the GO market',
                                 'It activates the competition in the GO market'),
                                ('It deactivates the competition in the GO market',
                                 'It deactivates the competition in the GO market'),
                                ('It does not modify the competition in the GO market',
                                 'It does not modify the competition in the GO market')])
    submit = SubmitField('Submit') 

class SpotGo_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('5.923',
                                 '5.923'),
                                ('5.137',
                                 '5.137'),
                                ('4.567',
                                 '4.567')])
    submit = SubmitField('Submit') 
    
class SpotGo_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('5.856',
                                 '5.856'),
                                ('5.395',
                                 '5.395'),
                                ('4.954',
                                 '4.954')])
    submit = SubmitField('Submit')      

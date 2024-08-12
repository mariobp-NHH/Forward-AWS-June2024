from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Optional
from webse.models import User

class ModulsForm_m2_ch1_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Reducing the waste of food in supermarkets and restaurants', 'Reducing the waste of food in supermarkets and restaurants'),
                                ('Reducing transport carbon emissions and the public transport', 'Reducing transport carbon emissions and the public transport'),
                                ('Improving the recycling system', 'Improving the recycling system')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Yes, substantially', 'Yes, substantially'),
                                ('Yes, slightly', 'Yes, slightly'),
                                ('No', 'No')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch1_e3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Yes, substantially', 'Yes, substantially'),
                                ('Yes, slightly', 'Yes, slightly'),
                                ('No', 'No')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch1_e4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Yes, substantially', 'Yes, substantially'),
                                ('Yes, slightly', 'Yes, slightly'),
                                ('No', 'No')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Produce energy locally', 'Produce energy locally'),
                                ('Share ownership of energy technologies', 'Share ownership of energy technologies'),
                                ('Buy green energy from another country', 'Buy green energy from another country')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Focus only on the aesthetic', 'Focus only on the aesthetic'),
                                ('Help accessibility to people with reduced mobility', 'Help accessibility to people with reduced mobility'),
                                ('Create safe an inviting spaces for women, minorities and people with different sexual orientations', 'Create safe an inviting spaces for women, minorities and people with different sexual orientations')])
    submit = SubmitField('Submit') 


# Chapter 2
class ModulsForm_m2_ch2_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Demand is difficult to forecast', 'Demand is difficult to forecast'),
                                ('Storage is prohibitively costly', 'Storage is prohibitively costly'),
                                ('Demand and supply have to match all the time', 'Demand and supply have to match all the time')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The transmission line can be congested', 'The transmission line can be congested'),
                                ('Low demand elasticity', 'Low demand elasticity'),
                                ('Electricity cannot be stored', 'Electricity cannot be stored')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch2_e3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The introduction of sensors at home', 'The introduction of sensors at home'),
                                ('The introduction of sensors in the grid', 'The introduction of sensors in the grid'),
                                ('Real time electricity pricing apps', 'Real time electricity pricing apps')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch2_e4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Yes, substantially', 'Yes, substantially'),
                                ('Yes, slightly', 'Yes, slightly'),
                                ('No', 'No')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch2_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Storage is prohibitively costly', 'Storage is prohibitively costly'),
                                ('Electricity is produced in remote rural areas', 'Electricity is produced in remote rural areas'),
                                ('Demand and supply have to match all the time', 'Demand and supply have to match all the time')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Long-term contracts ensure electricity consumption in the long term', 'Long-term contracts ensure electricity consumption in the long term'),
                                ('Long-term contracts guarantee a deterministic price', 'Long-term contracts guarantee a deterministic price'),
                                ('Long-term contracts reduce the incentives to restric output', 'Long-term contracts reduce the incentives to restric output')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch2_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Electricity consumption is stable during the day', 'Electricity consumption is stable during the day'),
                                ('The non-storability of electricity', 'The non-storability of electricity'),
                                ('The very low elasticity of demand for electricity', 'The very low elasticity of demand for electricity')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch2_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('An active demand side that can respond to spot market price signals', 'An active demand side that can respond to spot market price signals'),
                                ('Stable consumption in the industry', 'Stable consumption in the industry'),
                                ('Forward contracts to mitigate market power', 'Forward contracts to mitigate market power')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch2_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Creates value to the customers that make upwards or downwards consumption', 'Creates value to the customers that make upwards or downwards consumption'),
                                ('Foster the development of renewable energy', 'Foster the development of renewable energy'),
                                ('Reduce the consumption of energy', 'Reduce the consumption of energy')])
    submit = SubmitField('Submit') 

class ModulsForm_m2_ch2_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Solve the congestion problems in the grid that connect different countries', 'Solve the congestion problems in the grid that connect different countries'),
                                ('Solve the congestion problems in the grid at local level', 'Solve the congestion problems in the grid at local level'),
                                ('Solve supply fluctuation of electricity du to the introduction of renewable energy', 'Solve supply fluctuation of electricity du to the introduction of renewable energy')])
    submit = SubmitField('Submit') 

# Chapter 3
class ModulsForm_m2_ch3_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Access in real time to databases, information, and simulations', 'Access in real time to databases, information, and simulations'),
                                ('Better information from the consumers', 'Better information from the consumers'),
                                ('Better information with suppliers', 'Better information with suppliers')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Statistical packages (e.g., R, Stata); programming languages (e.g., Python)', 'Statistical packages (e.g., R, Stata); programming languages (e.g., Python)'),
                                ('Excel with basic functionality', 'Excel with basic functionality'),
                                ('More advanced Excel (including Power-BI, Solver, Miner, and Macros)', 'More advanced Excel (including Power-BI, Solver, Miner, and Macros)')])
    submit = SubmitField('Submit') 
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

#Chapter 2
class ModulsForm_boa205_ch2_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('lønn til ansatte som jobber direkte med produksjonen',
                                 'lønn til ansatte som jobber direkte med produksjonen'),
                                ('generelle kostnader i husleie',
                                 'generelle kostnader i husleie'),
                                ('spesifikk frakt knyttet til materialer for ett produkt',
                                 'spesifikk frakt knyttet til materialer for ett produkt')])
    submit = SubmitField('Send inn')  

class ModulsForm_boa205_ch2_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('trevirke for møbler, stål for sykler, eller gummi for dekk',
                                 'trevirke for møbler, stål for sykler, eller gummi for dekk'),
                                ('generelle kampanjer om markedsføring og salg',
                                 'generelle kampanjer om markedsføring og salg'),
                                ('renter, avskrivninger',
                                 'renter, avskrivninger')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('800 kr per time',
                                 '800 kr per time'),
                                ('875 kr per time',
                                 '875 kr per time'),
                                ('900 kr per time',
                                 '900 kr per time')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('selvkostmetoden tar hensyn til alle direkte kostnader',
                                 'selvkostmetoden tar hensyn til alle direkte kostnader'),
                                ('selvkostmetoden tar hensyn til alle faste kostnader',
                                 'selvkostmetoden tar hensyn til alle faste kostnader'),
                                ('selvkostmetoden tar hensyn til alle direkte og indirekte kostnader',
                                 'selvkostmetoden tar hensyn til alle direkte og indirekte kostnader')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-37000',
                                 '-37000'),
                                ('-35000',
                                 '-35000'),
                                ('-30000',
                                 '-30000')])
    submit = SubmitField('Send inn')  

class ModulsForm_boa205_ch2_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-11000',
                                 '-11000'),
                                ('-10000',
                                 '-10000'),
                                ('-5000',
                                 '-5000')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-5000',
                                 '-5000'),
                                ('-4500',
                                 '-4500'),
                                ('-4000',
                                 '-4000')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-8000',
                                 '-8000'),
                                ('-7000',
                                 '-7000'),
                                ('-6000',
                                 '-6000')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('73700000',
                                 '73700000'),
                                ('74000000',
                                 '74000000'),
                                ('74300000',
                                 '74300000')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('73000000',
                                 '73000000'),
                                ('74800000',
                                 '74800000'),
                                ('75000000',
                                 '75000000')])
    submit = SubmitField('Send inn') 

class TableForm_boa205_ch2_t1(FlaskForm):
    direkte_material_normal= SelectField("Direkte Material Normal",
                       choices=[('250000',
                                 'kr 250 000'),
                                ('300000',
                                 'kr 300 000'),
                                ('350000',
                                 'kr 350 000')])
    faste_material_budsjett = SelectField("Faste Material Budsjett",
                       choices=[('20000',
                                 'kr 20 000'),
                                ('25000',
                                 'kr 25 000'),
                                 ('30000',
                                 'kr 30 000')])
    indirekte_materialkostnader_faste_normalsatser = SelectField("Indirekte Materialkostnader Faste Normalsatser",
                       choices=[('0.06',
                                 '6%'),
                                ('0.08',
                                 '8%'),
                                 ('0.1',
                                 '10%')])
    indirekte_tilvirkningskostnader_faste_normalsatser = SelectField("Indirekte Tilvirkningskostnader Faste Normalsatser",
                       choices=[('0.18',
                                 '18%'),
                                ('0.2',
                                 '20%'),
                                 ('0.22',
                                 '22%')])
    submit = SubmitField('Send inn')

class TableForm_boa205_ch2_t2(FlaskForm):
    lagerreduksjon_selv= SelectField("Lagerreduksjon Selvkostmetoden",
                       choices=[('800000',
                                 'kr 800 000'),
                                ('850000',
                                 'kr 850 000'),
                                ('900000',
                                 'kr 900 000')])
    ferdigvaren_selv = SelectField("Ferdigvaren Selvkostmetoden",
                       choices=[('1400000',
                                 'kr 1 400 000'),
                                ('1500000',
                                 'kr 1 500 000'),
                                 ('1600000',
                                 'kr 1 600 000')])
    lagerreduksjon_bidra= SelectField("Lagerreduksjon Bidragsmetoden",
                       choices=[('650000',
                                 'kr 650 000'),
                                ('670000',
                                 'kr 670 000'),
                                ('700000',
                                 'kr 700 000')])
    ferdigvaren_bidra = SelectField("Ferdigvaren Bidragsmetoden",
                       choices=[('900000',
                                 'kr 900 000'),
                                ('1000000',
                                 'kr 1 000 000'),
                                 ('1100000',
                                 'kr 1 100 000')])
    submit = SubmitField('Send inn')

""" Chapter 2b """
class ModulsForm_boa205_ch2b_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('desember',
                                 'desember'),
                                ('januar',
                                 'januar'),
                                ('begge måneder',
                                 'begge måneder')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2b_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('desember',
                                 'desember'),
                                ('januar',
                                 'januar'),
                                ('begge måneder',
                                 'begge måneder')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2b_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('januar',
                                 'januar'),
                                ('februar',
                                 'februar'),
                                ('begge måneder',
                                 'begge måneder')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2b_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-17629',
                                 '-17629'),
                                ('-17567',
                                 '-17567'),
                                ('-17490',
                                 '-17490')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2b_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('2000',
                                 '2000'),
                                ('2500',
                                 '2500'),
                                ('3000',
                                 '3000')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch2b_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-5650',
                                 '-5650'),
                                ('-5335',
                                 '-5335'),
                                ('-5220',
                                 '-5220')])
    submit = SubmitField('Send inn') 

class TableForm_boa205_ch2b_t1(FlaskForm):
    endring_varer_i_arbeid_102= SelectField("Endring varer i arbeid ordre 102",
                       choices=[('7000',
                                 'kr 7000'),
                                ('7430',
                                 'kr 7430'),
                                ('7800',
                                 'kr 7800')])
    endring_ferdige_varer_101 = SelectField("Endring ferdige varer ordre 101",
                       choices=[('105000',
                                 'kr 105 000'),
                                ('109500',
                                 'kr 109 500'),
                                 ('110000',
                                 'kr 110 000')])
    submit = SubmitField('Send inn')

class TableForm_boa205_ch2b_t2(FlaskForm):
    endring_varer_i_arbeid_102= SelectField("Endring varer i arbeid ordre 102",
                       choices=[('5500',
                                 'kr 5500'),
                                ('6035',
                                 'kr 6035'),
                                ('6500',
                                 'kr 6500')])
    endring_ferdige_varer_101 = SelectField("Endring ferdige varer ordre 101",
                       choices=[('85000',
                                 'kr 85 000'),
                                ('88900',
                                 'kr 88 900'),
                                 ('95000',
                                 'kr 95 000')])
    submit = SubmitField('Send inn')

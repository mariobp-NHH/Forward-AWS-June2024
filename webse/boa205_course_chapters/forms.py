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
                       choices=[('bare desember',
                                 'bare desember'),
                                ('bare januar',
                                 'bare januar'),
                                ('begge to måneder',
                                 'begge to måneder')])
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

""" Chapter 3 """
class TableForm_boa205_ch3_t1(FlaskForm):
    pris_beholdning_1_januar= SelectField("Pris beholdning material 01 januar",
                       choices=[('49',
                                 'kr/ltr 49'),
                                ('50',
                                 'kr/ltr 50'),
                                ('51',
                                 'kr/ltr 51')])
    pris_innkjop_material_i_januar = SelectField("Pris innkjøp material i januar",
                       choices=[('51',
                                 'kr/ltr 51'),
                                ('51.43',
                                 'kr/ltr 51.43'),
                                 ('52',
                                 'kr/ltr 52')])
    submit = SubmitField('Send inn')

class TableForm_boa205_ch3_t2(FlaskForm):
    standard_lonn= SelectField("Standard lønn i januar",
                       choices=[('298',
                                 '298 kr/t'),
                                ('300',
                                 '300 kr/t'),
                                ('302',
                                 '302 kr/t')])
    virkelig_timer = SelectField("Virkelige timer i januar",
                       choices=[('862',
                                 '862 timer'),
                                ('865',
                                 '865 time'),
                                 ('868',
                                 '868 timer')])
    submit = SubmitField('Send inn')

class TableForm_boa205_ch3_t3(FlaskForm):
    sat_faste_indirekte_tilv= SelectField("Standardsats faste indirekte tilvirk kost",
                       choices=[('28',
                                 '28 kr'),
                                ('30',
                                 '30 kr'),
                                ('32',
                                 '32 kr')])
    sat_variable_indirekte_tilv= SelectField("Standardsats variable indirekte tilvirk kost",
                       choices=[('18',
                                 '18 kr'),
                                ('20',
                                 '20 kr'),
                                ('22',
                                 '22 kr')])
    sat_faste_administrasjon= SelectField("Standardsats faste administrasjonkostnader",
                       choices=[('98',
                                 '98 kr'),
                                ('100',
                                 '100 kr'),
                                ('102',
                                 '102 kr')])
    submit = SubmitField('Send inn')

class TableForm_boa205_ch3_t4(FlaskForm):
    sat_faste_indirekte_tilv_t4= SelectField("Standardsats faste indirekte tilvirk kost",
                       choices=[('28',
                                 '28 kr'),
                                ('30',
                                 '30 kr'),
                                ('32',
                                 '32 kr')])
    sat_variable_indirekte_tilv_t4= SelectField("Standardsats variable indirekte tilvirk kost",
                       choices=[('18',
                                 '18 kr'),
                                ('20',
                                 '20 kr'),
                                ('22',
                                 '22 kr')])
    sat_faste_administrasjon_t4= SelectField("Standardsats faste administrasjonkostnader",
                       choices=[('98',
                                 '98 kr'),
                                ('100',
                                 '100 kr'),
                                ('102',
                                 '102 kr')])
    submit_t4 = SubmitField('Send inn')

class ModulsForm_boa205_ch3_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-1000',
                                 '-1000'),
                                ('-980',
                                 '-980'),
                                ('-940',
                                 '-940')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch3_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-106',
                                 '-106'),
                                ('-104',
                                 '-104'),
                                ('-102',
                                 '-102')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch3_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('2010',
                                 '2010'),
                                ('2250',
                                 '2250'),
                                ('2400',
                                 '2400')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch3_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-6085',
                                 '-6085'),
                                ('-6050',
                                 '-6050'),
                                ('-6025',
                                 '-6025')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch3_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('1688',
                                 '1688'),
                                ('1698',
                                 '1698'),
                                ('1705',
                                 '1705')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch3_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-240',
                                 '-240'),
                                ('-235',
                                 '-235'),
                                ('-232',
                                 '-232')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch3_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-23550',
                                 '-23550'),
                                ('-23120',
                                 '-23120'),
                                ('-23050',
                                 '-23050')])
    submit = SubmitField('Send inn') 

class ModulsForm_boa205_ch3_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-21200',
                                 '-21200'),
                                ('-21150',
                                 '-21150'),
                                ('-21045',
                                 '-21045')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch3_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-305',
                                 '-305'),
                                ('-300',
                                 '-300'),
                                ('-297',
                                 '-297')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch3_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-4000',
                                 '-4000'),
                                ('-3995',
                                 '-3995'),
                                ('-3992',
                                 '-3992')])
    submit = SubmitField('Send inn')

""" Chapter 4 """
class TableForm_boa205_ch4_t1(FlaskForm):
    budsjettert_pris_produkt_alfa= SelectField("Budsjettert pris produkt alfa",
                       choices=[('7',
                                 '7 kr'),
                                ('8',
                                 '8 kr'),
                                ('9',
                                 '9 kr')])
    budsjettert_pris_produkt_omega= SelectField("Budsjettert pris produkt omega",
                       choices=[('11',
                                 '11 kr'),
                                ('12',
                                 '12 kr'),
                                ('13',
                                 '13 kr')])
    virkelig_salg_i_enheter_alfa= SelectField("Virkelig salg i enheter alfa",
                       choices=[('5950',
                                 '5950'),
                                ('6000',
                                 '6000'),
                                ('6050',
                                 '6050')])
    virkelig_salg_i_enheter_omega= SelectField("Virkelig salg i enheter omega",
                       choices=[('6950',
                                 '6950'),
                                ('7000',
                                 '7000'),
                                ('7050',
                                 '7050')])
    submit = SubmitField('Send inn')

class TableForm_boa205_ch4_t2(FlaskForm):
    budsjettert_pris_tex= SelectField("Budsjettert pris produkt Tex",
                       choices=[('85',
                                 '85 kr'),
                                ('90',
                                 '90 kr'),
                                ('95',
                                 '95 kr')])
    budsjettert_pris_mex= SelectField("Budsjettert pris produkt Mex",
                       choices=[('45',
                                 '45 kr'),
                                ('50',
                                 '50 kr'),
                                ('55',
                                 '55 kr')])
    budsjettert_DB_tex= SelectField("Dekningsbidrag produkt Tex",
                       choices=[('25',
                                 '25 kr'),
                                ('30',
                                 '30 kr'),
                                ('35',
                                 '35 kr')])
    budsjettert_DB_mex= SelectField("Dekningsbidrag produkt Mex",
                       choices=[('20',
                                 '20 kr'),
                                ('25',
                                 '25 kr'),
                                ('30',
                                 '30 kr')])
    submit = SubmitField('Send inn')

class TableForm_boa205_ch4_t3(FlaskForm):
    virkelig_salgsvolum_3031= SelectField("Virkelig salgsvolum 3031",
                       choices=[('170',
                                 '170 enheter'),
                                ('180',
                                 '180 enheter'),
                                ('190',
                                 '190 enheter')])
    virkelig_salgsvolum_3032= SelectField("Virkelig salgsvolum 3032",
                       choices=[('240',
                                 '240 enheter'),
                                ('250',
                                 '250 enheter'),
                                ('260',
                                 '260 enheter')])
    db_3031= SelectField("Dekningsbidrag produkt 3031",
                       choices=[('164',
                                 '164 kr'),
                                ('169',
                                 '169 kr'),
                                ('175',
                                 '175 kr')])
    db_3032= SelectField("Dekningsbidrag produkt 3032",
                       choices=[('179',
                                 '179 kr'),
                                ('186',
                                 '186 kr'),
                                ('193',
                                 '193 kr')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-6000',
                                 '-6000'),
                                ('-5800',
                                 '-5800'),
                                ('-5700',
                                 '-5700')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('6690',
                                 '6690'),
                                ('6654',
                                 '6654'),
                                ('6648',
                                 '6648')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('8.5',
                                 '8.5'),
                                ('8.32',
                                 '8.32'),
                                ('8.1',
                                 '8.1')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-2200',
                                 '-2200'),
                                ('-2146',
                                 '-2146'),
                                ('-2034',
                                 '-2034')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-1050',
                                 '-1050'),
                                ('-1026',
                                 '-1026'),
                                ('-1000',
                                 '-1000')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('13050',
                                 '13050'),
                                ('13000',
                                 '13000'),
                                ('12995',
                                 '12995')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-1769',
                                 '-1769'),
                                ('-1755',
                                 '-1755'),
                                ('-1750',
                                 '-1750')]) 
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('6720',
                                 '6720'),
                                ('6725',
                                 '6725'),
                                ('6726',
                                 '6726')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('14395',
                                 '14395'),
                                ('14440',
                                 '14440'),
                                ('14447',
                                 '14447')])
    submit = SubmitField('Send inn')

class ModulsForm_boa205_ch4_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('-7497',
                                 '-7497'),
                                ('-7478',
                                 '-7478'),
                                ('-7450',
                                 '-7450')])
    submit = SubmitField('Send inn')

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired, Optional
from webse.models import User


class ChatFormUpdate(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

class ChatFormExercise(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Chat')

#M2_Ch1: SE, Frame.
class ModulsForm_m2_ch1_e1(FlaskForm):
    type = SelectField(validators=[DataRequired(False)],
                       choices=[('Should include only environmental pollution, carbon emissions', 'Should include only environmental pollution, carbon emissions'),
                                ('Should include only poverty alleviation, gender equality', 'Should include only poverty alleviation, gender equality'),
                                ('Should include both', 'Should include both')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_e2(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Green Economy is more related to welfare and environmental economics', 'Green Economy is more related to welfare and environmental economics'),
                                ('Green Economy is more related to ecological economics', 'Green Economy is more related to ecological economics'),
                                ('Green Economy is more related to economics schools', 'Green Economy is more related to economics schools')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Should only consider carbon emissions', 'Should only consider carbon emissions'),
                                ('Should only consider electrification', 'Should only consider electrification'),
                                ('Should also consider social aspects', 'Should also consider social aspects')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch1_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Pollution is a negative externality', 'Pollution is a negative externality'),
                                ('Sustainability and economy are a subsystem of the ecosystem', 'Sustainability and economy are a subsystem of the ecosystem'),
                                ('Research and technology are fundamental parts of agriculture development', 'Research and technology are fundamental parts of agriculture development')])
    submit = SubmitField('Submit')

#M2_Ch2: SE. Ch2. Ecological Footprint and Biocapacity
class ModulsForm_m2_ch2_e1(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('The ecological footprint should be charged to Norway', 'The ecological footprint should be charged to Norway'),
                                ('The ecological footprint should be charged to Spain', 'The ecological footprint should be charged to Spain'),
                                ('The ecological footprint should be charged partially to both countries', 'The ecological footprint should be charged partially to both countries')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_e2(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Land to capture carbon emissions', 'Land to capture carbon emissions'),
                                ('Cropland, grazing land, fishing grounds, and forest products land', 'Cropland, grazing land, fishing grounds, and forest products land'),
                                ('All the previous types of lands', 'All the previous types of lands')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_e3(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Land to capture carbon emissions', 'Land to capture carbon emissions'),
                                ('Cropland', 'Cropland'),
                                ('Fishing grounds', 'Fishing grounds')])
    submit = SubmitField('Submit')


class ModulsForm_m2_ch2_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Biologically productive area it takes to satisfy the exporting demand', 'Biologically productive area it takes to satisfy the exporting demand'),
                                ('Biologically productive area it takes to satisfy the demands of people', 'Biologically productive area it takes to satisfy the demands of people'),
                                ('Biologically productive area it takes to satisfy the importing demand', 'Biologically productive area it takes to satisfy the importing demand')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Land and sea area available to provide the resources a population consumes and to absorb its wastes',
                                 'Land and sea area available to provide the resources a population consumes and to absorb its wastes'),
                                ('Land and sea area available for agriculture and fisheries',
                                 'Land and sea area available for agriculture and fisheries'),
                                ('Land area available for wildlife',
                                 'Land area available for wildlife')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Productive land required to absorb the carbon dioxide emissions',
                                'Productive land required to absorb the carbon dioxide emissions'),
                                ('Amount of carbon absorbed by oceans',
                                 'Amount of carbon absorbed by oceans'),
                                ('Both', 'Both')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Cropland, grazing land, fishing grounds (marine waters), forest, and built-up',
                                'Cropland, grazing land, fishing grounds (marine waters), forest, and built-up'),
                                ('Cropland, grazing land, fishing grounds (marine and inland waters), forest, and built-up',
                                 'Cropland, grazing land, fishing grounds (marine and inland waters), forest, and built-up'),
                                ('Cropland, grazing land, fishing grounds (marine and inland waters), and forest',
                                 'Cropland, grazing land, fishing grounds (marine and inland waters), and forest')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Reflect the relative productivity of a given land use type',
                                'Reflect the relative productivity of a given land use type'),
                                ('Reflect the relative productivity of cropland',
                                 'Reflect the relative productivity of cropland'),
                                ('Reflect the relative productivity of fishing grounds',
                                 'Reflect the relative productivity of fishing grounds')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Very suitable, suitable, moderately suitable, and marginally suitable',
                                'Very suitable, suitable, moderately suitable, and marginally suitable'),
                                ('Very suitable, suitable, marginally suitable, and not suitable',
                                 'Very suitable, suitable, marginally suitable, and not suitable'),
                                ('Very suitable, suitable, moderately suitable, marginally suitable, and not suitable',
                                 'Very suitable, suitable, moderately suitable, marginally suitable, and not suitable')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'In the 80s',
                                'In the 80s'),
                                ('In the 70s',
                                 'In the 70s'),
                                ('In the 90s',
                                 'In the 90s')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch2_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'It represents the 50%','It represents the 50%'),
                                ('It represents the 40%','It represents the 40%'),
                                ('It represents the 60%', 'It represents the 60%')])
    submit = SubmitField('Submit')

#M2_Ch3: SE. Ch3. Human Development for the Anthropocene
class ModulsForm_m2_ch3_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('At the beginning of the Agricultural Revolution 12.000–15.000 years ago',
                                 'At the beginning of the Agricultural Revolution 12.000–15.000 years ago'),
                                ('In 1945 after the detonation of the first atomic bomb',
                                 'In 1945 after the detonation of the first atomic bomb'),
                                ('At the beginning of the Industrial Revolution',
                                 'At the beginning of the Industrial Revolution')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_e2(FlaskForm):
    type = SelectField(validators=[DataRequired()],
                       choices=[('Carbon emissions', 'Carbon emissions'),
                                ('Ecological Footprint', 'Ecological Footprint'),
                                ('Both', 'Both')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch3_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('At the beginning of the Agricultural Revolution 12.000–15.000 years ago', 'At the beginning of the Agricultural Revolution 12.000–15.000 years ago'),
                                ('In 1945 after the detonation of the first atomic bomb', 'In 1945 after the detonation of the first atomic bomb'),
                                ('The debate about the starting date of the Antrophocene is still open', 'The debate about the starting date of the Antrophocene is still open')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Homogenization of flora and fauna',
                                 'Homogenization of flora and fauna'),
                                ('One species (humans) consuming 25–40 percent of land net primary productivity',
                                 'One species (humans) consuming 25–40 percent of land net primary productivity'),
                                ('Increasing impact of new technologies as the biosphere interacts with the technosphere',
                                 'Increasing impact of new technologies as the biosphere interacts with the technosphere'),
                                ('Increase in arid areas',
                                 'Increase in arid areas')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Those elements do not interact with humans, and do not determine the relations of power and culture',
                                'Those elements do not interact with humans, and do not determine the relations of power and culture'),
                                ('Those elements do not interact with humans, and determine the relations of power and culture',
                                 'Those elements do not interact with humans, and determine the relations of power and culture')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch3_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Chemical pollution, and ocean acidification',
                                'Chemical pollution, and ocean acidification'),
                                ('Freshwater use, and phosphorus cycle',
                                 'Freshwater use, and phosphorus cycle'),
                                ('Biodiversity loss, climate crisis, and nitrogen cycle',
                                 'Biodiversity loss, climate crisis, and nitrogen cycle')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('They are two independent imbalances that operate independently',
                                 'They are two independent imbalances that operate independently'),
                                ('They are two interdependent imbalances that reinforce each other',
                                 'They are two interdependent imbalances that reinforce each other')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'The cost of carbon in 2030 will be $75 per tonne of carbon dioxide in 2017 US dollars',
                                'The cost of carbon in 2030 will be $75 per tonne of carbon dioxide in 2017 US dollars'),
                                ('The cost of carbon in 2030 will be $50 per tonne of carbon dioxide in 2017 US dollars',
                                 'The cost of carbon in 2030 will be $50 per tonne of carbon dioxide in 2017 US dollars'),
                                ('The cost of carbon in 2030 will be $85 per tonne of carbon dioxide in 2017 US dollars',
                                 'The cost of carbon in 2030 will be $85 per tonne of carbon dioxide in 2017 US dollars')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'Multiplying the HDI by the social cost of carbon emissions',
                                'Multiplying the HDI by the social cost of carbon emissions'),
                                ('Multiplying the HDI by the ecological footprint',
                                 'Multiplying the HDI by the ecological footprint'),
                                ('Multiplying the HDI by the arithmetic mean of carbon emissions and the ecological footprint',
                                 'Multiplying the HDI by the arithmetic mean of carbon emissions and the ecological footprint')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'The PHDI in country B is larger','The PHDI in country B is larger'),
                                ('The PHDI in country A is larger','The PHDI in country A is larger'),
                                ('The PHDI does not depend on carbon emissions', 'The PHDI does not depend on carbon emissions')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch3_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                'It is increasing the gap with the HDI','It is increasing the gap with the HDI'),
                                ('It is closing the gap with the HDI','It is closing the gap with the HDI'),
                                ('The gap between both indexes remains the same', 'The gap between both indexes remains the same')])
    submit = SubmitField('Submit')

#M2_Ch4: SE. Ch4. Global Energy Transformation. A road map to 2050
class ModulsForm_m2_ch4_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Electric vehicles, introduction of renewable energy, and energy efficiency',
                                 'Electric vehicles, introduction of renewable energy, and energy efficiency'),
                                ('Electrification, introduction of renewable energy, and energy efficiency',
                                 'Electrification, introduction of renewable energy, and energy efficiency'),
                                ('Auto-consumption, biomass, and energy efficiency',
                                 'Auto-consumption, biomass, and energy efficiency')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Agricultural sector, car sector, steel sector and building sector',
                                 'Agricultural sector, car sector, steel sector and building sector'),
                                ('Power sector, car sector, chemical sector and building sector',
                                 'Power sector, car sector, chemical sector and building sector'),
                                ('Power sector, industry sector, transport sector and building sector',
                                 'Power sector, industry sector, transport sector and building sector')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch4_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Electric vehicles, introduction of renewable energy, and energy efficiency', 'Electric vehicles, introduction of renewable energy, and energy efficiency'),
                                ('Electrification, introduction of renewable energy, and energy efficiency', 'Electrification, introduction of renewable energy, and energy efficiency'),
                                ('Auto-consumption, biomass, and energy efficiency', 'Auto-consumption, biomass, and energy efficiency')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Agricultural sector, car sector, steel sector and building sector',
                                 'Agricultural sector, car sector, steel sector and building sector'),
                                ('Power sector, car sector, chemical sector and building sector',
                                 'Power sector, car sector, chemical sector and building sector'),
                                ('Power sector, industry sector, transport sector and building sector',
                                 'Power sector, industry sector, transport sector and building sector')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The 66% of the electricity will be produced by using renewable energy',
                                'The 66% of the electricity will be produced by using renewable energy'),
                                ('The 76% of the electricity will be produced by using renewable energy',
                                 'The 76% of the electricity will be produced by using renewable energy'),
                                ('The 86% of the electricity will be produced by using renewable energy',
                                 'The 86% of the electricity will be produced by using renewable energy')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('20% in the building sector, 33% in the industry sector, 22% in the transport sector',
                                '20% in the building sector, 33% in the industry sector, 22% in the transport sector'),
                                ('40% in the building sector, 33% in the industry sector, 22% in the transport sector',
                                 '40% in the building sector, 33% in the industry sector, 22% in the transport sector'),
                                ('20% in the building sector, 33% in the industry sector, 12% in the transport sector',
                                 '20% in the building sector, 33% in the industry sector, 12% in the transport sector')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Solar, wind, hydrogen and hydropower',
                                 'Solar, wind, hydrogen and hydropower'),
                                ('Solar, wind, bioenergy and hydropower',
                                 'Solar, wind, bioenergy and hydropower'),
                                ('Solar, wind, bioenergy and nuclear',
                                 'Solar, wind, bioenergy and nuclear')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[(
                                '1, Electric vehicles (EV); 2, biofuels heavy freight, for road, aviation and marine transport',
                                '1, Electric vehicles (EV); 2, biofuels heavy freight, for road, aviation and marine transport'),
                                ('1, Hydrogen for vehicles, and heavy freight; 2, biofuels for road, aviation and marine transport',
                                 '1, Hydrogen for vehicles, and heavy freight; 2, biofuels for road, aviation and marine transport'),
                                ('1, EV; 2, hydrogen for heavy freight; 3, biofuels for road, aviation and marine transport',
                                 '1, EV; 2, hydrogen for heavy freight; 3, biofuels for road, aviation and marine transport')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Bioenergy for industrial heat and processes',
                                'Bioenergy for industrial heat and processes'),
                                ('Hydrogen and direct use of electricity for industrial heat and processes',
                                 'Hydrogen and direct use of electricity for industrial heat and processes'),
                                ('Gas for industrial heat and processes',
                                 'Gas for industrial heat and processes')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Renewables for heating, and electricity; biogas for cooking; increase in efficiency','Renewables for heating, and electricity; biogas for cooking; increase in efficiency'),
                                ('Renewables for electricity; biogas for heating and cooking; smart meters','Renewables for electricity; biogas for heating and cooking; smart meters'),
                                ('Renewables for heating and electricity; smart meters', 'Renewables for heating and electricity; smart meters')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Electrification, and renewables','Electrification, and renewables'),
                                ('Investment, consumer expenditure, and trade','Investment, consumer expenditure, and trade'),
                                ('Digitalization and electric vehicles (EV)', 'Digitalization and electric vehicles (EV)')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch4_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Around 10% for a 2°C global warming and 15% for a 5°C global warming','Around 10% for a 2°C global warming and 15% for a 5°C global warming'),
                                ('Around 5% for a 2°C global warming and 20% for a 5°C global warming','Around 5% for a 2°C global warming and 20% for a 5°C global warming'),
                                ('Around 20% for a 2°C global warming and 35% for a 5°C global warming', 'Around 20% for a 2°C global warming and 35% for a 5°C global warming')])
    submit = SubmitField('Submit')

#M2_Ch5: SE. Ch5. Sustainable Energy. Wind Energy
class ModulsForm_m2_ch5_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('To minimize the weight of the turbine', 'To minimize the weight of the turbine'),
                                ('To cover as much surface as possible and simultaneously minimize the cost of production', 'To cover as much surface as possible and simultaneously minimize the cost of production'),
                                ('To cover as much surface as possible maximizing energy production', 'To cover as much surface as possible maximizing energy production')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('30%', '30%'),
                                ('35%', '35%'),
                                ('40%', '40%')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch5_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Mass of wind that pass through an area A divided by the square of wind speed', 'Mass of wind that pass through an area A divided by the square of wind speed'),
                                ('Mass of wind that pass through an area A multiplied by the square of wind speed', 'Mass of wind that pass through an area A multiplied by the square of wind speed'),
                                ('Mass of wind that pass through an area A multiplied by the wind speed', 'Mass of wind that pass through an area A multiplied by the wind speed')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Measures possible production', 'Measures possible production'),
                                ('Measures actual production', 'Measures actual production'),
                                ('Measures actual production relative to possible production', 'Measures actual production relative to possible production')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('45%', '45%'),
                                ('40%', '40%'),
                                ('50%', '50%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('49.3%', '49.3%'),
                                ('59.3%', '59.3%'),
                                ('51.3%', '51.3%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('30%', '30%'),
                                ('35%', '35%'),
                                ('40%', '40%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('8844 GW, 1000 GW', '8844 GW, 1000 GW'),
                                ('9944 GW, 900 GW', '9944 GW, 900 GW'),
                                ('5044 GW, 1000 GW', '5044 GW, 1000 GW')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('150 GW/yr, 25 GW/yr', '150 GW/yr, 25 GW/yr'),
                                ('200 GW/yr, 45 GW/yr', '200 GW/yr, 45 GW/yr'),
                                ('250 GW/yr, 40 GW/yr', '250 GW/yr, 40 GW/yr')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('400-600 USD/KW, 1000-2000 USD/KW', '400-600 USD/KW, 1000-2000 USD/KW'),
                                ('650-1000 USD/KW, 1400-2800 USD/KW', '650-1000 USD/KW, 1400-2800 USD/KW'),
                                ('200-400 USD/KW, 900-1800 USD/KW', '200-400 USD/KW, 900-1800 USD/KW')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.02-0.03 USD/KWh, 0.03-0.07 USD/KWh', '0.02-0.03 USD/KWh, 0.03-0.07 USD/KWh'),
                                ('0.05-0.07 USD/KWh, 0.08-0.1 USD/KWh', '0.05-0.07 USD/KWh, 0.08-0.1 USD/KWh'),
                                ('0.07-0.09 USD/KWh, 0.11-0.13 USD/KWh', '0.07-0.09 USD/KWh, 0.11-0.13 USD/KWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.07USD/KWh', '0.07 USD/KWh'),
                                ('0.09 USD/KWh', '0.09 USD/KWh'),
                                ('0.12 USD/KWh', '0.12 USD/KWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q11(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('22%-38%, 33%-40%', '22%-38%, 33%-40%'),
                                ('32%-58%, 43%-60%', '32%-58%, 43%-60%'),
                                ('15%-30%, 23%-33%', '15%-30%, 23%-33%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch5_q12(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('6.06 M', '6.06 M'),
                                ('5.06 M', '4.06 M'),
                                ('4.06 M', '4.06 M')])
    submit = SubmitField('Submit')

#M2_Ch6: SE. Ch6. Sustainable Energy. Solar Energy
class ModulsForm_m2_ch6_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('25%', '25%'),
                                ('35%', '35%'),
                                ('30%', '30%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('From 0.37 USD/KWh to 0.085 USD/KWh', 'From 0.37 USD/KWh to 0.085 USD/KWh'),
                                ('From 0.12 USD/KWh to 0.09 USD/KWh', 'From 0.12 USD/KWh to 0.09 USD/KWh'),
                                ('From 0.17 USD/KWh to 0.095 USD/KWh', 'From 0.17 USD/KWh to 0.095 USD/KWh')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch6_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The cost has dropped from 0.5 $/KWh to 0.1-0.2 $/KWh', 'The cost has dropped from 0.5 $/KWh to 0.1-0.2 $/KWh'),
                                ('The cost has dropped from 0.5 $/KWh to 0.01-0.02 $/KWh', 'The cost has dropped from 0.5 $/KWh to 0.01-0.02 $/KWh'),
                                ('The cost has dropped from 0.5 $/KWh to 0.3-0.4 $/KWh', 'The cost has dropped from 0.5 $/KWh to 0.3-0.4 $/KWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The cost has dropped from 1160 $/KWh to 576 $/KWh', 'The cost has dropped from 1160 $/KWh to 576 $/KWh'),
                                ('The cost has dropped from 1160 $/KWh to 476 $/KWh', 'The cost has dropped from 1160 $/KWh to 476 $/KWh'),
                                ('The cost has dropped from 1160 $/KWh to 176 $/KWh', 'The cost has dropped from 1160 $/KWh to 176 $/KWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Non-concentrating collectors at home, while concentrating collectors in power plants', 'Non-concentrating collectors at home, while concentrating collectors in power plants'),
                                ('Both are mainly used at home', 'Both are mainly used at home'),
                                ('Both are mainly used in power plants', 'Both are mainly used in power plants')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('CSP is mainly used in the industry, while CST is mainly used in generation', 'CSP is mainly used in the industry, while CST is mainly used in generation'),
                                ('CST is mainly used in the industry, while CSP is mainly used in generation', 'CST is mainly used in the industry, while CSP is mainly used in generation'),
                                ('Both are mainly used in the industry', 'Both are mainly used in the industry')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.26', '0.26'),
                                ('0.36', '0.36'),
                                ('0.46', '0.46')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.1', '0.1'),
                                ('0.03', '0.03'),
                                ('0.15', '0.15')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Making the N-layer thick and heavily doped, and making the P-layer thick and heavily doped', 'Making the N-layer thick and heavily doped, and making the P-layer thick and heavily doped'),
                                ('Making the N-layer thin and heavily doped, and making the P-layer thick and heavily doped', 'Making the N-layer thin and heavily doped, and making the P-layer thick and heavily doped'),
                                ('Making the N-layer thin and heavily doped, and making the P-layer thick and poorly doped', 'Making the N-layer thin and heavily doped, and making the P-layer thick and poorly doped')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The combination of Amps and Ohms that maximize Watts', 'The combination of Amps and Ohms that maximize Watts'),
                                ('The combination of Amps and Volts that maximize Watts', 'The combination of Amps and Volts that maximize Watts'),
                                ('The combination of Ohms and Volts that maximize Watts', 'The combination of Ohms and Volts that maximize Watts')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('7000 GW', '7000 GW'),
                                ('7500 GW', '7500 GW'),
                                ('8500 GW', '8500 GW')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Asia 3000 GW, North-America 1300 GW, Europe 1200 GW, Africa 1000 GW', 'Asia 3000 GW, North-America 1300 GW, Europe 1200 GW, Africa 1000 GW'),
                                ('Asia 4800 GW, North-America 1720 GW, Europe 890 GW, Africa 670 GW', 'Asia 4800 GW, North-America 1720 GW, Europe 890 GW, Africa 670 GW'),
                                ('Asia 3500 GW, North-America 100 GW, Europe 1200 GW, Africa 1500 GW', 'Asia 3500 GW, North-America 100 GW, Europe 1200 GW, Africa 1500 GW')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q11(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('From 4621 USD/KW in 2010 to 481-165 USD/KW in 2050', 'From 4621 USD/KW in 2010 to 481-165 USD/KW in 2050'),
                                ('From 3000 USD/KW in 2010 to 1050-850 USD/KW in 2050', 'From 3000 USD/KW in 2010 to 1050-850 USD/KW in 2050'),
                                ('From 3500 USD/KW in 2010 to 1100-900 USD/KW in 2050', 'From 3500 USD/KW in 2010 to 1100-900 USD/KW in 2050')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch6_q12(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('0.12 Euros/KWh', '0.12 Euros/KWh'),
                                ('0.16 Euros/KWh', '0.16 Euros/KWh'),
                                ('0.1 Euros/KWh', '0.1 Euros/KWh')])
    submit = SubmitField('Submit')

#M2_Ch6: SE. Ch7. Sustainable Energy. Hydrogen
class ModulsForm_m2_ch7_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Cost of electrolysers, and cost of electricity', 'Cost of electrolysers, and cost of electricity'),
                                ('Cost of electrolysers and storage cost', 'Cost of electrolysers and storage cost'),
                                ('Cost of electricity and transport cost', 'Cost of electricity and transport cost')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Heavy industry and transport sector', 'Heavy industry and transport sector'),
                                ('Heavy industry and building sector', 'Heavy industry and building sector'),
                                ('Building sector and energy sector', 'Building sector and energy sector')])
    submit = SubmitField('Submit')



class ModulsForm_m2_ch7_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('China + Japan', 'China + Japan'),
                                ('Indonesia + UK', 'Indonesia + UK'),
                                ('Senegal + Morocco', 'Senegal + Morocco')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Higher energy efficiency from production to final use', 'Higher energy efficiency from production to final use'),
                                ('Lower production cost', 'Lower production cost'),
                                ('Lower time to charge, and lower fuel storage requirements', 'Lower time to charge, and lower fuel storage requirements')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The electrons does not move since H2 and O2 have already a neutral charge', 'The electrons does not move since H2 and O2 have already a neutral charge'),
                                ('The electrons go out of the water, and the O2 is produced by a oxidation process', 'The electrons go out of the water, and the O2 is produced by a oxidation process'),
                                ('The electrons go into the water, and the H2 is produced by a reduction process', 'The electrons go into the water, and the H2 is produced by a reduction process')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Gaining two electrons', 'Gaining two electrons'),
                                ('Lossing two electrons', 'Lossing two electrons'),
                                ('The oxidation process of the oxygen is not necessary', 'The oxidation process of the oxygen is not necessary')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Cell, transport, and pressure devices', 'Cell, transport, and pressure devices'),
                                ('Cell, stack, and system level', 'Cell, stack, and system level'),
                                ('Electric system, transport, and pressure devices', 'Electric system, transport, and pressure devices')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Electricity cost, compression cost, and transport cost', 'Electricity cost, compression cost, and transport cost'),
                                ('Efficiency, electricity cost, compression cost', 'Efficiency, electricity cost, compression cost'),
                                ('Efficiency, current of the stack, durability, and investment cost', 'Efficiency, current of the stack, durability, and investment cost')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('70% reduction electrolyser cost, electricity cost from 53 USD/MWh to 40 USD/MWh', '70% reduction electrolyser cost, electricity cost from 53 USD/MWh to 40 USD/MWh'),
                                ('80% reduction electrolyser cost, electricity cost from 53 USD/MWh to 20 USD/MWh', '80% reduction electrolyser cost, electricity cost from 53 USD/MWh to 20 USD/MWh'),
                                ('60% reduction electrolyser cost, electricity cost from 53 USD/MWh to 30 USD/MWh', '60% reduction electrolyser cost, electricity cost from 53 USD/MWh to 30 USD/MWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('30 USD/MWh', '30 USD/MWh'),
                                ('40 USD/MWh', '40 USD/MWh'),
                                ('45 USD/MWh', '45 USD/MWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Batteries in the transport sector, and efficiency in the building sector', 'Batteries in the transport sector, and efficiency in the building sector'),
                                ('Bionergy in the transport sector and CCS in industry sector', 'Bionergy in the transport sector and CCS in industry sector'),
                                ('Batteries in planes, and bioenergy in the industry sector', 'Batteries in planes, and bioenergy in the industry sector')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Hydrogen used as a chemical, and in heavy industry', 'Hydrogen used as a chemical, and in heavy industry'),
                                ('Hydrogen used in marine transport, and in heavy industry', 'Hydrogen used in marine transport, and in heavy industry'),
                                ('Hydrogen can be used as an energy carrier, in fuel cells, and as a chemical', 'Hydrogen can be used as an energy carrier, in fuel cells, and as a chemical')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q11(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Supply of electricity, demand of hydrogen, and flexibility of the electrolyser', 'Supply of electricity, demand of hydrogen, and flexibility of the electrolyser'),
                                ('Seasonality of wind and solar', 'Seasonality of wind and solar'),
                                ('Start up and shut down time of the electrolyser', 'Start up and shut down time of the electrolyser')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch7_q12(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Flexibility services provided by the electrolyser', 'Flexibility services provided by the electrolyser'),
                                ('Technology employed in the electrolyser stack', 'Technology employed in the electrolyser stack'),
                                ('Seasonality of renewable energy production (mainly solar and wind)', 'Seasonality of renewable energy production (mainly solar and wind)')])
    submit = SubmitField('Submit')

#M2_Ch8: SE. Ch8. Sustainable Energy. Bioenergy
class ModulsForm_m2_ch8_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Only in the gasification process', 'Only in the gasification process'),
                                ('Only in the anaerobic digestion process', 'Only in the anaerobic digestion process'),
                                ('In both processes', 'In both processes')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('4%', '4%'),
                                ('14%', '14%'),
                                ('24%', '24%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_e3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('10%', '10%'),
                                ('20%', '20%'),
                                ('30%', '30%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_e4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('7%', '7%'),
                                ('14%', '14%'),
                                ('21%', '21%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The reduction in methane emissions', 'The reduction in methane emissions'),
                                ('The reduction of plastic in the nature', 'The reduction of plastic in the nature'),
                                ('The recycling of residues', 'The recycling of residues')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Heating in buildings', 'Heating in buildings'),
                                ('Incineration, and gasification to obtain biodiesel and hydrogen', 'Incineration, and gasification to obtain biodiesel and hydrogen'),
                                ('Compost to be used in agriculture', 'Compost to be used in agriculture')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Selling the waste to be recycled', 'Selling the waste to be recycled'),
                                ('Downstream by taking the waste; upstream, by producing high-value products', 'Downstream by taking the waste; upstream, by producing high-value products'),
                                ('Collecting the waste and selling it', 'Collecting the waste and selling it')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('32.3%', '32.3%'),
                                ('28.2%', '28.2%'),
                                ('21.6%', '21.6%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('As a residual of the gasification process', 'As a residual of the gasification process'),
                                ('In the methane-reforming process', 'In the methane-reforming process'),
                                ('In the water-gas-shift process', 'In the water-gas-shift process')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('In the cleaning and upgrading process', 'In the cleaning and upgrading process'),
                                ('In the hydrolysis process', 'In the hydrolysis process'),
                                ('In the acidogenesis process', 'In the acidogenesis process')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Providing heat to warm the factories', 'Providing heat to warm the factories'),
                                ('Providing heat used in the chemical and manufacturing processes', 'Providing heat used in the chemical and manufacturing processes'),
                                ('Providing electricity to light the factories', 'Providing electricity to light the factories')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Trucks and agricultural transport', 'Trucks and agricultural transport'),
                                ('Trucks and aviation', 'Trucks and aviation'),
                                ('Aviation and marine transport', 'Aviation and marine transport')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('In biomass gasification processes with carbon capture storage', 'In biomass gasification processes with carbon capture storage'),
                                ('In combined heat and power systems', 'In combined heat and power systems')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('4%', '4%'),
                                ('16%', '16%'),
                                ('24%', '24%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q11(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('10%', '10%'),
                                ('20%', '20%'),
                                ('30%', '30%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch8_q12(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('14%', '14%'),
                                ('7%', '7%'),
                                ('21%', '21%')])
    submit = SubmitField('Submit')

#M2_Ch9: SE. Ch9. Sustainable Energy. Batteries and EV
class ModulsForm_m2_ch9_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('75%', '75%'),
                                ('80%', '80%'),
                                ('95%', '95%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('25%', '25%'),
                                ('30%', '30%'),
                                ('10%', '10%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_e3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('5 TWh', '5 TWh'),
                                ('8 TWh', '8 TWh'),
                                ('14 TWh', '14 TWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_e4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('5%', '5%'),
                                ('8%', '8%'),
                                ('19%', '19%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Charging at home, battery expectancy', 'Charging at home, battery expectancy'),
                                ('Battery life expectancy, charging stations, autonomy (kilometers without charging the battery)', 'Battery life expectancy, charging stations, autonomy (kilometers without charging the battery)'),
                                ('Fast chargers, Autonomy (kilometers without charging the battery)', 'Fast chargers, EV autonomy (kilometers without charging the battery)')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Levels 1 and 2: 2-20 miles per hour; level 3: 60-80 miles in 20 minutes', 'Levels 1 and 2: 2-20 miles per hour; level 3: 60-80 miles in 20 minutes'),
                                ('Levels 1 and 2: 20-40 miles per hour; level 3: 80-100 miles in 20 minutes', 'Levels 1 and 2: 20-40 miles per hour; level 3: 80-100 miles in 20 minutes'),
                                ('Levels 1 and 2: 30-50 miles per hour; level 3: 100-120 miles in 20 minutes', 'Levels 1 and 2: 30-50 miles per hour; level 3: 100-120 miles in 20 minutes')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('BMW', 'BMW'),
                                ('General Motors', 'General Motors'),
                                ('Tesla', 'Tesla')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The zinc bar becomes thicker', 'The zinc bar becomes thicker'),
                                ('The zinc bar becomes thinner', 'The zinc bar becomes thinner'),
                                ('It does not change', 'It does not change')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The cooper bar becomes thicker', 'The cooper bar becomes thicker'),
                                ('The cooper bar becomes thinner', 'The cooper bar becomes thinner'),
                                ('It changes very little', 'It changes very little')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Keep the charge in the zinc-sulfate and the copper-sulfate neutral to keep electrons moving', 'Keep the charge in the zinc-sulfate and the copper-sulfate neutral to keep electrons moving'),
                                ('The electrons move between containers through the salt bridge', 'The electrons move between containers through the salt bridge'),
                                ('The zinc and cooper move between containers through the salt bridge', 'The zinc and cooper move between containers through the salt bridge')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('85% of the time the cars are parked', '85% of the time the cars are parked'),
                                ('60% of the time the cars are parked', '60% of the time the cars are parked'),
                                ('50% of the time the cars are parked', '50% of the time the cars are parked')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('5TWh', '5TWh'),
                                ('7TWh', '7TWh'),
                                ('14TWh', '14TWh')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The energy needs of EVs represent no more than 2% to 5% of total electricity production', 'The energy needs of EVs represent no more than 2% to 5% of total electricity production'),
                                ('The energy needs of EVs represent no more than 10% to 15% of total electricity production', 'The energy needs of EVs represent no more than 10% to 15% of total electricity production'),
                                ('The energy needs of EVs represent no more than 5% to 7% of total electricity production', 'The energy needs of EVs represent no more than 5% to 7% of total electricity production')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The peak demand would increase by 19%', 'The peak demand would increase by 19%'),
                                ('The peak demand would increase by 5%', 'The peak demand would increase by 5%'),
                                ('The peak demand would increase by 8%', 'The peak demand would increase by 8%')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q11(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Tariff regulation, and market design changes as real time pricing', 'Tariff regulation, and market design changes as real time pricing'),
                                ('Demand response policies as smart buildings', 'Demand response policies as smart buildings'),
                                ('All the enumerated measures', 'All the enumerated measures')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch9_q12(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Unidirectional V1G, Virtual Power Plant, and vehicle grid integration', 'Unidirectional V1G, Virtual Power Plant, and vehicle grid integration'),
                                ('V2G, second-life batteries, and smart buildings "as-a-service"', 'V2G, second-life batteries, and smart buildings "as-a-service"'),
                                ('Unidirectional V1G, V2G and second-life batteries', 'Unidirectional V1G, V2G and second-life batteries')])
    submit = SubmitField('Submit')

#M2_Ch10: SE. Ch10. Sustainable Energy. Carbon Capture Storage
class ModulsForm_m2_ch10_e1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Production of synthetic fuels by combining CO2 and hydrogen', 'Production of synthetic fuels by combining CO2 and hydrogen'),
                                ('BECCS (bioenergy with carbon capture and storage)', 'BECCS (bioenergy with carbon capture and storage)'),
                                ('Steel production with CCS', 'Steel production with CCS')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_e2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Capture', 'Capture'),
                                ('Transport', 'Transport'),
                                ('Storage', 'Storage')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_e3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('100 Dollars/Tonne', '100 Dollars/Tonne'),
                                ('200 Dollars/Tonne', '200 Dollars/Tonne'),
                                ('50 Dollars/Tonne', '50 Dollars/Tonne')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_e4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Transport and Industry', 'Transport and Industry'),
                                ('Power and building', 'Power and building'),
                                ('Building and agriculture', 'Building and agriculture')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q1(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Direct carbon capture technologies are 50 times more expensive',
                                 'Direct carbon capture technologies are 50 times more expensive'),
                                ('Direct carbon capture technologies are 30 times more expensive',
                                 'Direct carbon capture technologies are 30 times more expensive'),
                                ('Direct carbon capture technologies are 20 times more expensive',
                                 'Direct carbon capture technologies are 20 times more expensive')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q2(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Carbon capture and utilization', 'Carbon capture and utilization'),
                                ('Carbon capture storage and sell that storage as a carbon emission right',
                                 'Carbon capture storage and sell that storage as a carbon emission right'),
                                ('Enhanced oil recovery (EOR)', 'Enhanced oil recovery (EOR)')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q3(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('50-150 Dollars/Tonne', '50-150 Dollars/Tonne'),
                                ('300-800 Dollars/Tonne', '300-800 Dollars/Tonne'),
                                ('100-150 Dollars/Tonne', '100-150 Dollars/Tonne')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q4(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('A Carbon Capture and Storage technology (CCS)', 'A Carbon Capture and Storage technology (CCS)'),
                                ('A Carbon Dioxide Removal technology (CDR)', 'A Carbon Dioxide Removal technology (CDR)'),
                                ('A Carbon Capture and Utilisation technology (CCU)', 'A Carbon Capture and Utilisation technology (CCU)')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q5(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('A CCS technology',
                                 'A CCS technology'),
                                ('A CDR technology',
                                 'A CDR technology'),
                                ('A CCU technology',
                                 'A CCU technology')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q6(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Mainly, a Carbon Capture and Storage technology (CCS)',
                                 'Mainly, a Carbon Capture and Storage technology (CCS)'),
                                ('Mainly, a Carbon Dioxide Removal technology (CDR)',
                                 'Mainly, a Carbon Dioxide Removal technology (CDR)'),
                                ('Both classifications could be possible',
                                 'Both classifications could be possible')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q7(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The estimated cost of CCS in the iron and steel industry are USD 50-62/tCO2', 'The estimated cost of CCS in the iron and steel industry are USD 50-62/tCO2'),
                                ('The estimated cost of CCS in the iron and steel industry are USD 41-50/tCO2', 'The estimated cost of CCS in the iron and steel industry are USD 41-50/tCO2'),
                                ('The estimated cost of CCS in the iron and steel industry are USD 75–131/tCO2', 'The estimated cost of CCS in the iron and steel industry are USD 75–131/tCO2')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q8(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The estimated cost of CCS in the cement industry are USD 81-90/tCO2', 'The estimated cost of CCS in the cement industry are USD 81-90/tCO2'),
                                ('The estimated cost of CCS in the cement industry are USD 62–102/tCO2', 'The estimated cost of CCS in the cement industry are USD 62–102/tCO2'),
                                ('The estimated cost of CCS in the cement industry are USD 88-97/tCO2', 'The estimated cost of CCS in the cement industry are USD 88-97/tCO2')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q9(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('The estimated costs of bioenergy with carbon capture and storage are USD 71–80/tCO2', 'The estimated costs of bioenergy with carbon capture and storage are USD 71–80/tCO2'),
                                ('The estimated costs of bioenergy with carbon capture and storage are USD 69–105/tCO2', 'The estimated costs of bioenergy with carbon capture and storage are USD 69–105/tCO2'),
                                ('The estimated costs of bioenergy with carbon capture and storage are USD 51–62/tCO2', 'The estimated costs of bioenergy with carbon capture and storage are USD 51–62/tCO2')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q10(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('CCS in the industry sector must reach 1 Gtpa by 2050', 'CCS in the industry sector must reach 1 Gtpa by 2050'),
                                ('CCS in the industry sector must reach 3.4 Gtpa by 2050', 'CCS in the industry sector must reach 3.4 Gtpa by 2050'),
                                ('CCS in the industry sector must reach 0.6 Gtpa by 2050', 'CCS in the industry sector must reach 0.6 Gtpa by 2050')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q11(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Bioenergy with CCS must reach 4.5 Gtpa by 2050', 'Bioenergy with CCS must reach 4.5 Gtpa by 2050'),
                                ('Bioenergy with CCS must reach 3.2 Gtpa by 2050', 'Bioenergy with CCS must reach 3.2 Gtpa by 2050'),
                                ('Bioenergy with CCS must reach 1.8 Gtpa by 2050', 'Bioenergy with CCS must reach 1.8 Gtpa by 2050')])
    submit = SubmitField('Submit')

class ModulsForm_m2_ch10_q12(FlaskForm):
    type = SelectField('Type', validators=[DataRequired()],
                       choices=[('Iron and synthetic fuels', 'Iron and synthetic fuels'),
                                ('Cement, chemical, steel sectors and blue hydrogen', 'Cement, chemical, steel sectors and blue hydrogen'),
                                ('Cement and steel', 'Cement and steel')])
    submit = SubmitField('Submit')
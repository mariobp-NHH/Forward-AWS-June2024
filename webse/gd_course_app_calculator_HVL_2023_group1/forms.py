from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import  SubmitField,  SelectField,  FloatField
from wtforms.validators import InputRequired


###############################
###   App Calculator form   ###
###############################
class AddRecordForm(FlaskForm):
    kms = FloatField("Kilometers", [InputRequired()])
    transport_type = SelectField("Type of Transport",
                                 [InputRequired()],
                                 choices=[
                                     ('Bus', 'Bus'),
                                     ('Car', 'Car'),
                                     ('Plane', 'Plane'),
                                     ('Ferry', 'Ferry'),
                                     ('Scooter', 'Scooter'),
                                     ('Bicycle', 'Bicycle'),
                                     ('Motorbike', "Motorbike"),
                                     ('Walk', 'Walk')
                                 ])

    fuel_type = SelectField("Fuel Type",
                            validators=[InputRequired()], choices=[])
    submit = SubmitField("Submit")
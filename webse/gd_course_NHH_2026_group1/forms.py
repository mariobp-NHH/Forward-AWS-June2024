from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webse.models import User
from wtforms import StringField, FloatField, SelectField, SubmitField, DateField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

from webse.gd_course_NHH_2026_group1.emission_factors import EMISSION_FACTORS_CO2

# Skjema for registrering
class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=2, max=30)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')

    # Egen validator for brukernavn, slik at vi får en pen og tydelig feilmelding
    # hvis brukernavnet allerede finnes i databasen.
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    # Egen validator for e-post av samme grunn som over.
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


# Skjema for innlogging
class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()]
    )
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RouteForm(FlaskForm):
    name = StringField('Route Name', validators=[DataRequired(), Length(min=2, max=80)])
    origin = StringField('Origin', validators=[DataRequired(), Length(min=1, max=60)])
    destination = StringField('Destination', validators=[DataRequired(), Length(min=1, max=60)])
    transport_type = SelectField(
        'Transport Type',
        choices=[('Road', 'Road'), ('Sea', 'Sea'), ('Air', 'Air')],
        validators=[DataRequired()]
    )
    # Verdiene må matche undernøklene i EMISSION_FACTORS_CO2 i emission_factors.py (GLEC Framework v3.2).
    subcategory = SelectField(
        'Subcategory',
        choices=[
            ('small',  'Small truck (3.5–7.5 t)'),
            ('medium', 'Medium truck (7.5–20 t)'),
            ('large',  'Large truck (20–40 t)'),
            ('general_cargo_small', 'General cargo, small (≤ 9 999 dwt)'),
            ('general_cargo_large', 'General cargo, large (≥ 10 000 dwt)'),
            ('bulk_carrier_small',  'Bulk carrier, small (≤ 34 999 dwt)'),
            ('bulk_carrier_large',  'Bulk carrier, large (≥ 35 000 dwt)'),
            ('short_haul', 'Short-haul flight (< 1 500 km)'),
            ('long_haul',  'Long-haul flight (≥ 1 500 km)'),
        ],
        validators=[DataRequired()]
    )
    distance_km = FloatField(
        'Distance (km)',
        validators=[DataRequired(), NumberRange(min=1, max=20000, message='Distance must be between 1 and 20,000 km.')]
    )
    submit = SubmitField('Add Route')

    def validate_subcategory(self, subcategory):
        # Sørger for at valgt subcategory passer til valgt transport_type
        # (f.eks. 'short_sea' kan ikke velges sammen med 'Road').
        # Nøklene her må holdes i sync med EMISSION_FACTORS_CO2-strukturen i emission_factors.py.
        valid_combinations = {
            'Road': {'small', 'medium', 'large'},
            'Sea':  {'general_cargo_small', 'general_cargo_large',
                     'bulk_carrier_small',  'bulk_carrier_large'},
            'Air':  {'short_haul', 'long_haul'},
        }
        #Sjekker om transport typen samsvarer med subcategory
        transport = self.transport_type.data
        if transport in valid_combinations:
            if subcategory.data not in valid_combinations[transport]:
                raise ValidationError(
                    f'Selected subcategory is not valid for {transport} transport. '
                    f'Please pick a {transport}-compatible subcategory.'
                )


class ShipmentForm(FlaskForm):
    route_id = SelectField('Route', coerce=int, validators=[DataRequired()])
    cargo_tonnes = FloatField(
        'Cargo (tonnes)',
        validators=[DataRequired(), NumberRange(min=0.01, max=100000, message='Cargo must be between 0.01 and 100,000 tonnes.')]
    )
    shipped_at = DateField('Shipment Date', validators=[DataRequired()], format='%Y-%m-%d')
    # Unionen av fuel types på tvers av modi. Gyldigheten mot valgt rute sjekkes
    # i validate_fuel_type basert på EMISSION_FACTORS_CO2.
    fuel_type = SelectField(
        'Fuel Type',
        choices=[
            ('Diesel',    'Diesel'),
            ('CNG',       'CNG'),
            ('LNG',       'LNG'),
            ('HFO',       'HFO'),
            ('VLSFO',     'VLSFO'),
            ('MDO',       'MDO'),
            ('Jet A/A-1', 'Jet A/A-1'),
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Log Shipment')

    def validate_fuel_type(self, fuel_type):
        # Unngår KeyError i calculate_co2_kg ved å avvise fuel-typer som ikke
        # finnes for valgt rutes transport_type + subcategory.
        from webse.models import Route_NHH_2026_g1
        route = Route_NHH_2026_g1.query.get(self.route_id.data) if self.route_id.data else None
        if route is None:
            return
        allowed = EMISSION_FACTORS_CO2.get(route.transport_type, {}) \
                                      .get(route.subcategory, {})
        if fuel_type.data not in allowed:
            raise ValidationError(
                f'Selected fuel type is not valid for {route.transport_type} transport. '
                f'Please pick a {route.transport_type}-compatible fuel type.'
            )

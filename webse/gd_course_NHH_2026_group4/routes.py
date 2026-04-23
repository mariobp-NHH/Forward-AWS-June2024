from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_NHH_2026_group4.forms import RegistrationForm, LoginForm
from webse.models import User, EmissionsGD
from webse import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from flask import render_template, Blueprint, request, redirect, url_for, flash
from datetime import timedelta, datetime
from webse.gd_course_NHH_2026_group4.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm, TrainForm
from webse.gd_course_NHH_2026_group4.functions import carbon_emmissions
import json

gd_course_NHH_2026_group4=Blueprint('gd_course_NHH_2026_group4',__name__)

@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/home')
def home_home():
  return render_template('gd_course/NHH_2026_group4/home.html', title='Home')

@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/methodology')
def methodology_home():
  return render_template('gd_course/NHH_2026_group4/methodology.html', title='methodology')

@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2026_group4.home_home'))
  if form.validate_on_submit():
      user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2026_group4')
      db.session.add(user)
      db.session.commit()
      # message from flask to show a message to the user after they register --> in home page for example, we have a code to display this message 
      flash('Your account has been created! Now, you are able to login!', 'success')
      return redirect(url_for('gd_course_NHH_2026_group4.login'))
  return render_template('gd_course/NHH_2026_group4/users/register.html', title='register', form=form)

@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2026_group4.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2026_group4.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger') 
  return render_template('gd_course/NHH_2026_group4/users/login.html', title='login', form=form)

@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/logout')
def logout():    
    logout_user()
    return redirect(url_for('gd_course_NHH_2026_group4.home_home'))


# CO2 emissions factor in kg per passenger km
# Sources: 
#   Car, Train, Plane: Framtiden i våre hender / Klimatsmart semester Chalmers (2024)
#   Bus, Ferry, Motorbike: European Environment Agency (EEA)
#   Bicycle, Walk: zero emissions (human-powered)

# CH4 emissions factor in kg per passenger km
# Source: European Environment Agency (EEA)
# Note: CH4 values are negligible (<0.2% of total) but included for completeness

# CO2 emissions factor in kg per passenger km
# Sources: DESNZ (UK Department for Energy Security and Net Zero) + IPCC
efco2 = {
    'Bus':       {'Diesel': 0.030, 'Electric/Hydrogen': 0},
    'Car':       {'Petrol': 0.171, 'Diesel': 0.171, 'Hybrid': 0.110, 'Electric': 0.050},
    'Plane':     {'Economy': 0.127, 'Business Class': 0.284},
    'Train':     {'Electric': 0.007},
    'Ferry':     {'Diesel': 0.186,  'Electric': 0},
    'Motorbike': {'Petrol': 0.09816, 'Electric': 0},
    'Bicycle':   {'No Fossil Fuel': 0},
    'Walk':      {'No Fossil Fuel': 0}
}

# CH4 emissions factor in kg per passenger km
efch4 = {
    'Bus':       {'Diesel': 2e-5, 'Electric/Hydrogen': 0},
    'Car':       {'Petrol': 3.1e-4, 'Diesel': 3e-6, 'Hybrid': 1.5e-4, 'Electric': 0},
    'Plane':     {'Economy': 1.1e-4, 'Business Class': 1.1e-4},
    'Train':     {'Electric': 0},
    'Ferry':     {'Diesel': 3e-5, 'Electric': 0},
    'Motorbike': {'Petrol': 2.1e-3, 'Electric': 0},
    'Bicycle':   {'No Fossil Fuel': 0},
    'Walk':      {'No Fossil Fuel': 0}
}

# Behavioral nudges: shown on each "New Entry" form to prompt reflection
# before the user logs a trip. Each nudge compares the selected mode (positive --> is it good or not --> for the css code to have the desired layout)
# to a greener alternative using values from the emission factors.
nudges = {
    'Bus': {
        'comparison': 'Buses are already among the more efficient motorized options per person. Nice choice!',
        'positive': True
    },
    'Car': {
        'comparison': 'A solo car trip emits roughly <strong>10× more CO₂ per km</strong> than a bus. Could this journey be a bus or train trip? If you must drive, consider carpooling — sharing with 3 others cuts your footprint by 75%.',
        'positive': False
    },
    'Plane': {
        'comparison': 'A flight emits about <strong>18× more CO₂ per km</strong> than a train. For trips under 1,000 km, the train is often nearly as fast when you count airport time.',
        'positive': False
    },
    'Train': {
        'comparison': 'Trains are the greenest motorized option, emitting <strong>9× less CO₂</strong> than a bus and <strong>20× less</strong> than a solo car. Excellent choice!',
        'positive': True
    },
    'Ferry': {
        'comparison': 'Ferries can emit more CO₂ per km than planes per passenger. If a bridge or train route exists for this trip, consider it instead.',
        'positive': False
    },
    'Motorbike': {
        'comparison': 'Motorbikes are more efficient than solo car trips but still emit significantly more than public transport. Consider if a bus or bike could work.',
        'positive': False
    },
    'Bicycle': {
        'comparison': 'Zero emissions, great for your health, and often faster than driving in cities. The best choice on every level!',
        'icon': '🚴',
        'positive': True
    },
    'Walk': {
        'comparison': 'Zero emissions, zero cost, and the healthiest option. Every step matters!',
        'icon': '🚶',
        'positive': True
    }
}

#Carbon app, main page
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app')
@login_required
def carbon_app_home():
    return render_template('gd_course/NHH_2026_group4/carbon_app/carbon_app.html', title='carbon_app')

#New entry bus
@gd_course_NHH_2026_group4.route('/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'

        # Calculate emissions with the function from functions.py, this is to make the code cleaner and more modular, and also allows us to test the function separately from the routes.
        # co2 = carbon_emmissions(kms, transport, fuel)

        # calculate directly in the route, this is to make the code more readable and easier to understand for people who are not familiar with functions and modular code.
        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group4', institution='NHH_2026_group4', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    return render_template('gd_course/NHH_2026_group4/carbon_app/new_entry_bus.html', title='new entry bus', form=form, nudge=nudges['Bus'])

#New entry car
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'

        passengers = form.passengers.data
        co2 = (float(kms) * efco2[transport][fuel]) / passengers
        ch4 = (float(kms) * efch4[transport][fuel]) / passengers
        total = co2 + ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group4', institution='NHH_2026_group4', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    return render_template('gd_course/NHH_2026_group4/carbon_app/new_entry_car.html', title='new entry car', form=form, nudge=nudges['Car'])    

#New entry plane
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group4', institution='NHH_2026_group4', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    return render_template('gd_course/NHH_2026_group4/carbon_app/new_entry_plane.html', title='new entry plane', form=form, nudge=nudges['Plane'])  

# New entry train
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/new_entry_train', methods=['GET', 'POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2 + ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group4', institution='NHH_2026_group4', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    return render_template('gd_course/NHH_2026_group4/carbon_app/new_entry_train.html', title='new entry train', form=form, nudge=nudges['Train'])

#New entry ferry
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group4', institution='NHH_2026_group4', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    return render_template('gd_course/NHH_2026_group4/carbon_app/new_entry_ferry.html', title='new entry ferry', form=form, nudge=nudges['Ferry'])     

#New entry motorbike
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group4', institution='NHH_2026_group4', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    return render_template('gd_course/NHH_2026_group4/carbon_app/new_entry_motorbike.html', title='new entry motorbike', form=form, nudge=nudges['Motorbike']) 

#New entry bicycle
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group4', institution='NHH_2026_group4', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    return render_template('gd_course/NHH_2026_group4/carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form, nudge=nudges['Bicycle'])

#New entry walk
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group4', institution='NHH_2026_group4', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    return render_template('gd_course/NHH_2026_group4/carbon_app/new_entry_walk.html', title='new entry walk', form=form, nudge=nudges['Walk'])


#Your data
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/your_data')
@login_required
def your_data():
    # Table entries
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))). \
        filter(EmissionsGD.institution=='NHH_2026_group4').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()

    # EmissionsGD types in alphabetical order (must match chart labels in template)
    transport_types = ['Bus', 'Car', 'Ferry', 'Motorbike', 'Plane', 'Train', 'Walk', 'Bicycle']

    # Emissions by category --> big change here --> we use a single query to get the sum of emissions for each transport type, and then we create a dictionary to map the transport types to their emissions, and then we create a list of emissions in the same order as the transport types list, this way we can easily pass it to the template and use it for the chart.
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2026_group4').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()

    emissions_dict = {transport: total for total, transport in emissions_by_transport}
    emission_transport = [emissions_dict.get(t, 0) for t in transport_types]

    # Kilometers by category --> big change here cut down the python code by using a dictionary comprehension to create a dictionary of transport types and their corresponding kilometers, then using a list comprehension to create a list of kilometers for each transport type in the same order as the transport_types list. This is more efficient and cleaner than the previous code which was doing multiple queries and loops to achieve the same result.
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2026_group4').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()

    kms_dict = {transport: kms for kms, transport in kms_by_transport}
    kms_transport = [kms_dict.get(t, 0) for t in transport_types]

    # Emissions by date
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2026_group4').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)

    # Kms by date
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2026_group4').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    for total, date in kms_by_date:
        over_time_kms.append(total)

    return render_template('gd_course/NHH_2026_group4/carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))



#Delete emission
@gd_course_NHH_2026_group4.route('/green_digitalization_course/NHH/2026/group4/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2026_group4.your_data'))
    
  
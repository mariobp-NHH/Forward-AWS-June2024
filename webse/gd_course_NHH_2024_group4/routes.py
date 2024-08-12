from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_NHH_2024_group4.forms import RegistrationForm, LoginForm, CarForm, BusForm, TrainForm, PlaneForm, MotorbikeForm, WalkForm, BicycleForm, FerryForm
from datetime import timedelta, datetime
from webse import db, bcrypt
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
import json
from json import dumps as json_dumps

gd_course_NHH_2024_group4=Blueprint('gd_course_NHH_2024_group4',__name__)

#Home routes
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/home')
def home_home():
  return render_template('gd_course/NHH_2024_group4/home.html', title = 'Home')

@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/aboutUs')
def aboutUs_home():
    return render_template('gd_course/NHH_2024_group4/aboutUs.html', title='aboutUs')

#Users routes
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2024_group4')
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_HVL_2024_group4.carbon_app_home'))
    return render_template('gd_course/NHH_2024_group4/users/register.html', title='Register', form=form)

@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2024_group4.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2024_group4.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger') 
  return render_template('gd_course/NHH_2024_group4/users/login.html', title='Login', form=form)

@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/logout')
def logout():
  logout_user()
  return redirect(url_for('gd_course_NHH_2024_group4.home_home'))

# Methodology
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/methodology')
def methodology_home():
  return render_template('gd_course/NHH_2024_group4/methodology.html', title='Methodology')


#Carbon app, main page
# Emissions factor per transport in kg per passemger km
efco2 = {
    "Bus": {"Fossil fuel": 0.097, "Electric": 0},
    "Car": {
        "Normal": {
            "Petrol": 0.192,
            "Diesel": 0.171,
            "Hybrid": 0.068,
            "Electric": 0.047,
        },
        "Small": {
            "Petrol": 0.192 * 0.85,
            "Diesel": 0.171 * 0.85,
            "Hybrid": 0.068 * 0.85,
            "Electric": 0.047 * 0.85,
        },
        "Large": {
            "Petrol": 0.192 * 1.15,
            "Diesel": 0.171 * 1.15,
            "Hybrid": 0.068 * 1.15,
            "Electric": 0.047 * 1.15,
        },
    },
    "Plane": {
        "Domestic flight": {"Petrol": 0.246},
        "Short-haul flight": {"Petrol": 0.151},
        "Long-haul flight": {"Petrol": 0.147},
    },
    "Ferry": {"Passanger": {"Diesel": 0.0187}, "With car": {"Diesel": 0.1295}},
    "Train": {"Fossil fuel": 0.041, "Electric": 0.004},
    "Motorbike": {"Petrol": 0.114},
    "Bicycle": {"No Fossil Fuel": 0},
    "Walk": {"No Fossil Fuel": 0},
    "Ferry": {
        "Passenger": {"Diesel": 0.0187},
        "Driver alone": {"Diesel": 0.1295},
        "Driver with passengers": {"Diesel": 0.1295},
    },
    "Train": {"Fossil fuel": 0.041, "Electric": 0.004},
    "Motorbike": {"Petrol": 0.114},
    "Bicycle": {"No Fossil Fuel": 0},
    "Walk": {"No Fossil Fuel": 0},
}

@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app')
#@login_required
def carbon_app_home():
    return render_template('gd_course/NHH_2024_group4/carbon_app/carbon_app.html', title='carbon_app')

@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_calculator')
def carbon_calculator_home():
    return render_template('gd_course/NHH_2024_group4/carbon_app/carbon_calculator.html')


# New entry bus
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport="Bus"

        co2 = efco2["Bus"][fuel]

        total_co2_emissions = co2 * kms
        co2 = float(kms) * efco2["Bus"][fuel]
        co2 = round(co2, 4)

        total = co2

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group4', institution='NHH_2024_group4', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        flash(f"Total CO2 emissions for the bus journey: {co2}", "success")
        return redirect(url_for('gd_course_NHH_2024_group4.carbon_calculator_home'))
    return render_template('gd_course/NHH_2024_group4/carbon_app/new_entry_bus.html', title='new entry bus', form=form)

# New entry car
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        transport = 'Car'
        kms = form.kms.data
        size = form.size.data
        fuel = form.fuel_type.data

        if size == "Small":
            factor = 0.85
        elif size == "Large":
            factor = 1.15
        else:
            factor = 1.0  # Normal size

        co2 = float(kms) * efco2["Car"][size][fuel] * factor

        co2 = round(co2, 4)
        total = co2
    
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group4', institution='NHH_2024_group4', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        flash(f"Total CO2 emissions for the car journey: {co2}", "success")
        return redirect(url_for('gd_course_NHH_2024_group4.carbon_calculator_home'))
    return render_template('gd_course/NHH_2024_group4/carbon_app/new_entry_car.html', title='new entry car', form=form)    

# New entry train
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        transport = 'Train'
        kms = form.kms.data
        fuel = form.fuel_type.data

        co2 = float(kms) * efco2["Train"][fuel]
        co2 = round(co2, 4)
        total = co2
    
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group4', institution='NHH_2024_group4', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        flash(f"Total CO2 emissions for the train journey: {co2}", "success")
        return redirect(url_for('gd_course_NHH_2024_group4.carbon_calculator_home'))
    return render_template('gd_course/NHH_2024_group4/carbon_app/new_entry_train.html', title='new entry train', form=form)    


# New entry plane
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        transport = 'Plane'
        kms = form.kms.data
        flight_type = form.flight_type.data

        co2 = float(kms) * efco2["Plane"][flight_type]["Petrol"]

        co2 = round(co2, 4)
        total = co2
        fuel=flight_type

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group4', institution='NHH_2024_group4', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        flash(f"Total CO2 emissions for the plane journey: {co2}", "success")
        return redirect(url_for('gd_course_NHH_2024_group4.carbon_calculator_home'))
    return render_template('gd_course/NHH_2024_group4/carbon_app/new_entry_plane.html', title='new entry plane', form=form)  

# New entry ferry
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        transport = 'Ferry'
        kms = form.kms.data
        travel_option = form.travel_option.data
        passengers = form.passengers.data

        if travel_option == "Passenger":
            co2 = float(kms) * efco2["Ferry"][travel_option]["Diesel"]
            co2 = round(co2, 4)

        if travel_option == "Driver alone":
            co2 = float(kms) * efco2["Ferry"][travel_option]["Diesel"]
            co2 = round(co2, 4)

        if travel_option == "Driver with passengers":
            co2_driver = float(kms) * efco2["Ferry"][travel_option]["Diesel"]
            co2_passengers = (
                float(kms) * efco2["Ferry"]["Passenger"]["Diesel"] * passengers
            )

            co2 = co2_passengers + co2_driver
            co2 = round(co2, 4)

        if travel_option == "Passenger":
            co2_per_passenger = co2
        if travel_option == "Driver alone":
            co2_per_passenger = co2
        if travel_option == "Driver with passengers":
            P = passengers + 1  # Total number of passengers including the driver
            co2_per_passenger = co2 / P
            co2_per_passenger = round(co2_per_passenger, 4)
        total = co2
        fuel = travel_option

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group4', institution='NHH_2024_group4', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        flash(
            f"Total CO2 emissions for the ferry journey: {co2}, CO2 per passemger: {co2_per_passenger}",
            "success",
        )
        return redirect(url_for('gd_course_NHH_2024_group4.carbon_calculator_home'))
    return render_template('gd_course/NHH_2024_group4/carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)     

# New entry motorbike
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        transport = 'Motorbike'
        kms = form.kms.data
        fuel = form.fuel_type.data

        co2 = float(kms) * efco2["Motorbike"][fuel]

        co2 = round(co2, 4)
        total = co2

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group4', institution='NHH_2024_group4', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        flash(f"Total CO2 emissions for the motorbike journey: {co2}", "success")
        return redirect(url_for('gd_course_NHH_2024_group4.carbon_calculator_home'))
    return render_template('gd_course/NHH_2024_group4/carbon_app/new_entry_motorbike.html', title='new entry motorbike', form=form) 


# New entry bicycle
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        transport = 'Bicycle'
        kms = form.kms.data
        fuel = form.fuel_type.data

        co2 = float(kms) * efco2["Bicycle"][fuel]

        co2 = round(co2, 4)
        total = co2

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group4', institution='NHH_2024_group4', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        flash(f"Total CO2 emissions for the bicycle journey: {co2}", "success")
        return redirect(url_for('gd_course_NHH_2024_group4.carbon_calculator_home'))
    return render_template('gd_course/NHH_2024_group4/carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

# New entry walk
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        transport = 'Walk'
        kms = form.kms.data
        fuel = form.fuel_type.data

        co2 = float(kms) * efco2["Walk"][fuel]

        co2 = round(co2, 4)
        total = co2

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group4', institution='NHH_2024_group4', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        flash(f"Total CO2 emissions for the walk journey: {co2}", "success")
        return redirect(url_for('gd_course_NHH_2024_group4.carbon_calculator_home'))
    return render_template('gd_course/NHH_2024_group4/carbon_app/new_entry_walk.html', title='new entry walk', form=form)


# Your data
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/carbon_your_emissions')
@login_required
def carbon_your_emissions():
    #Table
    db_entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='NHH_2024_group4').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    
    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group4').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    
    # Emissions by date (individual)
    emissions_over_time = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group4').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()

    emissions_over_time_list = [
        {"date": date.strftime("%Y-%m-%d"), "total": total}
        for total, date in emissions_over_time
    ]

    # Making the dictionary a JSON object
    emissions_over_time_json = json_dumps(emissions_over_time_list)
    print(emissions_over_time_json)

    # a list to store the emissions by transport
    transport_emissions = [
        {"transport": transport, "total": total}
        for total, transport in emissions_by_transport
    ]

    # Making the dictionary a JSON object
    transport_emissions_json = json_dumps(transport_emissions)
    print(db_entries)        

    return render_template('gd_course/NHH_2024_group4/carbon_app/carbon_your_emissions.html',
        title="Carbon Your Emissions",
        db_entries=db_entries,
        transport_emissions_json=transport_emissions_json,
        emissions_over_time_json=emissions_over_time_json)

# Delete emission
@gd_course_NHH_2024_group4.route('/green_digitalization_course/NHH/2024/group4/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2024_group4.carbon_your_emissions'))
    

from flask import render_template, Blueprint, redirect, flash, url_for, request, session, jsonify
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
from webse.gd_course_HVL_2025_group4.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, ScooterForm, TrainForm
import json
import flask 
from sqlalchemy import cast, Date, func, distinct, and_


gd_course_HVL_2025_group4=Blueprint('gd_course_HVL_2025_group4',__name__)


#Users routes
@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='HVL_2025_group4')
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_HVL_2025_group4.carbon_app_home'))
    return render_template('gd_course/HVL_2025_group4/buttons/register.html', title='register', form=form)
    
@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
    return redirect(url_for('gd_course_HVL_2025_group4.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use carbon app!', 'success')
        return redirect (next_page) if next_page else redirect(url_for('gd_course_HVL_2025_group4.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('gd_course/HVL_2025_group4/buttons/login.html', title='login', form=form)

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/logout')
def logout ():
   flash('You have logged out!', 'success') 
   logout_user()
   return redirect(url_for('gd_course_HVL_2025_group4.home_home'))

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/home')
def home_home():
  return render_template('gd_course/HVL_2025_group4/home.html')

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/meet_us')
def meet_us():
    return render_template('gd_course/HVL_2025_group4/buttons/meet_us.html')

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/cbnapp')
def cbnapp():
    return render_template('gd_course/HVL_2025_group4/buttons/cbnapp.html')

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/methodology')
def methodology_home():
  return render_template('gd_course/HVL_2025_group4/methodology.html', title='methodology')

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/paper')
def paper():
    return render_template('gd_course/HVL_2025_group4/buttons/buttons/paper.html')

"""  """

efco2={'Bus':{'Diesel':0.08},
    'Car':{'Petrol':0.122,'Diesel':0.148,'Electric':0},
    'Plane':{'Kerosene':0.225},
    'Ferry':{'Diesel':0.267},
    'Motorbike':{'Petrol':0.112,'Diesel':0.089},
    'Scooter':{'Electric':0.034},
    'Bicycle':{'Normal':0.0,'Electric':0.03},
    'Walk':{'No Fossil Fuel':0},
    'Train':{'Diesel':0.063,'Electric':0.005}}

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/carbon_app')
@login_required
def carbon_app_home():
    return render_template('gd_course/HVL_2025_group4/carbon_app/carbon_app.html')

@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/tutorial")
def tutorial():
    return render_template("gd_course/HVL_2025_group4/carbon_app/tutorial.html")

@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/car-emission", methods=['GET','POST'])
@login_required
def car_emission():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        days_used = form.days_used.data
        transport = 'Car'

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=days_used, student='HVL_2025_group4', institution='HVL_2025_group4', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    return render_template("gd_course/HVL_2025_group4/carbon_app/car_emission.html", form=form)

@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/bus-emission", methods=['GET','POST'])
@login_required
def bus_emission():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        days_used = form.days_used.data

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=days_used, student='HVL_2025_group4', institution='HVL_2025_group4', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    return render_template("gd_course/HVL_2025_group4/carbon_app/bus_emission.html", form=form)

@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/plane-emission", methods=['GET','POST'])
@login_required
def plane_emission():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        days_used = form.days_used.data

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=days_used, student='HVL_2025_group4', institution='HVL_2025_group4', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    return render_template("gd_course/HVL_2025_group4/carbon_app/plane_emission.html", form=form)

@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/train-emission", methods=['GET','POST'])
@login_required
def train_emission():
    form=TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport='Train'
        days_used = form.days_used.data

        co2 = float(kms) * efco2[transport][fuel]

        co2 = round(co2, 2)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=days_used, student='HVL_2025_group4', institution='HVL_2025_group4', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    return render_template("gd_course/HVL_2025_group4/carbon_app/train_emission.html", form=form)

@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/scooter-emission", methods=['GET','POST'])
@login_required
def scooter_emission():
    form = ScooterForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Scooter'
        days_used = form.days_used.data

        co2 = float(kms) * efco2[transport][fuel]

        co2 = round(co2, 2)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=days_used, student='HVL_2025_group4', institution='HVL_2025_group4', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    return render_template("gd_course/HVL_2025_group4/carbon_app/scooter_emission.html", form=form)


@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/bicycle-emission", methods=['GET','POST'])
@login_required
def bicycle_emission():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        days_used = form.days_used.data
        transport = 'Bicycle'

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=days_used, student='HVL_2025_group4', institution='HVL_2025_group4', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    return render_template("gd_course/HVL_2025_group4/carbon_app/bicycle_emission.html", form=form)

@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/ferry-emission", methods=['GET','POST'])
@login_required
def ferry_emission():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        days_used = form.days_used.data
        transport = 'Ferry'

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=days_used, student='HVL_2025_group4', institution='HVL_2025_group4', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    return render_template("gd_course/HVL_2025_group4/carbon_app/ferry_emission.html", form=form)

@gd_course_HVL_2025_group4.route("/green_digitalization_course/HVL/2025/group4/motorbike-emission", methods=['GET','POST'])
@login_required
def motorbike_emission():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        days_used = form.days_used.data
        transport = 'Motorbike'

        co2 = float(kms) * efco2[transport][fuel]

        co2 = float("{:.2f}".format(co2))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=days_used, student='HVL_2025_group4', institution='HVL_2025_group4', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    return render_template("gd_course/HVL_2025_group4/carbon_app/motorbike_emission.html", form=form)

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/carbon_app/your_data')
@login_required
def your_data():
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group4').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    
    vehicle_labels = []
    vehicle_totals = []

    weekly_labels = []
    weekly_emissions = []

    for e in entries:
        if e.transport not in vehicle_labels:
            vehicle_labels.append(e.transport)
            vehicle_totals.append(float(e.co2))
        else:
            index = vehicle_labels.index(e.transport)
            vehicle_totals[index] += float(e.co2)

        weekly_labels.append(f"{e.transport} ({e.fuel})")
        weekly_emissions.append(float(e.co2) * int(e.total))

    return render_template('gd_course/HVL_2025_group4/carbon_app/your_data.html', title='your_data', entries=entries, vehicle_labels=vehicle_labels, vehicle_totals=vehicle_totals, weekly_labels=weekly_labels, weekly_emissions=weekly_emissions)

@gd_course_HVL_2025_group4.route('/green_digitalization_course/HVL/2025/group4/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_HVL_2025_group4.your_data'))
    


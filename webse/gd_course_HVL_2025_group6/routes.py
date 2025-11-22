from flask import render_template, Blueprint, redirect, flash, url_for, request, session, jsonify
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
from webse.gd_course_HVL_2025_group6.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, FerryForm, TrainForm, WalkForm
import flask 
from sqlalchemy import cast, Date, func, distinct, and_
import json


gd_course_HVL_2025_group6=Blueprint('gd_course_HVL_2025_group6',__name__)


#Users routes
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('gd_course_HVL_2025_group6.home_home'))
    if form.validate_on_submit():
        user_hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='HVL_2025_group6')
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_HVL_2025_group6.carbon_app_home'))
    return render_template('gd_course/HVL_2025_group6/users/register.html', title='register', form=form)
    
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
    return redirect(url_for('gd_course_HVL_2025_group6.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use carbon app!', 'success')
        return redirect (next_page) if next_page else redirect(url_for('gd_course_HVL_2025_group6.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('gd_course/HVL_2025_group6/users/login.html', title='login', form=form)

@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/logout')
def logout ():
   flash('You have logged out!', 'success') 
   logout_user()
   return redirect(url_for('gd_course_HVL_2025_group6.home_home'))

@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/home')
def home_home():
  return render_template('gd_course/HVL_2025_group6/home.html')

@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/aboutus')
def aboutus_home():
  return render_template('gd_course/HVL_2025_group6/aboutus.html', title='aboutus')

efco2 = {
    'Bus': {'Diesel': 0.030},
    'Car': {'Petrol': 0.198, 'Diesel': 0.229, 'Electric': 0.059},
    'Plane': {'Economy': 0.127, 'Business': 0.284},
    'Ferry': {'Passenger with car': 0.563, 'Passenger only': 0.186},
    'Train': {'Diesel': 0.091, 'Electric': 0.007},
    'Walk': {'No Fossil Fuel': 0}
}
# Carbon app, main page
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator')
@login_required
def calculator_home():
    return render_template('gd_course/HVL_2025_group6/calculator/calculator_home.html', title='calculator')
# Carbon app, plane
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator/new_entry_plane', methods=['GET', 'POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, 
                                total=co2, student='HVL_2025_group6', institution='HVL_2025_group6', 
                                year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group6.your_data'))
    return render_template('gd_course/HVL_2025_group6/calculator/new_entry_plane.html',
        title='Plane Calculator',
        form=form
    )
# Carbon app, walk
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator/new_entry_walk', methods=['GET', 'POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, 
                                total=co2, student='HVL_2025_group6', institution='HVL_2025_group6', 
                                year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group6.your_data'))
    return render_template('gd_course/HVL_2025_group6/calculator/new_entry_walk.html',
        title='Walk/Bike Calculator',
        form=form
    )
# Carbon app, bus
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator/new_entry_bus', methods=['GET', 'POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, 
                                total=co2, student='HVL_2025_group6', institution='HVL_2025_group6', 
                                year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group6.your_data'))
    return render_template('gd_course/HVL_2025_group6/calculator/new_entry_bus.html',
        title='Bus Calculator',
        form=form
    )
# Carbon app, car
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator/new_entry_car', methods=['GET', 'POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, 
                                total=co2, student='HVL_2025_group6', institution='HVL_2025_group6', 
                                year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group6.your_data'))
    return render_template('gd_course/HVL_2025_group6/calculator/new_entry_car.html',
        title='Car Calculator',
        form=form
    )
# Carbon app, ferry
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator/new_entry_ferry', methods=['GET', 'POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, 
                                total=co2, student='HVL_2025_group6', institution='HVL_2025_group6', 
                                year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group6.your_data'))
    return render_template('gd_course/HVL_2025_group6/calculator/new_entry_ferry.html',
        title='Ferry Calculator',
        form=form
    )
# Carbon app, train
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator/new_entry_train', methods=['GET', 'POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, 
                                total=co2, student='HVL_2025_group6', institution='HVL_2025_group6', 
                                year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group6.your_data'))
    return render_template('gd_course/HVL_2025_group6/calculator/new_entry_train.html',
        title='Train Calculator',
        form=form
    )
# Your data
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator/your_data')
@login_required
def your_data():
    # Table
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='HVL_2025_group6').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    
    # Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group6').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])
    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[1] = first_tuple_elements[index_bus]
    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        kms_transport[2] = first_tuple_elements[index_car]
    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        kms_transport[3] = first_tuple_elements[index_ferry]
    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[4] = first_tuple_elements[index_plane]
    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[5] = first_tuple_elements[index_train]
    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        kms_transport[6] = first_tuple_elements[index_walk]
   
    # Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group6').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)
    return render_template('gd_course/HVL_2025_group6/calculator/your_data.html',
        title='your_data',
        entries=entries,
        kms_by_transport=json.dumps(kms_transport),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label)
    )
# Delete emission
@gd_course_HVL_2025_group6.route('/green_digitalization_course/HVL/2025/group6/calculator/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_HVL_2025_group6.your_data'))

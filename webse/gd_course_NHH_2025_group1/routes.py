from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_NHH_2025_group1.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, TrainForm, VanForm
from webse.models import User, EmissionsGD
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_user, current_user, logout_user, login_required
import json

gd_course_NHH_2025_group1=Blueprint('gd_course_NHH_2025_group1',__name__)

@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/home')
def home_home():
  return render_template('gd_course/NHH_2025_group1/home.html')

@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2025_group1.home_home'))
  if form.validate_on_submit():
      user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2025_group1')
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created! Now, you are able to login!', 'success')
      return redirect(url_for('gd_course_NHH_2025_group1.login'))
  return render_template('gd_course/NHH_2025_group1/users/register.html', title='register', form=form)

@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2025_group1.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2025_group1.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')
  return render_template('gd_course/NHH_2025_group1/users/login.html', title='login', form=form)

@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/logout')
def logout():
    logout_user()
    return redirect(url_for('gd_course_NHH_2025_group1.home_home'))

efco2 = {
    'Bus': {'Diesel': 0.03,'Electric':0.00},
    'Car': {'Petrol': 0.17082, 'Diesel': 0.17048, 'Hybrid': 0.12004, 'Electric':0.00},
    'Plane': {'Economy': 0.140625, 'Business': 0.40781, 'First Class': 0.56251},
    'Ferry': {'Diesel': 0.01874},
    'Motorbike': {'Petrol': 0.11355},
    'Van': {'Petrol': 0.21332, 'Diesel': 0.23157, 'Electric': 0},
    'Train': {
        'Diesel': 0.091,
        'Electric (Nordic)': 0.007,
        'Electric (Europe excluding Nordic)': 0.026
    },
    'Bicycle': {'No Fossil Fuel': 0},
    'Walk': {'No Fossil Fuel': 0}
}

efch4 = {
    'Bus': {'Diesel': 2e-5},
    'Car': {'Petrol': 3.1e-4, 'Diesel': 3e-6},
    'Plane': {'Economy': 1.1e-4, 'Business': 1.1e-4, 'First Class': 1.1e-4},
    'Ferry': {'Diesel': 3e-5},
    'Motorbike': {'Petrol': 2.1e-3},
    'Scooter': {'No Fossil Fuel': 0},
    'Bicycle': {'No Fossil Fuel': 0},
    'Walk': {'No Fossil Fuel': 0},
    'Train': {
        'Diesel': 9.1e-2,
        'Electric (Nordic)': 0.007,
        'Electric (Europe excluding Nordic)': 0.026
    },
    'Van': {'Petrol': 3.1e-4, 'Diesel': 3e-6, 'Electric': 0}
}

# Carbon app, main page
@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app')
@login_required
def carbon_app_home():
    return render_template('gd_course/NHH_2025_group1/carbon_app/carbon_app.html', title='Carbon App')

# New entry bus
@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/new_entry_bus', methods=['GET', 'POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2 + ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, student='NHH_2025_group1', institution='NHH_2025_group1', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group1.your_data'))
    return render_template('gd_course/NHH_2025_group1/carbon_app/new_entry_bus.html', title='New Entry: Bus', form=form)

# New entry car
@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/new_entry_car', methods=['GET', 'POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2 + ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, student='NHH_2025_group1', institution='NHH_2025_group1', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group1.your_data'))
    return render_template('gd_course/NHH_2025_group1/carbon_app/new_entry_car.html', title='New Entry: Car', form=form)

# New entry plane
@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/new_entry_plane', methods=['GET', 'POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2 + ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, student='NHH_2025_group1', institution='NHH_2025_group1', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group1.your_data'))
    return render_template('gd_course/NHH_2025_group1/carbon_app/new_entry_plane.html', title='New Entry: Plane', form=form)

# New entry ferry
@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/new_entry_ferry', methods=['GET', 'POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2 + ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, student='NHH_2025_group1', institution='NHH_2025_group1', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group1.your_data'))
    return render_template('gd_course/NHH_2025_group1/carbon_app/new_entry_ferry.html', title='New Entry: Ferry', form=form)

# New entry motorbike
@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/new_entry_motorbike', methods=['GET', 'POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2 + ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, student='NHH_2025_group1', institution='NHH_2025_group1', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group1.your_data'))
    return render_template('gd_course/NHH_2025_group1/carbon_app/new_entry_motorbike.html', title='New Entry: Motorbike', form=form)

# New entry train
@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/new_entry_train', methods=['GET', 'POST'])
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

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, student='NHH_2025_group1', institution='NHH_2025_group1', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group1.your_data'))
    return render_template('gd_course/NHH_2025_group1/carbon_app/new_entry_train.html', title='New Entry: Train', form=form)

# New entry van
@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/new_entry_van', methods=['GET', 'POST'])
@login_required
def new_entry_van():
    form = VanForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Van'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2 + ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, student='NHH_2025_group1', institution='NHH_2025_group1', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group1.your_data'))
    return render_template('gd_course/NHH_2025_group1/carbon_app/new_entry_van.html', title='New Entry: Van', form=form)

@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/your_data')
@login_required
def your_data():
    categories = ['Bus', 'Car', 'Ferry', 'Train', 'Motorbike', 'Plane', 'Van']

    entries = EmissionsGD.query.filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group1').\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()

    # Emissions by transport
    emissions_raw = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport).\
        filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group1').\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).\
        group_by(EmissionsGD.transport).all()

    emission_transport = [0] * len(categories)
    for total, transport in emissions_raw:
        if transport in categories:
            idx = categories.index(transport)
            emission_transport[idx] = round(float(total), 2)

    # Kilometers by transport
    kms_raw = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport).\
        filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group1').\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).\
        group_by(EmissionsGD.transport).all()

    kms_transport = [0] * len(categories)
    for total, transport in kms_raw:
        if transport in categories:
            idx = categories.index(transport)
            kms_transport[idx] = round(float(total), 2)

    # Emissions over time
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date).\
        filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group1').\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()

    over_time_emissions = [round(float(total), 2) for total, _ in emissions_by_date]
    dates_label = [date.strftime("%m-%d-%y") for _, date in emissions_by_date]

    # Kilometers over time
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date).\
        filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group1').\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()

    over_time_kms = [round(float(total), 2) for total, _ in kms_by_date]

    print("Categories:", categories)
    print("Emission Transport:", emission_transport)
    print("Kilometers Transport:", kms_transport)
    print("Over Time Emissions:", over_time_emissions)
    print("Over Time Kms:", over_time_kms)
    print("Dates Label:", dates_label)

    return render_template('gd_course/NHH_2025_group1/carbon_app/your_data.html',
        title='your_data',
        entries=entries,
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label),
        categories=categories  # Optional, if you want to use labels from backend
    )

@gd_course_NHH_2025_group1.route('/green_digitalization_course/NHH/2025/group1/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(entry_id)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2025_group1.your_data'))

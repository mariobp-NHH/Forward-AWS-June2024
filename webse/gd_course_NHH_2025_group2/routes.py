from flask import render_template, Blueprint, redirect, flash, url_for, request,  abort
from webse.gd_course_NHH_2025_group2.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, FerryForm, MotorcycleForm, TrainForm, BicycleForm, WalkForm
from webse.models import User, EmissionsGD
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_user, current_user, logout_user, login_required
import json

gd_course_NHH_2025_group2=Blueprint('gd_course_NHH_2025_group2',__name__)

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/home')
def home_home():
  return render_template('gd_course/NHH_2025_group2/home.html')

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/register', methods=['GET','POST'])
def register_home():
  form = RegistrationForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2025_group2.home_home'))
  if form.validate_on_submit():
      user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2025_group2')
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created! Now, you are able to login!', 'success')
      return redirect(url_for('gd_course_NHH_2025_group2.login_home'))
  return render_template('gd_course/NHH_2025_group2/user/register.html', title='register', form=form)

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/login', methods=['GET','POST'])
def login_home():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2025_group2.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2025_group2.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')
  return render_template('gd_course/NHH_2025_group2/user/login.html', title='login', form=form)

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/logout')
def logout():
    logout_user()
    return redirect(url_for('gd_course_NHH_2025_group2.home_home'))

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/methodology')
def methodology_home():
  return render_template('/gd_course/NHH_2025_group2/methodology.html', title='methodology')

efco2={
    'Walk': {'No Fossil Fuel': 0.0},
    'Bicycle': {'No Fossil Fuel': 0.0},
    'Car': {
        'Petrol': 0.160,
        'Diesel': 0.170,
        'Electric': 0.0193,
        'Hybrid': 0.1261
    },
    'Motorcycle': {
        'Small': 0.08277,
        'Medium': 0.10086,
        'Large': 0.13237
    },
    'Bus': {
        'Diesel': 0.027,
        'Electric': 0.013
    },
    'Train': {
        'Norway': 0.010,
        'EU': 0.033
    },
    'Ferry': {'Diesel': 0.377},
    'Plane': {
        'Short-haul': 0.246,
        'Long-haul': 0.147
    }
}

@gd_course_NHH_2025_group2.route("/green_digitalization_course/NHH/2025/group2/carbon_app")
@login_required
def carbon_app_home():
    return render_template("gd_course/NHH_2025_group2/carbon_app/carbon_app.html", title="carbon_app")

def handle_new_entry(form, transport):
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        co2 = float(kms) * efco2[transport][fuel]
        co2 = float("{:.2f}".format(co2))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2025_group2', institution='NHH_2025_group2', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group2.your_data'))
    return render_template(f'gd_course/NHH_2025_group2/carbon_app/new_entry_{transport.lower()}.html', title=f'new entry {transport.lower()}', form=form)

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    return handle_new_entry(BusForm(), 'Bus')

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    return handle_new_entry(CarForm(), 'Car')

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    return handle_new_entry(PlaneForm(), 'Plane')

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    return handle_new_entry(FerryForm(), 'Ferry')

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/new_entry_motorcycle', methods=['GET','POST'])
@login_required
def new_entry_motorcycle():
    return handle_new_entry(MotorcycleForm(), 'Motorcycle')

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    return handle_new_entry(BicycleForm(), 'Bicycle')

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    return handle_new_entry(TrainForm(), 'Train')

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    return handle_new_entry(WalkForm(), 'Walk')

@gd_course_NHH_2025_group2.route("/green_digitalization_course/NHH/2025/group2/carbon_app/your_data")
@login_required
def your_data():
    entries = EmissionsGD.query.filter_by(author=current_user).\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='NHH_2025_group2').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()

    transport_types = ['Bicycle', 'Bus', 'Car', 'Ferry', 'Motorcycle', 'Plane', 'Train', 'Walk']
    emission_transport = [0] * 8
    kms_transport = [0] * 8
    transport_indices = {name: i for i, name in enumerate(transport_types)}

    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.co2), EmissionsGD.transport).\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group2').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    for total, transport in emissions_by_transport:
        if transport in transport_indices:
            emission_transport[transport_indices[transport]] = total

    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport).\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group2').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    for total, transport in kms_by_transport:
        if transport in transport_indices:
            kms_transport[transport_indices[transport]] = total

    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.co2), EmissionsGD.date).\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group2').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = [total for total, _ in emissions_by_date]
    dates_label = [date.strftime("%m-%d-%y") for _, date in emissions_by_date]

    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date).\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user).\
        filter(EmissionsGD.institution=='NHH_2025_group2').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = [total for total, _ in kms_by_date]

    return render_template('gd_course/NHH_2025_group2/carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))

@gd_course_NHH_2025_group2.route('/green_digitalization_course/NHH/2025/group2/carbon_app/delete-emission/<int:entry_id>')
@login_required
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    if entry.author != current_user: abort(403)
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2025_group2.your_data'))

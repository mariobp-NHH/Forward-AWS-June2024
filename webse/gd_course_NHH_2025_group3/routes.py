from flask import render_template, Blueprint, redirect, flash, url_for, request, jsonify, send_file
from webse.gd_course_NHH_2025_group3.forms import RegistrationForm, LoginForm, Form
from webse.models import User, EmissionsGD
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_user, current_user, logout_user, login_required
import json

gd_course_NHH_2025_group3=Blueprint('gd_course_NHH_2025_group3',__name__)

@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/home')
def home_page():
  return render_template('gd_course/NHH_2025_group3/home.html')


@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/profile')
def profile_page():
  return render_template('gd_course/NHH_2025_group3/profile.html')

@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/about')
def about_page():
  return render_template('gd_course/NHH_2025_group3/about.html')

@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/methodology')
def methodology_page():
  return render_template('gd_course/NHH_2025_group3/methodology.html')

@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/downloadPaper')
def download ():
    path = "./static/gd_course_NHH_2025_group3/downloadable/Carbon-App-Paper-Group-3-2025.pdf"
    return send_file(path, as_attachment=True)

@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2025_group3.home_page'))
  if form.validate_on_submit():
      user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2025_group3')
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created! You can now login!', 'success')
      return redirect(url_for('gd_course_NHH_2025_group3.login'))
  return render_template('gd_course/NHH_2025_group3/users/register.html', title='register', form=form)

@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2025_group3.home_page'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2025_group3.home_page'))
    else:
        flash('Login unsuccessful. Please check your email and password!', 'danger')
  return render_template('gd_course/NHH_2025_group3/users/login.html', title='login', form=form)

@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/logout')
def logout():
    logout_user()
    return redirect(url_for('gd_course_NHH_2025_group3.home_page'))

efco2={'Bus':{'Diesel':0.03,'CNG':0.0285, 'No Fossil Fuel':0.013},
    'Car':{'Petrol':0.180,'Diesel':0.160, 'Hybrid (gasoline)': 0.100, 'CNG': 0.130, 'No Fossil Fuel':0.026},
    'Train': {'Diesel': 0.027, 'Biodiesel': 0.014, 'No Fossil Fuel': 0.013}, ##ADD BIODIESEL
    'Plane':{'Petrol':0.300},
    'Ferry':{'Diesel':0.019, 'CNG': 0.01425},
    'Motorbike':{'Petrol':0.200},
    'Scooter':{'Petrol': 0.100,'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}


#Calculator, main page
@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/calculator', methods=['GET','POST'])
@login_required
def calculator_page():
    form = Form()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = form.method.data
        passengers = form.passengers.data
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * (efco2[transport][fuel]/passengers)

        co2 = float("{:.2f}".format(co2))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, student='NHH_2025_group3', institution='NHH_2025_group3', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2025_group3.your_data'))
    return render_template('gd_course/NHH_2025_group3/calculator/calculator.html', title='New entry', form=form)

@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/get-items')
def get_items():
    method = request.args.get('method')
    items_dict = {
        'Bus': ['Diesel', 'CNG', 'No Fossil Fuel'],
        'Car': ['Petrol', 'Diesel', 'Hybrid (gasoline)', 'CNG', 'No Fossil Fuel'],
        'Train': ['Diesel', 'Biodiesel', 'No Fossil Fuel'],
        'Plane': ['Petrol'],
        'Ferry': ['Diesel', 'CNG'],
        'Motorbike': ['Petrol'],
        'Scooter': ['Petrol', 'No Fossil Fuel'],
        'Bicycle': ['No Fossil Fuel'],
        'Walk': ['No Fossil Fuel']
    }
    items = items_dict.get(method, [])
    return jsonify({'items': items})


#Your data
@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/calculator/your_data')
@login_required
def your_data():
    #Table
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=30))).\
        filter(EmissionsGD.institution=='NHH_2025_group3').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()

#Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.co2), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=30))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2025_group3').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        emission_transport[1]=first_tuple_elements[index_bus]
    else:
        emission_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        emission_transport[2]=first_tuple_elements[index_car]
    else:
        emission_transport[2]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        emission_transport[3]=first_tuple_elements[index_ferry]
    else:
        emission_transport[3]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        emission_transport[4]=first_tuple_elements[index_motorbike]
    else:
        emission_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        emission_transport[5]=first_tuple_elements[index_plane]
    else:
        emission_transport[5]

    if 'Scooter' in second_tuple_elements:
        index_scooter = second_tuple_elements.index('Scooter')
        emission_transport[6]=first_tuple_elements[index_scooter]
    else:
        emission_transport[6]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[7]=first_tuple_elements[index_train]
    else:
        emission_transport[7]

    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=30))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2025_group3').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bicycle' in second_tuple_elements:
        index_bicycle = second_tuple_elements.index('Bicycle')
        kms_transport[0]=first_tuple_elements[index_bicycle]
    else:
        kms_transport[0]

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[1]=first_tuple_elements[index_bus]
    else:
        kms_transport[1]

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        kms_transport[2]=first_tuple_elements[index_car]
    else:
        kms_transport[2]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        kms_transport[3]=first_tuple_elements[index_ferry]
    else:
        kms_transport[3]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        kms_transport[4]=first_tuple_elements[index_motorbike]
    else:
        kms_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[5]=first_tuple_elements[index_plane]
    else:
        kms_transport[5]

    if 'Scooter' in second_tuple_elements:
        index_scooter = second_tuple_elements.index('Scooter')
        kms_transport[6]=first_tuple_elements[index_scooter]
    else:
        kms_transport[6]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[7]=first_tuple_elements[index_train]
    else:
        kms_transport[7]

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        kms_transport[8]=first_tuple_elements[index_walk]
    else:
        kms_transport[8]

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.co2), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=30))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2025_group3').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=30))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2025_group3').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)


    return render_template('gd_course/NHH_2025_group3/calculator/your_data.html', title='Your Data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,
        emission_transport_python_list=emission_transport,
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))


#Delete emission
@gd_course_NHH_2025_group3.route('/green_digitalization_course/NHH/2025/group3/calculator/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2025_group3.your_data'))


from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_HVL_2023_group1.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, TrainForm, ElkickScooterForm, ElBicycleForm
from datetime import timedelta, datetime
from webse import db, bcrypt
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
import json

gd_course_HVL_2023_group1=Blueprint('gd_course_HVL_2023_group1',__name__)

#Home routes
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/home')
def home_home():
  return render_template('gd_course/HVL_2023_group1/home.html', title = 'Home')

#Users routes
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='HVL_2023_group1')
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_HVL_2023_group1.login'))
    return render_template('gd_course/HVL_2023_group1/users/register.html', title='Register', form=form)

@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_HVL_2023_group1.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_HVL_2023_group1.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger') 
  return render_template('gd_course/HVL_2023_group1/users/login.html', title='Login', form=form)

@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/logout')
def logout():
  logout_user()
  return redirect(url_for('gd_course_HVL_2023_group1.home_home'))

# Methodology
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/methodology')
def methodology_home():
  return render_template('gd_course/HVL_2023_group1/methodology.html', title='Methodology')


#Carbon app, main page
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app')
@login_required
def carbon_app_home():
    return render_template('gd_course/HVL_2023_group1/carbon_app/carbon_app.html', title='carbon_app')

efco2={'Bus':{'Diesel':0.855,'BioDiesel':0.014,'Electric':0.067},
    'Car':{'Gasoline':0.157,'Diesel':0.130,'Hybrid':0.152,'No Fossil Fuel':0.0776},
    'Plane':{'Gasoline':0.298},
    'Train':{'No Fossil Fuel':0.045},
    'ElkickScooter':{'No Fossil Fuel':0.002328},
    'ElBicycle':{'No Fossil Fuel':0.002327}}


#New entry bus
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='HVL_2023_group1', institution='HVL_2023_group1', year=2023, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2023_group1.your_data'))
    return render_template('gd_course/HVL_2023_group1/carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='HVL_2023_group1', institution='HVL_2023_group1', year=2023, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2023_group1.your_data'))
    return render_template('gd_course/HVL_2023_group1/carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry plane
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='HVL_2023_group1', institution='HVL_2023_group1', year=2023, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2023_group1.your_data'))
    return render_template('gd_course/HVL_2023_group1/carbon_app/new_entry_plane.html', title='new entry plane', form=form)  

#New entry Train
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='HVL_2023_group1', institution='HVL_2023_group1', year=2023, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2023_group1.your_data'))
    return render_template('gd_course/HVL_2023_group1/carbon_app/new_entry_train.html', title='new entry Train', form=form)     

#New entry ElkickScooter
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app/new_entry_ElkickScooter', methods=['GET','POST'])
@login_required
def new_entry_ElkickScooter():
    form = ElkickScooterForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'ElkickScooter'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='HVL_2023_group1', institution='HVL_2023_group1', year=2023, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2023_group1.your_data'))
    return render_template('gd_course/HVL_2023_group1/carbon_app/new_entry_ElkickScooter.html', title='new entry motorbike', form=form) 

#New entry ElBicycleForm
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app/new_entry_ElBicycle', methods=['GET','POST'])
@login_required
def new_entry_ElBicycle():
    form = ElBicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'ElBicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='HVL_2023_group1', institution='HVL_2023_group1', year=2023, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2023_group1.your_data'))
    return render_template('gd_course/HVL_2023_group1/carbon_app/new_entry_Elbicycle.html', title='new entry Elbicycle', form=form)


#Your data
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app/your_data')
@login_required
def your_data():
    #Table
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='HVL_2023_group1').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    
    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2023_group1').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        emission_transport[0]=first_tuple_elements[index_bus]
    else:
        emission_transport[0] 

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        emission_transport[1]=first_tuple_elements[index_car]
    else:
        emission_transport[1]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        emission_transport[2]=first_tuple_elements[index_plane]
    else:
        emission_transport[2]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[3]=first_tuple_elements[index_train]
    else:
        emission_transport[3]

    if 'ElkickScooter' in second_tuple_elements:
        index_scooter = second_tuple_elements.index('ElkickScooter')
        emission_transport[4]=first_tuple_elements[index_scooter]
    else:
        emission_transport[4]

    if 'ElBicycle' in second_tuple_elements:
        index_bike = second_tuple_elements.index('ElBicycle')
        emission_transport[5]=first_tuple_elements[index_bike]
    else:
        emission_transport[5]


    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2023_group1').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[0]=first_tuple_elements[index_bus]
    else:
        kms_transport[0] 

    if 'Car' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car')
        kms_transport[1]=first_tuple_elements[index_car]
    else:
        kms_transport[1]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[2]=first_tuple_elements[index_plane]
    else:
        kms_transport[2]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[3]=first_tuple_elements[index_train]
    else:
        kms_transport[3]

    if 'ElkickScooter' in second_tuple_elements:
        index_scooter = second_tuple_elements.index('ElkickScooter')
        kms_transport[4]=first_tuple_elements[index_scooter]
    else:
        kms_transport[4]

    if 'ElBicycle' in second_tuple_elements:
        index_bike = second_tuple_elements.index('ElBicycle')
        kms_transport[5]=first_tuple_elements[index_bike]
    else:
        kms_transport[5]

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2023_group1').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2023_group1').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)      


    return render_template('gd_course/HVL_2023_group1/carbon_app/your_data.html', title='your_data', entries=entries,         
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))
    

#Delete emission
@gd_course_HVL_2023_group1.route('/green_digitalization_course/HVL/2023/group1/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_HVL_2023_group1.your_data'))
    

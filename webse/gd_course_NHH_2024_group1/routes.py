from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_NHH_2024_group1.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, FerryForm, TrainForm, MotorbikeForm, BicycleForm, WalkForm, SpecificCarForm, CarbonAPI
from datetime import timedelta, datetime
from webse import db, bcrypt
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
import json

gd_course_NHH_2024_group1=Blueprint('gd_course_NHH_2024_group1',__name__)

#Home routes
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/home')
def home_home():
  return render_template('gd_course/NHH_2024_group1/home.html', title = 'Home')

#Users routes
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2024_group1')
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        flash('Your account has been created! ✅ Now, you are able to login.', 'success')
        return redirect(url_for('gd_course_HVL_2024_group1.carbon_app_home'))
    return render_template('gd_course/NHH_2024_group1/users/register.html', title='Register', form=form)

@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2024_group1.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2024_group1.home_home'))
    else:
        flash('Login unsuccessful ❌ Please check email and password!', 'danger')   
  return render_template('gd_course/NHH_2024_group1/users/login.html', title='Login', form=form)

@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/logout')
def logout():
  logout_user()
  flash('You have been logged out 👋🏾', 'success')
  return redirect(url_for('gd_course_NHH_2024_group1.home_home'))

# Methodology
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/methodology')
def methodology_home():
  return render_template('gd_course/NHH_2024_group1/methodology.html', title='Methodology')

#Carbon Interface
api = CarbonAPI()

#API
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_interface/cars')
def allV():
    return api.allVehicleMakes()

@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/models/<id>')
def getMakes(id):
    return api.getVehicleMake(id)


#Carbon app, main page
# Emissions factor per transport in kg per passemger km
efco2={'Bus':{'Diesel':0.105,'Electric':0.03052,'Hybrid':0.054},
    'Car':{'Gasoline':0.0384,'Diesel':0.0343,'Hybrid':0.0298,'Electric':0.0106,'Hydrogen':0},
    'Plane':{'Short-haul (Buisness)':0.147,
             'Long-haul (Economy)': 0.235, 
             'Long-haul (Premium economy)': 0.427, 
             'Long-haul (First-class)': 0.558, 
             'International (Economy)': 0.140,
             'International (Premium economy)': 0.229,
             'International (Buisness)': 0.406,
             'International (First Class)': 0.560},
    'Ferry':{'Regular':0.226, 'High-speed':0.452},
    'Train':{'Diesel':0.091, 'Electric (Nordic)':0.024, 'Electric (EU)': 0.007},
    'Motorbike':{'≤125cc':0.0415,'125cc to 500cc':0.0505, '>500cc':0.0665,},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}

@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc')
#@login_required
def carbon_calc_home():
    return render_template('gd_course/NHH_2024_group1/carbon_calc/carbon_calc.html', title='carbon_calc')


# New entry bus
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data 
        transport = 'Bus'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / 70 # Divided by passenger(s)
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_bus.html', title='new entry bus', form=form)

# New entry car
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / 4
        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))
    
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_car.html', title='new entry car', form=form)    

# New entry specific car
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_specific_car', methods=['GET','POST'])
@login_required
def new_entry_specific_car():
    form = SpecificCarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        model = form.model.data
        transport = "Specified Car"
        fuel = "N/A"
        
        estimate = api.getEstimate(id=model, distance=kms)
        co2 = estimate["data"]["attributes"]["carbon_kg"]
        co2 = int(co2)/4

        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))
    
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_specific_car.html', title='new entry specific car', form=form)


# New entry plane
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / 100 # average amount of passengers (for all types of flights)

        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_plane.html', title='new entry plane', form=form)  

# New entry ferry
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / 309

        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_ferry.html', title='new entry ferry', form=form)     

# New entry motorbike
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_motorbike.html', title='new entry motorbike', form=form) 

@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_train', methods=['GET','POST'])
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

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_train.html', title='new entry train', form=form) 

# New entry bicycle
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_bicycle.html', title='new entry bicycle', form=form)

# New entry walk
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]

        total = co2

        co2 = float("{:.2f}".format(co2))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group1', institution='NHH_2024_group1', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    return render_template('gd_course/NHH_2024_group1/carbon_calc/new_entry_walk.html', title='new entry walk', form=form)

# Your data
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/your_data')
@login_required
def your_data():
    #Table
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='NHH_2024_group1').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    
    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group1').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
    
    if 'Specified Car' in second_tuple_elements:
        index_specified_car = second_tuple_elements.index('Specified Car')
        emission_transport[2]=first_tuple_elements[index_specified_car]
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

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[6]=first_tuple_elements[index_train]
    else:
        emission_transport[6]

    # Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group1').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

    if 'Specified Car' in second_tuple_elements:
        index_specified_car = second_tuple_elements.index('Specified Car')
        kms_transport[3]=first_tuple_elements[index_specified_car]
    else:
        kms_transport[3]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        kms_transport[4]=first_tuple_elements[index_ferry]
    else:
        kms_transport[4]

    if 'Motorbike' in second_tuple_elements:
        index_motorbike = second_tuple_elements.index('Motorbike')
        kms_transport[5]=first_tuple_elements[index_motorbike]
    else:
        kms_transport[5]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[6]=first_tuple_elements[index_plane]
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

    # Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group1').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    # Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group1').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)      

    return render_template('gd_course/NHH_2024_group1/carbon_calc/your_data.html', title='your_data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))

# Delete emission
@gd_course_NHH_2024_group1.route('/green_digitalization_course/NHH/2024/group1/carbon_calc/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2024_group1.your_data'))
    

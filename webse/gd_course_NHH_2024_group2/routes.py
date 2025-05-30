from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_NHH_2024_group2.forms import RegistrationForm, LoginForm, BusForm, CarForm, FerryForm,trainForm, BicycleForm, WalkForm, CarFormSUV, Domestic_FlightForm, Long_haul_FlightForm, long_distance_busForm, tramForm
from datetime import timedelta, datetime
from webse import db, bcrypt
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
import json

gd_course_NHH_2024_group2=Blueprint('gd_course_NHH_2024_group2',__name__)

#Home routes
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/home')
def home_home():
  return render_template('gd_course/NHH_2024_group2/home.html', title = 'Home')

@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/contact')
def contact_home():
  return render_template('gd_course/NHH_2024_group2/contact.html', title='contact')

#Users routes
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2024_group2')
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_HVL_2024_group2.carbon_app_home'))
    return render_template('gd_course/NHH_2024_group2/users/register.html', title='Register', form=form)

@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2024_group2.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2024_group2.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger') 
  return render_template('gd_course/NHH_2024_group2/users/login.html', title='Login', form=form)

@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/logout')
def logout():
  logout_user()
  return redirect(url_for('gd_course_NHH_2024_group2.home_home'))

# Methodology
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/methodology')
def methodology_home():
  return render_template('gd_course/NHH_2024_group2/methodology.html', title='Methodology')

# About us
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/about_us')
def about_us_home():
  return render_template('gd_course/NHH_2024_group2/about_us.html', title='About us')


#Carbon app, main page
# Emissions factor per transport in kg per passemger km
efco2={'Car: Small':{'Petrol':0.1462,'Diesel':0.1197,'Electric':0.0414},
    'Car: SUV':{'Petrol':0.2088,'Diesel':0.1835,'Electric':0.0477},
    'Domestic Flight':{'Not my choice':0.246},
    'Long-haul Flight':{'Not my choice':0.1480},
    'Bus':{'Not my choice':0.097},
    'Long distance bus (Coach)':{'Not my choice':0.027},
    'Tram':{'Not my choice':0.029},
    'Train':{'Not my choice':0.035},
    'Ferry':{'Not my choice':0.019},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}

@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app')
#@login_required
def carbon_app_home():
    return render_template('gd_course/NHH_2024_group2/carbon_app/carbon_app.html', title='carbon_app')


# New entry bus
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_bus', methods=['GET','POST'])
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

        co2 = round(co2, 2)
        total =co2

        if float(kms) <= 15:
            saved = co2
            message = f"You could have saved {saved} by taking the bicycle or walking"
        else:
            saved = float(kms) - efco2['Tram'][fuel]
            saved2 = float(kms) * efco2['Train'][fuel]
            message = f"You could have saved {saved} by taking the tram and {saved2} by taking the train"
    

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_bus.html', title='new entry bus', form=form)

#New entry car small
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        people = form.people.data
        transport = 'Car: Small'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / float(people)
        #ch4 = float(kms) * efch4[transport][fuel]
        #total = co2+ch4

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)
        total =co2
        #ch4 = float("{:.2f}".format(ch4))
        #total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_car.html', title='new entry car', form=form)    

#New entry car SUV
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_carSUV', methods=['GET','POST'])
@login_required
def new_entry_carSUV():
    form = CarFormSUV()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        people = form.people.data
        transport = 'Car: SUV'
        # kms = request.form['kms']
        # fuel = request.form['fuel_type']

        co2 = (float(kms) * efco2[transport][fuel]) / float(people)
        #ch4 = float(kms) * efch4[transport][fuel]
        #total = co2+ch4

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)
        total =co2

        #ch4 = float("{:.2f}".format(ch4))
        #total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_carSUV.html', title='new entry car SUV', form=form) 

#New entry Domestic Flight
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_domestic_flight', methods=['GET','POST'])
@login_required
def new_entry_domestic_flight():
    form = Domestic_FlightForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Domestic Flight'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        total =co2
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_domestic_flight.html', title='new entry domestic flight', form=form)

#New entry Long-haul Flight
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_long_haul_flight', methods=['GET','POST'])
@login_required
def new_entry_long_haul_flight():
    form = Long_haul_FlightForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Long-haul Flight'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        total =co2
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_long_haul_flight.html', title='new entry Long-haul Flight', form=form)

#New entry Long distance bus (Coach) 
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_long_distance_bus', methods=['GET','POST'])
@login_required
def new_entry_long_distance_bus():
    form = long_distance_busForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Long distance bus (Coach)'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        total =co2
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_long_distance_bus.html', title='new entry long distance bus (Coach)', form=form)

#New entry Tram 
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_tram', methods=['GET','POST'])
@login_required
def new_entry_tram():
    form = tramForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Tram'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        total =co2
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_tram.html', title='new entry tram', form=form)

#New entry Train 
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = trainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        total =co2
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_train.html', title='new entry train', form=form)

#New entry Ferry 
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        total =co2
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)


#New entry Bicycle
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        total =co2
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry Walk
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'

        co2 = float(kms) * efco2[transport][fuel]

        #co2 = float("{:.2f}".format(co2))
        co2 = round(co2, 2)

        total =co2
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2024_group2', institution='NHH_2024_group2', year=2024, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    return render_template('gd_course/NHH_2024_group2/carbon_app/new_entry_walk.html', title='new entry walk', form=form)


# Your data
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/your_data')
@login_required
def your_data():
    #Table
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='NHH_2024_group2').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    
    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group2').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Car: Small' in second_tuple_elements:
        index_car_small = second_tuple_elements.index('Car: Small')
        emission_transport[0]=first_tuple_elements[index_car_small]
    else:
        emission_transport[0]

    if 'Car: SUV' in second_tuple_elements:
        index_car = second_tuple_elements.index('Car: SUV')
        emission_transport[1]=first_tuple_elements[index_car]
    else:
        emission_transport[1]

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        emission_transport[2]=first_tuple_elements[index_bus]
    else:
        emission_transport[2]  

    if 'Long distance bus (Coach)' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Long distance bus (Coach)')
        emission_transport[3]=first_tuple_elements[index_bus]
    else:
        emission_transport[3]   

    if 'Domestic Flight' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Domestic Flight')
        emission_transport[4]=first_tuple_elements[index_ferry]
    else:
        emission_transport[4]

    if 'Long-haul Flight' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Long-haul Flight')
        emission_transport[5]=first_tuple_elements[index_ferry]
    else:
        emission_transport[5]

    if 'Tram' in second_tuple_elements:
        index_tram = second_tuple_elements.index('Tram')
        emission_transport[6]=first_tuple_elements[index_tram]
    else:
        emission_transport[6]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[7]=first_tuple_elements[index_train]
    else:
        emission_transport[7]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        emission_transport[8]=first_tuple_elements[index_ferry]
    else:
        emission_transport[8]

    # Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group2').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Car: Small' in second_tuple_elements:
        index_car_small = second_tuple_elements.index('Car: Small')
        kms_transport[0]=first_tuple_elements[index_car_small]
    else:
        kms_transport[0]

    if 'Car: SUV' in second_tuple_elements:
        index_car_SUV = second_tuple_elements.index('Car: SUV')
        kms_transport[1]=first_tuple_elements[index_car_SUV]
    else:
        kms_transport[1]

    if 'Bus' in second_tuple_elements:
        index_bus = second_tuple_elements.index('Bus')
        kms_transport[2]=first_tuple_elements[index_bus]
    else:
        kms_transport[2]

    if 'Long distance bus (Coach)' in second_tuple_elements:
        index_car_SUV = second_tuple_elements.index('Long distance bus (Coach)')
        kms_transport[3]=first_tuple_elements[index_car_SUV]
    else:
        kms_transport[3]

    if 'Domestic Flight' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Domestic Flight')
        kms_transport[4]=first_tuple_elements[index_ferry]
    else:
        kms_transport[4]

    if 'Long-haul Flight' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Long-haul Flight')
        kms_transport[5]=first_tuple_elements[index_ferry]
    else:
        kms_transport[5]

    if 'Tram' in second_tuple_elements:
        index_tram = second_tuple_elements.index('Tram')
        kms_transport[6]=first_tuple_elements[index_tram]
    else:
        kms_transport[6]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[7]=first_tuple_elements[index_train]
    else:
        kms_transport[7]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        kms_transport[8]=first_tuple_elements[index_ferry]
    else:
        kms_transport[8]

    if 'Bicycle' in second_tuple_elements:
        index_bicycle = second_tuple_elements.index('Bicycle')
        kms_transport[9]=first_tuple_elements[index_bicycle]
    else:
        kms_transport[9] 

    if 'Walk' in second_tuple_elements:
        index_bicycle = second_tuple_elements.index('Walk')
        kms_transport[10]=first_tuple_elements[index_bicycle]
    else:
        kms_transport[10]    

    # Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group2').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    # Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2024_group2').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)

    #message 
    message = 'No availible data yet'
    latest_entry = db.session.query(EmissionsGD.co2, EmissionsGD.transport, EmissionsGD.kms).filter_by(author=current_user).order_by(EmissionsGD.date.desc()).first()
    latest_co2 = latest_entry[0] if latest_entry else None
    latest_transport = latest_entry[1] if latest_entry else None
    latest_kms = latest_entry[2] if latest_entry else None

    if latest_kms != None:
        if latest_kms <= 2:
            if latest_transport != 'Walk':
                message = f"If you would have chosen walking, you would produce {latest_co2} less kg of CO2-eq."
            else:
                message = "You made a good transportation choiche!"
           
        elif 2 < latest_kms <= 10:
            if latest_transport != 'Bicycle':
                message = f"You could have saved {latest_co2} kg of CO2-eq by biking."
            else:
                message = "You made a good transportation choiche!"
        elif 10 < latest_kms <= 25:
            if latest_transport != 'Ferry':
                ferry = latest_kms * efco2['Ferry']['Not my choice']
                saved = latest_co2 - ferry
                saved = round(saved, 2)
                if saved >= 0:
                    message = f"You could have saved {saved} kg of CO2-eq by taking the ferry."
                else:
                    message = "You made a good transportation choice!"
            else:
                message = "You made a good transportation choiche!"
        elif 25 < latest_kms <= 50:
            if latest_transport != 'Tram':
                tram = latest_kms * efco2['Tram']['Not my choice']
                saved = latest_co2 - tram
                saved = round(saved, 2)
                if saved >= 0:
                    message = f"You could have saved {saved} kg of CO2-eq by taking the tram."
                else:
                    message = "You made a good transportation choice!"
            else:
                message = "You made a good transportation choiche!"
        elif 50 < latest_kms <= 250:
            if latest_transport != 'Long distance bus (Coach)':
                long_distance_bus_coach = latest_kms * efco2['Long distance bus (Coach)']['Not my choice']
                saved = latest_co2 - long_distance_bus_coach 
                saved = round(saved, 2)
                if saved >= 0:
                    message = f"You could have saved {saved} kg of CO2-eq by taking the long distance bus (Coach)."
                else:
                    message = "You made a good transportation choice!"
            else:
                message = "You made a good transportation choiche!"
        elif 250 < latest_kms:
            if latest_transport != 'Train':
                train = latest_kms * efco2['Train']['Not my choice']
                saved = latest_co2 - train
                saved = round(saved, 2)
                if saved >= 0:
                    message = f"You could have saved {saved} kg of CO2-eq by taking the train."
                else:
                    message = "You made a good transportation choice!"               
            else:
                message = "You made a good transportation choiche!"
        else:
            message = "You made a good transportation choiche!"          

    return render_template('gd_course/NHH_2024_group2/carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label),
        message=message)

# Delete emission
@gd_course_NHH_2024_group2.route('/green_digitalization_course/NHH/2024/group2/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2024_group2.your_data'))
    

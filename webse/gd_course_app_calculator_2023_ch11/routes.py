from flask import render_template, Blueprint, redirect, flash, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from webse import db, bcrypt
from datetime import timedelta, datetime
from webse.models import User, EmissionsGD
from webse.gd_course_app_calculator_2023_ch11.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm

gd_course_app_carbon_app_2023_ch11=Blueprint('gd_course_app_carbon_app_2023_ch11',__name__)

# Home
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/home')
def home():
  return render_template('gd_course/chapters/ch11_home.html', title='home')

# Users
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_app_carbon_app_2023_ch11.home'))
  if form.validate_on_submit():
      user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='none')
      db.session.add(user)
      db.session.commit()
      flash('Your account has been created! Now, you are able to login!', 'success')
      return redirect(url_for('gd_course_app_carbon_app_2023_ch11.home'))
  return render_template('gd_course/chapters/ch11_register.html', title='register', form=form)

@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_app_carbon_app_2023_ch11.home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_app_carbon_app_2023_ch11.home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger') 
  return render_template('gd_course/chapters/ch11_login.html', title='login', form=form)

@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/logout')
def logout():    
    logout_user()
    return redirect(url_for('gd_course_app_carbon_app_2023_ch11.home'))

# Methodology
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/methodology')
def methodology():
  return render_template('gd_course/chapters/ch11_methodology.html', title='methodology')

# Carbon_app
#Emissions factor per transport in kg per passemger km
#Data from: http://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D
efco2={'Bus':{'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0},
    'Car':{'Petrol':0.18592,'Diesel':0.16453,'No Fossil Fuel':0},
    'Plane':{'Petrol':0.24298},
    'Ferry':{'Diesel':0.11131, 'CNG':0.1131, 'No Fossil Fuel':0},
    'Motorbike':{'Petrol':0.09816,'No Fossil Fuel':0},
    'Scooter':{'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}
efch4={'Bus':{'Diesel':2e-5,'CNG':2.5e-3,'Petrol':2e-5,'No Fossil Fuel':0},
    'Car':{'Petrol':3.1e-4,'Diesel':3e-6,'No Fossil Fuel':0},
    'Plane':{'Petrol':1.1e-4},
    'Ferry':{'Diesel':3e-5, 'CNG':3e-5,'No Fossil Fuel':0},
    'Motorbike':{'Petrol':2.1e-3,'No Fossil Fuel':0},
    'Scooter':{'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}

@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/carbon_app')
def carbon_app():
    return render_template('gd_course/chapters/ch11_carbon_app.html', title='gd_course_app_carbon_app_2023_ch11')

#New entry bus
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user, 
                student='none', institution='none', year=2023)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_app_carbon_app_2023_ch11.your_data'))
    return render_template('gd_course/chapters/ch11_new_entry_bus.html', title='new entry bus', form=form)

#New entry car
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user, 
                student='none', institution='none', year=2023)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_app_carbon_app_2023_ch11.your_data'))
    return render_template('gd_course/chapters/ch11_new_entry_car.html', title='new entry car', form=form)    

#New entry plane
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/carbon_app/new_entry_plane', methods=['GET','POST'])
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

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user, 
                student='none', institution='none', year=2023)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_app_carbon_app_2023_ch11.your_data'))
    return render_template('gd_course/chapters/ch11_new_entry_plane.html', title='new entry plane', form=form)  

#New entry ferry
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/carbon_app/new_entry_ferry', methods=['GET','POST'])
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

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user, 
                student='none', institution='none', year=2023)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_app_carbon_app_2023_ch11.your_data'))
    return render_template('gd_course/chapters/ch11_new_entry_ferry.html', title='new entry ferry', form=form)     

#New entry motorbike
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/carbon_app/new_entry_motorbike', methods=['GET','POST'])
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

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user, 
                student='none', institution='none', year=2023)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_app_carbon_app_2023_ch11.your_data'))
    return render_template('gd_course/chapters/ch11_new_entry_motorbike.html', title='new entry motorbike', form=form) 

#New entry bicycle
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/carbon_app/new_entry_bicycle', methods=['GET','POST'])
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

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user, 
                student='none', institution='none', year=2023)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_app_carbon_app_2023_ch11.your_data'))
    return render_template('gd_course/chapters/ch11_new_entry_bicycle.html', title='new entry bicycle', form=form)

#New entry walk
@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/carbon_app/new_entry_walk', methods=['GET','POST'])
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

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user, 
                student='none', institution='none', year=2023)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('carbon_app.your_data'))
    return render_template('gd_course/chapters/ch11_new_entry_walk.html', title='new entry walk', form=form)

@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_app_carbon_app_2023_ch11.your_data'))

@gd_course_app_carbon_app_2023_ch11.route('/green_digitalization_course/app_calculator/2023/ch11/your_data')
def your_data():
    #Table  
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).filter(EmissionsGD.student=='none').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    return render_template('gd_course/chapters/ch11_your_data.html', title='your_data', entries=entries)
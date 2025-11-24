from flask import render_template, Blueprint, redirect, flash, url_for, request, session, jsonify, abort
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
from webse.gd_course_HVL_2025_group3.forms import RegistrationForm, LoginForm, BusForm, CarForm, PlaneForm, TrainForm, FerryForm, MotorcycleForm
import flask 
from sqlalchemy import cast, Date, func, distinct, and_
import json


gd_course_HVL_2025_group3=Blueprint('gd_course_HVL_2025_group3',__name__)


#Users routes
@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='HVL_2025_group3')
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_HVL_2025_group3.calculator_home'))
    return render_template('gd_course/HVL_2025_group3/register.html', title='register', form=form)
    
@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use carbon app!', 'success')
        return redirect (next_page) if next_page else redirect(url_for('gd_course_HVL_2025_group3.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('gd_course/HVL_2025_group3/login.html', title='login', form=form)

@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3/logout')
def logout ():
   flash('You have logged out!', 'success') 
   logout_user()
   return redirect(url_for('gd_course_HVL_2025_group3.home_home'))

@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3/home')
def home_home():
  return render_template('gd_course/HVL_2025_group3/home.html')

@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3/aboutus')
def aboutus_home():
  return render_template('gd_course/HVL_2025_group3/aboutus.html', title='aboutus')

@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//foryou')
def foryou_home():
    return render_template('gd_course/HVL_2025_group3/foryou.html')

fco2 = {

    "Car": {
        "Diesel":     {"Small": 58,  "Medium": 76,  "Large": 101, "Camper": 149},
        "Gasoline":   {"Small": 50,  "Medium": 66,  "Large": 87,  "Camper": 129},
        "Electricity Nordic": {"Small": 15, "Medium": 20, "Large": 26, "Camper": 36},
        "Fossil gas": {"Small": 51,  "Medium": 68,  "Large": 89,  "Camper": 132},
        "Vehicle gas": {"Small": 6.8, "Medium": 9.0, "Large": 12, "Camper": 18},
        "Biogas":     {"Small": 6.6, "Medium": 8.6, "Large": 11, "Camper": 17},
        "Ethanol":    {"Small": 23,  "Medium": 31,  "Large": 40, "Camper": 60}
    },

    "Bus": {
        "Diesel": 30,
        "Biofuel HVO100": 3.5,
        "Biofuel FAME100": 11
    },

    "Train": {
        "Electricity Nordic": 7,
        "Diesel": 91,
        "Biofuel HVO100": 10
    },

    "Ferry": {
        "Standard fuel (186)": 186,
        "Standard fuel (377)": 377
    },

    "Motorcycle": {
        "Small": 85.0,
        "Medium": 103.2,
        "Large": 137.2
    },

    "Plane": {
        "Scheduled": {
            "Standard fuel": {"Economy": 127, "Premium": 155, "Business": 284},
            "100% biofuel": {"Economy": 51, "Premium": 63, "Business": 115}
        },
        "Charter": {
            "Standard fuel": {"Economy": 112, "Premium": 137},
            "100% biofuel": {"Economy": 45, "Premium": 56}
        }
    }
}


@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator', methods=['GET'])
@login_required
def calculator_home():
    return render_template('gd_course/HVL_2025_group3/calculator/calculator_home.html', title='Calculator')



@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator/new_entry_car', methods=['GET', 'POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        size = form.vehicle_size.data

        factor = fco2["Car"][fuel][size]
        total = kms * factor

        entry = EmissionsGD(kms=kms, transport="Car", fuel=f"{fuel} ({size})", co2=round(total, 2), total=round(total, 2), 
                                student='HVL_2025_group3', institution='HVL_2025_group3', year=2025, author=current_user)

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group3.your_data'))

    return render_template('gd_course/HVL_2025_group3/calculator/new_entry_car.html', title="Car Calculator", form=form)



@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator/new_entry_bus', methods=['GET', 'POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data

        factor = fco2["Bus"][fuel]
        total = kms * factor

        entry = EmissionsGD(kms=kms, transport="Bus", fuel=fuel, co2=round(total, 2), total=round(total, 2), 
                                student='HVL_2025_group3', institution='HVL_2025_group3', year=2025, author=current_user)

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group3.your_data'))

    return render_template('gd_course/HVL_2025_group3/calculator/new_entry_bus.html', title="Bus Calculator", form=form)



@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator/new_entry_train', methods=['GET', 'POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data

        factor = fco2["Train"][fuel]
        total = kms * factor

        entry = EmissionsGD(kms=kms, transport="Train", fuel=fuel, co2=round(total, 2), total=round(total, 2), 
                                student='HVL_2025_group3', institution='HVL_2025_group3', year=2025, author=current_user)

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group3.your_data'))

    return render_template('gd_course/HVL_2025_group3/calculator/new_entry_train.html', title="Train Calculator", form=form)



@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator/new_entry_ferry', methods=['GET', 'POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data

        factor = fco2["Ferry"][fuel]
        total = kms * factor
        
        entry = EmissionsGD(kms=kms, transport="Ferry", fuel=fuel, co2=round(total, 2), total=round(total, 2), 
                                student='HVL_2025_group3', institution='HVL_2025_group3', year=2025, author=current_user)

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group3.your_data'))

    return render_template('gd_course/HVL_2025_group3/calculator/new_entry_ferry.html', title="Ferry Calculator", form=form)




@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator/new_entry_motorcycle', methods=['GET', 'POST'])
@login_required
def new_entry_motorcycle():
    form = MotorcycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        size = form.fuel_type.data 

        factor = fco2["Motorcycle"][size]
        total = kms * factor

        entry = EmissionsGD(kms=kms, transport="Bus", fuel=size, co2=round(total, 2), total=round(total, 2), 
                                student='HVL_2025_group3', institution='HVL_2025_group3', year=2025, author=current_user)

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group3.your_data'))

    return render_template('gd_course/HVL_2025_group3/calculator/new_entry_motorcycle.html', title="Motorcycle Calculator", form=form)


@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator/new_entry_plane', methods=['GET', 'POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        ground_dep = form.ground_dep.data
        ground_arr = form.ground_arr.data
        flight_type = form.flight_type.data
        seat_class = form.seat_class.data

        fuel_type = "Standard fuel"  # par défaut

        factor = fco2["Plane"][flight_type][fuel_type][seat_class]
        total = (kms * factor) + (ground_dep + ground_arr) * 44

        entry = EmissionsGD(kms=kms, transport="Plane", fuel=f"{fuel_type} ({flight_type}/{seat_class})", co2=round(total, 2), total=round(total, 2), 
                                student='HVL_2025_group3', institution='HVL_2025_group3', year=2025, author=current_user)

        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group3.your_data'))

    return render_template('gd_course/HVL_2025_group3/calculator/new_entry_plane.html', title="Plane Calculator", form=form)



@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator/your_data')
@login_required
def your_data():
    five_days_ago = datetime.now() - timedelta(days=5)

    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> five_days_ago).\
        filter(EmissionsGD.institution=='HVL_2025_group3').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()


    transports_list = ['Bus', 'Car', 'Train', 'Ferry', 'Motorcycle', 'Plane']

    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > five_days_ago).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group3').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()

    emission_transport_dict = {t: 0 for t in transports_list}
    for total, transport in emissions_by_transport:
        emission_transport_dict[transport] = float(total)

    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > five_days_ago).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group3').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()

    kms_transport_dict = {t: 0 for t in transports_list}
    for total, transport in kms_by_transport:
        kms_transport_dict[transport] = float(total)

    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > five_days_ago).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group3').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()

    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        over_time_emissions.append(float(total))
        dates_label.append(date.strftime('%m-%d-%Y'))

    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group3').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()

    over_time_kms = []
    for total, date in kms_by_date:
        over_time_kms.append(float(total))

    return render_template('gd_course/HVL_2025_group3/calculator/your_data.html',
        title='Your Data',
        entries=entries,
        transports=transports_list,
        emission_transport=list(emission_transport_dict.values()),
        kms_transport=list(kms_transport_dict.values()),
        over_time_emissions=over_time_emissions,
        over_time_kms=over_time_kms,
        dates_label=dates_label
    )


@gd_course_HVL_2025_group3.route('/green_digitalization_course/HVL/2025/group3//calculator/delete_emissions/<int:entry_id>')
@login_required
def delete_emissions(entry_id):
    entry = EmissionsGD.query.get_or_404(entry_id)

    if entry.user_id != current_user.id:
        abort(403)

    db.session.delete(entry)
    db.session.commit()

    flash('Entry deleted!', 'success')
    return redirect(url_for('gd_course_HVL_2025_group3.your_data'))


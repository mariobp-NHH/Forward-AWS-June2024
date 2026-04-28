from flask import render_template, Blueprint
from webse.models import User, EmissionsGD
from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse import db, bcrypt
from webse.gd_course_NHH_2026_group3.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user
from flask import render_template, Blueprint, request, redirect, url_for, flash
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from webse.gd_course_NHH_2026_group3.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm, TrainForm
import json
from webse.gd_course_NHH_2026_group3.functions import efco2, carbon_emissions

gd_course_NHH_2026_group3=Blueprint('gd_course_NHH_2026_group3',__name__)

@gd_course_NHH_2026_group3.route("/green_digitalization_course/NHH/2026/group3/home")
def home_home():
   
    user = User.query.filter_by(username="Bjørk").first()

    if not user:
        return render_template(
            "gd_course/NHH_2026_group3/home.html",
            user_name="Bjørk",
            user_transports=[],
            kms=None,
            max_kms=None,
            co2=None,
            co2_kms=None,
            max_co2_kms=None,
            transport_type=None,
            transport_max_co2_kms=None,
        )

    user_transports = EmissionsGD.query.filter_by(user_id=user.id).all()

    first_transport = user_transports[0] if user_transports else None

    
    kms = round(first_transport.kms, 2) if first_transport and first_transport.kms is not None else None

 
    max_kms = max((t.kms for t in user_transports if t.kms is not None), default=None)

    
    co2 = round(first_transport.co2, 2) if first_transport and first_transport.co2 is not None else None
    co2_kms = (
        round(first_transport.co2 / first_transport.kms, 2)
        if first_transport
        and first_transport.co2 is not None
        and first_transport.kms not in (None, 0)
        else None
    )

   
    valid_transports = [
        t for t in user_transports
        if t.co2 is not None and t.kms not in (None, 0)
    ]

    transport_with_max_co2_kms = (
        max(valid_transports, key=lambda t: t.co2 / t.kms)
        if valid_transports else None
    )

    max_co2_kms = (
        round(transport_with_max_co2_kms.co2 / transport_with_max_co2_kms.kms, 2)
        if transport_with_max_co2_kms else None
    )

    transport_type = (
        transport_with_max_co2_kms.transport
        if transport_with_max_co2_kms else None
    )

    transport_max_co2_kms = max_co2_kms

    return render_template(
        "gd_course/NHH_2026_group3/home.html",
        user_name=user.username,
        user_transports=user_transports,
        kms=kms,
        max_kms=max_kms,
        co2=co2,
        co2_kms=co2_kms,
        max_co2_kms=max_co2_kms,
        transport_type=transport_type,
        transport_max_co2_kms=transport_max_co2_kms,
    )


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/register', methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2026_group3')
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! Now, you are able to login!', 'success')
    return redirect(url_for('gd_course_NHH_2026_group3.home_home'))
  return render_template('gd_course/NHH_2026_group3/users/register.html', title='register', form=form)

@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
     return redirect(url_for("gd_course_NHH_2026_group3.home_home"))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page=request.args.get("next")
        flash('You have logged in! Now, you can start to use carbon app!', 'success')
        return redirect(next_page) if next_page else redirect(url_for("gd_course_NHH_2026_group3.home_home"))
        return redirect(url_for('gd_course_NHH_2026_group3.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('gd_course/NHH_2026_group3/users/login.html', title='login', form=form)

@gd_course_NHH_2026_group3.route("/green_digitalization_course/NHH/2026/group3/logout")
def logout():
   logout_user()
   return redirect(url_for("gd_course_NHH_2026_group3.home_home"))



@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app')
@login_required
def carbon_app_home():
    return render_template('gd_course/NHH_2026_group3/carbon_app/carbon_app.html', title='carbon_app')


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/new_entry_bus', methods=['GET','POST'])
@login_required
def new_entry_bus():
    form = BusForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bus'
        
        co2, total = carbon_emissions(kms, transport, fuel)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group3', institution='NHH_2026_group3', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group3.your_data'))
    return render_template('gd_course/NHH_2026_group3/carbon_app/new_entry_bus.html', title='new entry bus', form=form)

@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/new_entry_train', methods=['GET','POST'])
@login_required
def new_entry_train():
    form = TrainForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Train'
        
        co2, total = carbon_emissions(kms, transport, fuel)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group3', institution='NHH_2026_group3', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group3.your_data'))
    return render_template('gd_course/NHH_2026_group3/carbon_app/new_entry_train.html', title='new entry train', form=form)


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/new_entry_car', methods=['GET','POST'])
@login_required
def new_entry_car():
    form = CarForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Car'
        
        co2, total = carbon_emissions(kms, transport, fuel)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group3', institution='NHH_2026_group3', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group3.your_data'))
    return render_template('gd_course/NHH_2026_group3/carbon_app/new_entry_car.html', title='new entry car', form=form)    


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/new_entry_plane', methods=['GET','POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Plane'
        
        co2, total = carbon_emissions(kms, transport, fuel)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group3', institution='NHH_2026_group3', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group3.your_data'))
    return render_template('gd_course/NHH_2026_group3/carbon_app/new_entry_plane.html', title='new entry plane', form=form)  


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/new_entry_ferry', methods=['GET','POST'])
@login_required
def new_entry_ferry():
    form = FerryForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Ferry'
        
        co2, total = carbon_emissions(kms, transport, fuel)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group3', institution='NHH_2026_group3', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group3.your_data'))
    return render_template('gd_course/NHH_2026_group3/carbon_app/new_entry_ferry.html', title='new entry ferry', form=form)     


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/new_entry_motorbike', methods=['GET','POST'])
@login_required
def new_entry_motorbike():
    form = MotorbikeForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Motorbike'
        
        co2, total = carbon_emissions(kms, transport, fuel)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group3', institution='NHH_2026_group3', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group3.your_data'))
    return render_template('gd_course/NHH_2026_group3/carbon_app/new_entry_motorbike.html', title='new entry motorbike', form=form) 


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/new_entry_bicycle', methods=['GET','POST'])
@login_required
def new_entry_bicycle():
    form = BicycleForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Bicycle'
        
        co2, total = carbon_emissions(kms, transport, fuel)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group3', institution='NHH_2026_group3', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group3.your_data'))
    return render_template('gd_course/NHH_2026_group3/carbon_app/new_entry_bicycle.html', title='new entry bicycle', form=form)


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/new_entry_walk', methods=['GET','POST'])
@login_required
def new_entry_walk():
    form = WalkForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        transport = 'Walk'
        
        co2, total = carbon_emissions(kms, transport, fuel)

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='NHH_2026_group3', institution='NHH_2026_group3', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group3.your_data'))
    return render_template('gd_course/NHH_2026_group3/carbon_app/new_entry_walk.html', title='new entry walk', form=form)


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/your_data')
@login_required
def your_data():
   
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='NHH_2026_group3').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    
 
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.institution=='NHH_2026_group3').\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0]
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

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        emission_transport[6] = first_tuple_elements[index_train]
    else:
        emission_transport[6]

   
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2026_group3').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0]
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

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[6] = first_tuple_elements[index_train]
    else:
        kms_transport[6]   

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        kms_transport[7]=first_tuple_elements[index_walk]
    else:
        kms_transport[7]    


    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2026_group3').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

   
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2026_group3').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)      


    return render_template('gd_course/NHH_2026_group3/carbon_app/your_data.html', title='your_data', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))


@gd_course_NHH_2026_group3.route('/green_digitalization_course/NHH/2026/group3/carbon_app/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2026_group3.your_data'))





from flask import render_template, Blueprint, redirect, flash, url_for, request, session, jsonify
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
from webse.gd_course_HVL_2025_group2.forms import RegistrationForm, LoginForm, TransportForm
import json
import flask 
from sqlalchemy import cast, Date, func, distinct, and_


gd_course_HVL_2025_group2=Blueprint('gd_course_HVL_2025_group2',__name__)


#Users routes
@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('gd_course_HVL_2025_group2.home_home'))
    if form.validate_on_submit():
        user_hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='HVL_2025_group2')
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_HVL_2025_group2.carbon_app_home'))
    return render_template('gd_course/HVL_2025_group2/users/register.html', title='register', form=form)
    
@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
    return redirect(url_for('gd_course_HVL_2025_group2.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use carbon app!', 'success')
        return redirect (next_page) if next_page else redirect(url_for('gd_course_HVL_2025_group2.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger')  
  return render_template('gd_course/HVL_2025_group2/users/login.html', title='login', form=form)

@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/logout')
def logout ():
   flash('You have logged out!', 'success') 
   logout_user()
   return redirect(url_for('gd_course_HVL_2025_group2.home_home'))

@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/home')
def home_home():
  return render_template('gd_course/HVL_2025_group2/home.html')

@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/methodology')
def methodology_home():
  return render_template('gd_course/HVL_2025_group2/methodology.html', title='methodology')

@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/about_us')
def about_us_home():
  return render_template('gd_course/HVL_2025_group2/About_us.html', title='About Us')

#dictionary
efco2={'Bus':{'Diesel':0.03, 'Electric':0.013},
       'Car':{'Diesel':0.229, 'Petrol': 0.198, 'Electric':0.059},
       'Motorbike':{'Fossil fuel':0.095},
       'Train':{'Diesel':0.091,'Electric':0.007},
       'Plane Economy':{'Jetfuel':0.127},
       'Plane Business':{'Jetfuel':0.284},
       'Ferry':{'Fossil fuel':0.186, 'Electric':0.023},
       'Bybane':{'Electric':0.0015},
       'Walking/Cycling':{'Human powered':0}
}



@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/carbon_app', methods=['GET','POST'])
@login_required
def carbon_app_home():
    form =TransportForm()
    if form.validate_on_submit():
        kms=form.kms.data
        fuel=form.fuel_type.data
        transport= form.transport.data
        
        passengers = form.passenger.data if form.passenger.data else 1
        
        co2=float(kms)*efco2[transport][fuel]
        
        if transport in ["Car","Motorbike"]:
            co2 = co2 / passengers
        
        total = co2
        co2=float("{:.2f}".format(co2))
        total=float("{:.2f}".format(total))
        emissions=EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, total=total, student='HVL_2025_group2', institution='HVL_2025_group2', year=2025, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_HVL_2025_group2.your_data'))
    return render_template('gd_course/HVL_2025_group2/carbon_app/carbon_app.html', title='Carbon App', form=form)


#Viser brukeren dataen siste 5 dagene og sorterer etter nyest til gamlest
@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/carbon_app/your_data')
@login_required
def your_data():
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='HVL_2025_group2').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    

    #sier til databasen "add alle co2 tall sammen men sorter dem etter transport type", så summen av totale buss utslipp, summen av totale bil utslipp, ect
    #Bruker bare siste 5 dager
    #Grupperer transport sammen og alfabetisk for pie diagrammet
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group2').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()

    # Konverterer data til lister
    emission_dict = {}
    for value, transport in emissions_by_transport:
        emission_dict[transport] = value

    emission_value = list(emission_dict.values())
    emissions_lable = list(emission_dict.keys())

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group2').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    #for kilometers     
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group2').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()

    # kms transport pie chart
    kms_dict = {}
    for value, transport in kms_by_transport:
        kms_dict[transport] = value

    kms_values = list(kms_dict.values())
    kms_lable = list(kms_dict.keys())


        # Kilometers by date
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='HVL_2025_group2').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()

    kms_over_time = []
    for kms, date in kms_by_date:
        kms_over_time.append(kms)


#sender til html via json
    return render_template('gd_course/HVL_2025_group2/carbon_app/your_data.html', title='your_data', 
        entries=entries,
        emissions_by_transport=json.dumps(emission_value),
        transport_labels=json.dumps(emissions_lable),
        over_time_emissions=json.dumps(over_time_emissions),
        dates_label=json.dumps(dates_label),
        kms_over_time=json.dumps(kms_over_time),
        kms_by_transport=json.dumps(kms_values),
        kms_labels=json.dumps(kms_lable))
    

#Sletter fra databasen hvis brukeren ønsker det
@gd_course_HVL_2025_group2.route('/green_digitalization_course/HVL/2025/group2/carbon_app/delete_emissions/<int:entry_id>')
def delete_emission(entry_id):
    entry=EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted","sucsess")
    return redirect(url_for('gd_course_HVL_2025_group2.your_data'))

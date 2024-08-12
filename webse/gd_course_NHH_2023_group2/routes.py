from flask import render_template, Blueprint, redirect, flash, url_for, request
from webse.gd_course_NHH_2023_group2.forms import RegistrationForm, LoginForm, RegForm
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
import json

gd_course_NHH_2023_group2=Blueprint('gd_course_NHH_2023_group2',__name__)

#Home routes
@gd_course_NHH_2023_group2.route('/green_digitalization_course/NHH/2023/group2/home')
def home_func():
  return render_template('gd_course/NHH_2023_group2/home.html', title = 'Home')

#Users routes
@gd_course_NHH_2023_group2.route('/green_digitalization_course/NHH/2023/group2/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2023_group2')
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Login to use our app.', 'success')
        return redirect(url_for('gd_course_NHH_2023_group2.login'))
    return render_template('gd_course/NHH_2023_group2/users/register.html', title='Register', form=form)

@gd_course_NHH_2023_group2.route('/green_digitalization_course/NHH/2023/group2/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if current_user.is_authenticated:
     return redirect(url_for('@gd_course_NHH_2023_group2.home_func'))
  error = None
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data) :
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2023_group2.home_func'))
    else:
      error = 'Wrong Credentials. Please try again.'
  return render_template('gd_course/NHH_2023_group2/users/login.html', title='Login', form=form, error=error)

@gd_course_NHH_2023_group2.route('/green_digitalization_course/NHH/2023/group2/logout')
def logout():
  logout_user()
  return redirect(url_for('gd_course_NHH_2023_group2.home_func'))

# Methodology
@gd_course_NHH_2023_group2.route('/green_digitalization_course/NHH/2023/group2/methodology')
def methodology_func():
  return render_template('gd_course/NHH_2023_group2/methodology.html', title='Methodology')

# Carbon App
@gd_course_NHH_2023_group2.route('/green_digitalization_course/NHH/2023/group2/carbon_calculator')
@login_required
def carbon_calculator_func():
        #Table
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='NHH_2023_group2').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()
    
    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2023_group2').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    emission_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Walking' in second_tuple_elements:
        index_walking = second_tuple_elements.index('Walking')
        emission_transport[0]=first_tuple_elements[index_walking]
    else:
        emission_transport[0]

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

    if 'Motorcycle' in second_tuple_elements:
        index_motorcycle = second_tuple_elements.index('Motorcycle')
        emission_transport[4]=first_tuple_elements[index_motorcycle]
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

    if 'Tram' in second_tuple_elements:
        index_tram = second_tuple_elements.index('Tram')
        emission_transport[7]=first_tuple_elements[index_tram]
    else:
        emission_transport[7]

    if 'Metro' in second_tuple_elements:
        index_metro = second_tuple_elements.index('Metro')
        emission_transport[8]=first_tuple_elements[index_metro]
    else:
        emission_transport[8]
  
    if 'Bike' in second_tuple_elements:
        index_bike = second_tuple_elements.index('Bike')
        emission_transport[9]=first_tuple_elements[index_bike]
    else:
        emission_transport[9]

    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2023_group2').\
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Walking' in second_tuple_elements:
        index_walking = second_tuple_elements.index('Walking')
        kms_transport[0]=first_tuple_elements[index_walking]
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

    if 'Motorcycle' in second_tuple_elements:
        index_motorcycle = second_tuple_elements.index('Motorcycle')
        kms_transport[4]=first_tuple_elements[index_motorcycle]
    else:
        kms_transport[4]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        kms_transport[5]=first_tuple_elements[index_plane]
    else:
        kms_transport[5]

    if 'Train' in second_tuple_elements:
        index_train = second_tuple_elements.index('Train')
        kms_transport[6]=first_tuple_elements[index_train]
    else:
        kms_transport[6]     

    if 'Tram' in second_tuple_elements:
        index_tram = second_tuple_elements.index('Tram')
        kms_transport[7]=first_tuple_elements[index_tram]
    else:
        kms_transport[7]   

    if 'Metro' in second_tuple_elements:
        index_metro = second_tuple_elements.index('Metro')
        kms_transport[8]=first_tuple_elements[index_metro]
    else:
        kms_transport[8]
    
    if 'Bike' in second_tuple_elements:
        index_bike = second_tuple_elements.index('Bike')
        kms_transport[9]=first_tuple_elements[index_bike]
    else:
        kms_transport[9]

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2023_group2').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)    

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        filter(EmissionsGD.institution=='NHH_2023_group2').\
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)      


    return render_template('gd_course/NHH_2023_group2/carbon_calculator/carbon_calculator.html', title='carbon calculator', entries=entries,
        emissions_by_transport_python_dic=emissions_by_transport,     
        emission_transport_python_list=emission_transport,             
        emissions_by_transport=json.dumps(emission_transport),
        kms_by_transport=json.dumps(kms_transport),
        over_time_emissions=json.dumps(over_time_emissions),
        over_time_kms=json.dumps(over_time_kms),
        dates_label=json.dumps(dates_label))

@gd_course_NHH_2023_group2.route('/green_digitalization_course/NHH/2023/group2/carbon_calculator/new_entry', methods=['GET','POST'])
@login_required
def new_entry():
    form = RegForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel.data
        transport = form.transport.data
        total = float(kms)*co2eqIDX[transport][fuel]
        total = round(total,1)
        emissions = EmissionsGD(kms=kms, fuel=fuel, transport=transport,total=total, student='NHH_2023_group2', institution='NHH_2023_group2', year=2023, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2023_group2.your_data'))
    return render_template('gd_course/NHH_2023_group2/carbon_calculator/new_entry.html', title='New Entry', form=form)
#New Entries

#Dictionaries - emission factors:
co2eqIDX={}
co2eqIDX['Car'] = {'Diesel':141.8, 'Gas':155.5, 'Electric & Gas':88.4, 'Electric':7.3}
co2eqIDX['Bike']= {'Electric':0.2, 'No Fuel':0}
co2eqIDX['Walking']= {'No Fuel':0}
co2eqIDX['Bus'] = {'Diesel':93.8}
co2eqIDX['Motorcycle']={'Gas':163.5}
co2eqIDX['Metro']={'Electric':3.9}
co2eqIDX['Tram']= {'Electric':3.1}
co2eqIDX['Train']={'Electric':0.4}
co2eqIDX['Ferry']={'With_Car':1063.9, 'Without_Car':54.1}
co2eqIDX['Plane']={'Domestic':101}

      



@gd_course_NHH_2023_group2.route('/green_digitalization_course/NHH/2023/group2/carbon_calculator/your_data')
@login_required
def your_data():
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).\
        filter(EmissionsGD.institution=='NHH_2023_group2').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()  
    return render_template('gd_course/NHH_2023_group2/carbon_calculator/your_data.html', title='your_data', entries=entries)
#Delete emission
@gd_course_NHH_2023_group2.route('/carbon_calculator/delete_emissions/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry Deleted", "success")
    return redirect(url_for('gd_course_NHH_2023_group2.your_data'))
    

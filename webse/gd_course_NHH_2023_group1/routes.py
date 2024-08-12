from flask import render_template, Blueprint, redirect, flash, url_for, request, session, jsonify
from webse import db, bcrypt
from datetime import timedelta, datetime
from flask_login import login_required, login_user, current_user, logout_user
from webse.models import User, EmissionsGD
import json
import flask 
from sqlalchemy import cast, Date, func, distinct, and_

gd_course_NHH_2023_group1=Blueprint('gd_course_NHH_2023_group1',__name__)

#Home routes
@gd_course_NHH_2023_group1.route('/green_digitalization_course/NHH/2023/group1/home')
def home_home():
  return render_template('gd_course/NHH_2023_group1/home.html', title = 'Home')

#Users routes
@gd_course_NHH_2023_group1.route('/green_digitalization_course/NHH/2023/group1/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        data = request.form
        user_hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data["f:name"], email=data['email'], password=user_hashed_password, institution='NHH_2023_group1')
        # user_hasedh_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        # new_user = User((data["f:name"] +" " + data["l:name"]), data['email'], user_hasedh_password)
        db.session.add(new_user)
        db.session.commit()
        # login_user(User.valid_login(data["email"], data["password"]))
        flash(f'Your registration was successful. Welcome to our Carbon App!')
        session['logged_in'] = True
        return flask.redirect("/green_digitalization_course/NHH/2023/group1/home")
    return flask.render_template('gd_course/NHH_2023_group1/register.html', title='Register')

@gd_course_NHH_2023_group1.route('/green_digitalization_course/NHH/2023/group1/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        data = request.form
        print(f"Username: {data['email']}")
        print(f"Password: {data['password']}")

        if User.query.filter_by(email=data["email"]).first() and bcrypt.check_password_hash(User.query.filter_by(email=data["email"]).first().password, data["password"]):    
            flash(f'Login successful. Welcome back!')
            login_user(User.query.filter_by(email=data["email"]).first())
            session['logged_in'] = True
            return flask.redirect("/green_digitalization_course/NHH/2023/group1/home")
        else:
            flash("Login failed. Please enter correct email and password.")
            return flask.redirect('/green_digitalization_course/NHH/2023/group1/login')
    else:
        return flask.render_template('gd_course/NHH_2023_group1/login.html')

@gd_course_NHH_2023_group1.route('/green_digitalization_course/NHH/2023/group1/logout')
def logout():
  logout_user()
  session.clear()
  flash("Logout successful.")
  return redirect(url_for('gd_course_NHH_2023_group1.home_home'))

# Methodology
@gd_course_NHH_2023_group1.route('/green_digitalization_course/NHH/2023/group1/methodology')
def methodology_m():
  return render_template('gd_course/NHH_2023_group1/methodology.html', title='Methodology')

efco2={
        'Walk':{'No Fossil Fuel':0},
        'Bicycle':{'No Fossil Fuel':0},
        'Ferry':{'Diesel':0.019},
        'Train':{'Diesel':0.041,'Electric':0},
        'Car':{'Diesel':0.171, 'Gasoline':0.192, 'Hybrid':0.109, 'Electric':0.053},
        'Motorbike':{'Gasoline':0.103},
        'Bus':{'Diesel':0.105,'Electric':0},
        'Long distance flight':{'Jet Fuel':0.150},
        'Domestic flight':{'Jet Fuel':0.255},
        'Light rail and tram':{'Electric':0.035}
    }

efch4={
        'Walk':{'No Fossil Fuel':0},
        'Bicycle':{'No Fossil Fuel':0},
        'Ferry':{'Diesel':0},
        'Train':{'Diesel':0,'Electric':0},
        'Car':{'Diesel':0, 'Gasoline':0, 'Hybrid':0, 'Electric':0},
        'Motorbike':{'Gasoline':0,'No Fossil Fuel':0},
        'Bus':{'Diesel':0,'Electric':0},
        'Long distance flight':{'Jet Fuel':0},
        'Domestic flight':{'Jet Fuel':0},
        'Light rail and tram':{'Electric':0}
     }

transport_dict = {
    'bus': 'Bus',
    'car': 'Car',
    'plane': 'Long distance flight',
    'plane-up': 'Domestic flight',
    'ferry': 'Ferry',
    'motorcycle': 'Motorbike',
    'bicycle': 'Bicycle',
    'person-walking': 'Walk',
    'train': 'Train',
    'train-tram': 'Light rail and tram'
}

@gd_course_NHH_2023_group1.route("/green_digitalization_course/NHH/2023/group1/carbon_app")
@login_required
def carbon_application():
    return render_template("gd_course/NHH_2023_group1/carbon_app.html")

@gd_course_NHH_2023_group1.route("/green_digitalization_course/NHH/2023/group1/my_data/<arg>/<key>/<start>/<end>")
def my_data(arg, key, start, end):
    if start == 'undefined':
        start = datetime.now()
    else:
        start = start + " 23:59:59"
    if end == 'undefined':
        print('end is undefined')
        end = datetime.now() - timedelta(days=5)
    else:
        end = end + " 00:00:00"
    if int(key) == 0:
        if int(arg) == 1:
            emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
                filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)).filter_by(user_id=current_user.id). \
                filter(EmissionsGD.institution=='NHH_2023_group1').\
                group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
            emissions_by_transport_dict = {'labels': [], 'values': []}
            for i in emissions_by_transport:
                emissions_by_transport_dict['labels'].append(i[1])
                emissions_by_transport_dict['values'].append(i[0])
            print(emissions_by_transport_dict)
            return jsonify(emissions_by_transport_dict)
        elif int(arg) == 2:
            emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), func.date(EmissionsGD.date)). \
                filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)).filter_by(user_id=current_user.id). \
                filter(EmissionsGD.institution=='NHH_2023_group1').\
                group_by(func.date(EmissionsGD.date)).order_by(func.date(EmissionsGD.date).asc()).all()
            print(emissions_by_date)
            over_time_emissions = {'labels': [], 'values': []}
            for total, date in emissions_by_date:
                over_time_emissions['labels'].append(date)
                over_time_emissions['values'].append(total)
            print(over_time_emissions)
            return jsonify(over_time_emissions)
        elif int(arg) == 3:
            kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
            filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)).filter_by(user_id=current_user.id). \
            filter(EmissionsGD.institution=='NHH_2023_group1').\
            group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
            kms_by_transport_dict = {'labels': [], 'values': []}
            print(kms_by_transport)
            for i in kms_by_transport:
                kms_by_transport_dict['labels'].append(i[1])
                kms_by_transport_dict['values'].append(i[0])    
            return jsonify(kms_by_transport_dict)
        elif int(arg) == 4:
            print('here')
            kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), func.date(EmissionsGD.date)). \
            filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)).filter_by(user_id=current_user.id). \
            filter(EmissionsGD.institution=='NHH_2023_group1').\
            group_by(func.date(EmissionsGD.date)).order_by(func.date(EmissionsGD.date).asc()).all()
            over_time_kms = {'labels': [], 'values': []}
            for total, date in kms_by_date:
                print(type(date))
                over_time_kms['labels'].append(date)
                over_time_kms['values'].append(total)
            return jsonify(over_time_kms)
        elif int(arg) == 5:
            data = db.session.query(User.username, EmissionsGD.date, EmissionsGD.kms, EmissionsGD.transport, EmissionsGD.fuel, EmissionsGD.co2, EmissionsGD.id). \
            join(User, EmissionsGD.user_id == User.id).\
            filter(EmissionsGD.user_id ==  current_user.id).filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)). \
            filter(EmissionsGD.institution=='NHH_2023_group1').\
            order_by(EmissionsGD.date.desc()).all()
            list_data = []
            for i in data:
                list_data.append((i[0], str(i[1]), i[2], i[3], i[4], i[5], i[6]))
            print(list_data)
            return jsonify(list_data) 
    elif int(key) == 1:
        if int(arg) == 1:
            emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
                filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)). \
                filter(EmissionsGD.institution=='NHH_2023_group1').\
                group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
            emissions_by_transport_dict = {'labels': [], 'values': []}
            for i in emissions_by_transport:
                emissions_by_transport_dict['labels'].append(i[1])
                emissions_by_transport_dict['values'].append(i[0])
            return jsonify(emissions_by_transport_dict)
        elif int(arg) == 2:
            emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), func.date(EmissionsGD.date)). \
                filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)). \
                filter(EmissionsGD.institution=='NHH_2023_group1').\
                group_by(func.date(EmissionsGD.date)).order_by(func.date(EmissionsGD.date).asc()).all()
            print(emissions_by_date)
            over_time_emissions = {'labels': [], 'values': []}
            for total, date in emissions_by_date:
                over_time_emissions['labels'].append(date)
                over_time_emissions['values'].append(total)
            print(over_time_emissions)
            return jsonify(over_time_emissions)
        elif int(arg) == 3:
            kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
            filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)). \
            filter(EmissionsGD.institution=='NHH_2023_group1').\
            group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
            kms_by_transport_dict = {'labels': [], 'values': []}
            for i in kms_by_transport:
                kms_by_transport_dict['labels'].append(i[1])
                kms_by_transport_dict['values'].append(i[0])    
            return jsonify(kms_by_transport_dict)
        elif int(arg) == 4:
            print('here')
            kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), func.date(EmissionsGD.date)). \
            filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)). \
            filter(EmissionsGD.institution=='NHH_2023_group1').\
            group_by(func.date(EmissionsGD.date)).order_by(func.date(EmissionsGD.date).asc()).all()
            over_time_kms = {'labels': [], 'values': []}
            for total, date in kms_by_date:
                over_time_kms['labels'].append(date)
                over_time_kms['values'].append(total)
            return jsonify(over_time_kms)
        elif int(arg) == 5:
            data = db.session.query(User.username, EmissionsGD.date, EmissionsGD.kms, EmissionsGD.transport, EmissionsGD.fuel, EmissionsGD.co2, EmissionsGD.id). \
            join(User, EmissionsGD.user_id == User.id). \
            filter(and_(EmissionsGD.date <= start, EmissionsGD.date >=end)). \
            filter(EmissionsGD.institution=='NHH_2023_group1').\
            order_by(EmissionsGD.date.desc()).all()
            list_data = []
            for i in data:
                list_data.append((i[0], str(i[1]), i[2], i[3], i[4], i[5], i[6]))
            print(list_data)
            return jsonify(list_data) 
        
@gd_course_NHH_2023_group1.route("/green_digitalization_course/NHH/2023/group1/newEntry", methods=['GET', 'POST'])
@login_required
def newEntry():
    if request.method == 'POST':
        try:
            data = request.form
            transport = transport_dict[data['transport']]
            co2 = round(float(data['kms']) * efco2[transport][data['fuel']], 2)
            ch4 = round(float(data['kms']) * efch4[transport][data['fuel']],2)
            emissions = EmissionsGD(kms=data['kms'],transport=transport, fuel=data['fuel'],co2=co2,ch4=ch4,total= co2+ch4,student="NHH_2023_group1",institution= "NHH_2023_group1",year= 2023, author=current_user)
            db.session.add(emissions)
            db.session.commit()
            return jsonify({'success': "Data received successfully!"})
        except Exception as e:
            print(e)
            return jsonify({'error': str(e)})
    return render_template("gd_course/NHH_2023_group1/new_entry.html")

@gd_course_NHH_2023_group1.route("/green_digitalization_course/NHH/2023/group1/deleteEntry", methods=['GET', 'POST'])
@login_required
def deleteEntry():
    if request.method == "POST":
        #I want to delete an mysel entry
        try:
            data = request.form
            entry = EmissionsGD.query.filter_by(id=data['id']).first()
            db.session.delete(entry)
            db.session.commit()
            return jsonify({'success': "Entry deleted successfully!"})
        except Exception as e:
            return jsonify({'error': str(e)})
    

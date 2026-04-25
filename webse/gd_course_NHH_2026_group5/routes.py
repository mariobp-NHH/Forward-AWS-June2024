from flask import Flask, render_template, Blueprint, Response
from flask import Flask, flash, redirect, render_template, Blueprint, request, url_for
from webse.models import Transport_NHH_2026_g5
from flask_login import current_user, login_required
from webse import db, bcrypt
import csv
from io import StringIO
from flask import Flask, render_template, Blueprint, redirect, flash, request, url_for
from flask_login import current_user, login_user, logout_user
from webse.models import User
from webse.gd_course_NHH_2026_group5.forms import LoginForm, RegistrationForm


from webse.gd_course_NHH_2026_group5.emission_functions import carbon_emission, efco2
from webse.gd_course_NHH_2026_group5.table_functions import get_entries,format_entries_for_table, get_latest_entry, get_emissions_by_transport, get_kms_by_transport, get_emissions_by_date,get_kms_by_date
from webse.gd_course_NHH_2026_group5.chart_functions import get_categories_for_user_type,build_chart_values,format_date_chart,get_alternatives, alternatives_map

gd_course_NHH_2026_group5=Blueprint('gd_course_NHH_2026_group5',__name__)

@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/home')
def home_home():
  return render_template('gd_course/NHH_2026_group5/home.html')

@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/aboutUs')
def aboutUs_home():
    return render_template('gd_course/NHH_2026_group5/aboutUs.html', title='aboutUs')

@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/methodology')
def methodology_home():
  return render_template('gd_course/NHH_2026_group5/methodology.html', title='methodology')


@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/carbon_app')
def carbon_app_home():
    return render_template('gd_course/NHH_2026_group5/carbonCalculator/carbon_app.html', title='carbon_app')


@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/register', methods=['GET', 'POST'])
def register_home():
    form = RegistrationForm()
    
    if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2026_group5.home_home')) 
    
    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        users = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2026_group5')
        db.session.add(users)
        db.session.commit()
        flash('Your account has been created! You can login now!',
              'success')
        return redirect(url_for('gd_course_NHH_2026_group5.home_home'))
    return render_template('gd_course/NHH_2026_group5/user/register.html', title='register', form=form)


@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/login', methods=['GET','POST'])
def login_home():
  form = LoginForm()
  if current_user.is_authenticated:
        return redirect(url_for('gd_course_NHH_2026_group5.home_home'))
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        login_user(user)
        next_page = request.args.get('next')
        flash('You have logged in! Now, you can start to use our Carbon App!', 'success')
        return redirect(next_page) if next_page else redirect(url_for('gd_course_NHH_2026_group5.home_home'))
    else:
        flash('Login Unsuccessful. Please check email and password!', 'danger') 
  return render_template('gd_course/NHH_2026_group5/user/login.html', title='login', form=form)

@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/logout')
def logout():    
    logout_user()
    return redirect(url_for('gd_course_NHH_2026_group5.home_home'))


@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/entry', methods=['GET', 'POST'])
@login_required
def entry_home():
    user_type = request.args.get("user_type")
    transport = request.args.get("transport")
    results = None
   
    #Get the data 
    if request.method == "POST": 
        form_data = {
            "kms": request.form.get("kms", type=float),
            "fuel": request.form.get("fuel"),
            "cargo_weight": request.form.get("cargo_weight", type=float),
            "load": request.form.get("load", type=float),
            "volume": request.form.get("volume", type=float),
            "distance": request.form.get("distance", type=float),
            "flight_type": request.form.get("flight_type"),
            "cabin_class": request.form.get("cabin_class"),
            "aircraft_type": request.form.get("aircraft_type"),
            "ferry_type": request.form.get("ferry_type"),
            "train_type": request.form.get("train_type"),
            "bicycle_type": request.form.get("bicycle_type"),
            "energy_source": request.form.get("energy_source"),
        }
        
        
        results = carbon_emission(transport, form_data)
        if results is not None:
            entry = Transport_NHH_2026_g5(
                user_id=current_user.id,
                user_type=user_type,
                transport=transport,
                kms=form_data["kms"],
                fuel=form_data["fuel"],
                flight_type=form_data["flight_type"],
                cabin_class=form_data["cabin_class"],
                aircraft_type=form_data["aircraft_type"],
                ferry_type=form_data["ferry_type"],
                train_type=form_data["train_type"],
                bicycle_type=form_data["bicycle_type"],
                load=form_data["load"],
                cargo_weight=form_data["cargo_weight"],
                volume=form_data["volume"],
                distance=form_data["distance"],
                energy_source=form_data["energy_source"],
                co2=results
            )

            db.session.add(entry)
            db.session.commit()
            flash("Emission entry saved successfully.", "success")
            return redirect(url_for('gd_course_NHH_2026_group5.results_home',results=results,transport=transport,user_type=user_type))
            
    return render_template('gd_course/NHH_2026_group5/carbonCalculator/entry.html',user_type=user_type, transport=transport, results=results,title='entry')


@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/results')
@login_required
def results_home():
    user_type = request.args.get("user_type", "individual")
    
    entries = get_entries(current_user.id, user_type)
    formatted_entries = format_entries_for_table(entries)
    
    latest_entry = get_latest_entry(current_user.id, user_type)
    
    latest_result = latest_entry.co2 if latest_entry else 0
    latest_transport = latest_entry.transport if latest_entry else "-"
    
    emissions_by_transport = get_emissions_by_transport(current_user.id, user_type)
    kms_by_transport = get_kms_by_transport(current_user.id, user_type)
    emissions_by_date = get_emissions_by_date(current_user.id, user_type)
    kms_by_date = get_kms_by_date(current_user.id, user_type)

    categories = get_categories_for_user_type(user_type)
    emission_transport = build_chart_values(emissions_by_transport, categories)
    kms_transport = build_chart_values(kms_by_transport, categories)

    dates_label, over_time_emissions = format_date_chart(emissions_by_date)
    kms_dates_label, over_time_kms = format_date_chart(kms_by_date)
    
    
    #Alternatives 
    
    alternative_data = []
    
    if latest_entry: 
        alternatives = get_alternatives(latest_transport, user_type)
        
        for alt in alternatives: 
            if alt in efco2 and latest_entry.kms: 
                factor_data = efco2[alt]
                
                if isinstance(factor_data, dict): 
                    factor = list(factor_data.values())[0]
                else: 
                    factor = factor_data
                    
                alt_co2= (float(latest_entry.kms) *factor)/1000
                savings = max(0, latest_entry.co2 - alt_co2)
                
                alternative_data.append({"transport": alt, "co2": round(alt_co2,2), "savings": round(savings,2)})

    alternative_data = sorted(alternative_data, key=lambda x: x["co2"])
    
    return render_template(
        'gd_course/NHH_2026_group5/carbonCalculator/results.html',
        results=latest_result,
        transport=latest_transport,
        user_type=user_type,
        entries=entries,
        categories=categories,
        emission_transport=emission_transport,
        kms_transport=kms_transport,
        dates_label=dates_label,
        over_time_emissions=over_time_emissions,
        kms_dates_label=kms_dates_label,
        over_time_kms=over_time_kms, 
        alternative_data=alternative_data
    )
    
    
#Delete emission
@gd_course_NHH_2026_group5.route('/green_digitalization_course/NHH/2026/group5/delete-emission/<int:entry_id>', methods=['POST'])
def delete_emission(entry_id):
    entry = Transport_NHH_2026_g5.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2026_group5.results_home', user_type=entry.user_type))


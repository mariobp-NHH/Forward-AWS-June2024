from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user, logout_user
from webse import bcrypt, db
from webse.models import User, EmissionsGD
from webse.gd_course_NHH_2026_group2.forms import LoginForm, RegistrationForm, BoatForm, PlaneForm, TruckForm
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import timedelta, datetime

gd_course_NHH_2026_group2=Blueprint('gd_course_NHH_2026_group2',__name__)

@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/home')
def home_home():
    return render_template('gd_course/NHH_2026_group2/home.html')

@gd_course_NHH_2026_group2.route("/green_digitalization_course/NHH/2026/group2/about")
def about():
    return render_template("gd_course/NHH_2026_group2/about.html", title = "About Us")

@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/methodology')
def methodology_home():
    return render_template('gd_course/NHH_2026_group2/methodology.html', title='methodology')

@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user_hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=user_hashed_password, institution='NHH_2026_group2')
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! Now, you are able to login!', 'success')
        return redirect(url_for('gd_course_NHH_2026_group2.login'))

    return render_template('gd_course/NHH_2026_group2/users/register.html', title='Register', form=form)


@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login successful. You can start to use the app.', 'success')
            return redirect(url_for('gd_course_NHH_2026_group2.home_home'))

        flash('Login failed. Please check your credentials and try again.', 'danger')
        return redirect(url_for('gd_course_NHH_2026_group2.login'))

    return render_template('gd_course/NHH_2026_group2/users/login.html', title='Login', form=form)


@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('gd_course_NHH_2026_group2.home_home'))

efco2_freight = {
    'Truck': {'Diesel': 0.096, 'LNG': 0.080, 'HVO': 0.010, 'Electric': 0.000},
    'Plane': {'Jet Fuel': 0.800, 'SAF': 0.160},
    'Ferry': {'Diesel': 0.016, 'LNG': 0.013, 'Electric': 0.000}
}


@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/carbon_app')
def carbon_app_home():
    return render_template('gd_course/NHH_2026_group2/carbon_app/carbon_app.html', title='carbon_app')


@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/carbon_app/new_entry')
def new_entry():
    return render_template('gd_course/NHH_2026_group2/carbon_app/new_entry.html', title='new_entry')


# New-entry form functions - one for each freight transport type

@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/carbon_app/new_entry/boat', methods=['GET', 'POST'])
@login_required
def new_entry_boat():
    form = BoatForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        seafood_kg = form.seafood_kg.data
        transport = 'Ferry'
        weight_tonnes = seafood_kg / 1000
        total_co2e = float(weight_tonnes) * float(kms) * efco2_freight[transport][fuel]
        total_co2e = float("{:.4f}".format(total_co2e))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=total_co2e, total=total_co2e, ch4=seafood_kg, student='NHH_2026_group2', institution='NHH_2026_group2', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group2.your_data'))
    return render_template('gd_course/NHH_2026_group2/carbon_app/new_entry_boat.html', title='New Boat Entry', form=form)

@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/carbon_app/new_entry/plane', methods=['GET', 'POST'])
@login_required
def new_entry_plane():
    form = PlaneForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        seafood_kg = form.seafood_kg.data
        transport = 'Plane'
        weight_tonnes = seafood_kg / 1000
        total_co2e = float(weight_tonnes) * float(kms) * efco2_freight[transport][fuel]
        total_co2e = float("{:.4f}".format(total_co2e))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=total_co2e, total=total_co2e, ch4=seafood_kg, student='NHH_2026_group2', institution='NHH_2026_group2', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group2.your_data'))
    return render_template('gd_course/NHH_2026_group2/carbon_app/new_entry_plane.html', title='New Plane Entry', form=form)

@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/carbon_app/new_entry/truck', methods=['GET', 'POST'])
@login_required
def new_entry_truck():
    form = TruckForm()
    if form.validate_on_submit():
        kms = form.kms.data
        fuel = form.fuel_type.data
        seafood_kg = form.seafood_kg.data
        transport = 'Truck'
        weight_tonnes = seafood_kg / 1000
        total_co2e = float(weight_tonnes) * float(kms) * efco2_freight[transport][fuel]
        total_co2e = float("{:.4f}".format(total_co2e))
        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=total_co2e, total=total_co2e, ch4=seafood_kg, student='NHH_2026_group2', institution='NHH_2026_group2', year=2026, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_NHH_2026_group2.your_data'))
    return render_template('gd_course/NHH_2026_group2/carbon_app/new_entry_truck.html', title='New Truck Entry', form=form)

# Your data

@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/carbon_app/your_data')
@login_required
def your_data():
    user_id = current_user.id
    entries = EmissionsGD.query.filter_by(user_id=user_id)\
        .filter(EmissionsGD.date >= datetime.now() - timedelta(days=30))\
        .filter(EmissionsGD.institution=='NHH_2026_group2')\
        .order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()

    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=30))).filter_by(user_id=user_id). \
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    emission_transport = [0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in emissions_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

    if 'Truck' in second_tuple_elements:
        index_truck = second_tuple_elements.index('Truck')
        emission_transport[0]=first_tuple_elements[index_truck]

    if 'Plane' in second_tuple_elements:
        index_plane = second_tuple_elements.index('Plane')
        emission_transport[1]=first_tuple_elements[index_plane]

    if 'Ferry' in second_tuple_elements:
        index_ferry = second_tuple_elements.index('Ferry')
        emission_transport[2]=first_tuple_elements[index_ferry]
    # Emissions by date (individual)
    date_col = db.func.date(EmissionsGD.date)
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), date_col). \
        filter(EmissionsGD.institution=='NHH_2026_group2').\
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=30))).filter_by(user_id=user_id). \
        group_by(date_col).order_by(date_col.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date if isinstance(date, str) else date.strftime("%d-%m-%Y"))
        over_time_emissions.append(total)

    # CO₂e per kg by transport type (efficiency bar chart)
    efficiency_by_transport_query = db.session.query(
        db.func.sum(EmissionsGD.total),
        db.func.sum(EmissionsGD.ch4),
        EmissionsGD.transport
    ).filter(EmissionsGD.date > (datetime.now() - timedelta(days=30))).filter_by(user_id=user_id). \
        filter(EmissionsGD.institution=='NHH_2026_group2').\
        group_by(EmissionsGD.transport).all()
    efficiency_transport_labels = []
    efficiency_transport_values = []
    for total_co2, total_kg, transport_type in efficiency_by_transport_query:
        if total_kg and total_kg > 0:
            efficiency_transport_labels.append(transport_type)
            efficiency_transport_values.append(round(total_co2 / total_kg, 4))

    # CO₂e per kg over time (efficiency line chart)
    efficiency_by_date_query = db.session.query(
        db.func.sum(EmissionsGD.total),
        db.func.sum(EmissionsGD.ch4),
        date_col
    ).filter(EmissionsGD.date > (datetime.now() - timedelta(days=30))).filter_by(user_id=user_id). \
        filter(EmissionsGD.institution=='NHH_2026_group2').\
        group_by(date_col).order_by(date_col.asc()).all()
    over_time_efficiency = []
    for total_co2, total_kg, _ in efficiency_by_date_query:
        if total_kg and total_kg > 0:
            over_time_efficiency.append(round(total_co2 / total_kg, 4))
        else:
            over_time_efficiency.append(None)

    return render_template('gd_course/NHH_2026_group2/carbon_app/your_data.html', title='your_data', entries=entries,
                           emissions_by_transport=emission_transport,
                           over_time_emissions=over_time_emissions,
                           dates_label=dates_label,
                           efficiency_transport_labels=efficiency_transport_labels,
                           efficiency_transport_values=efficiency_transport_values,
                           over_time_efficiency=over_time_efficiency)

@gd_course_NHH_2026_group2.route('/green_digitalization_course/NHH/2026/group2/carbon_app/delete_emissions/<int:entry_id>')
def delete_emissions(entry_id):
    entry=EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_NHH_2026_group2.your_data'))
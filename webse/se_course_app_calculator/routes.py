import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt
from webse.se_course_app_calculator.forms import AddRecordForm
from webse.models import EmissionsSE
from flask_login import login_user, current_user, logout_user, login_required

se_course_app_calculator = Blueprint('se_course_app_calculator', __name__)

#####################################
####   Block 5. App Calculator   ####
#####################################

# https://efdb.apps.eea.europa.eu/?source=%7B%22query%22%3A%7B%22match_all%22%3A%7B%7D%7D%2C%22display_type%22%3A%22tabular%22%7D

##Emissions factor per transport in kg per passemger km
##++++++++++++++++++++++
efco2={"Bus":{"Diesel":0.10231,"CNG":0.08,"Petrol":0.10231,"No Fossil Fuel":0},
       "Car":{"Petrol":0.18592,"Diesel":0.16453,"No Fossil Fuel":0},
       "Plane":{"No Fossil Fuel":0.24298},
       "Ferry":{"Diesel":0.11131, "No Fossil Fuel":0},
       "Motorbike":{"Petrol":0.09816,"No Fossil Fuel":0},
       "Scooter":{"No Fossil Fuel":0},
       "Bicycle":{"No Fossil Fuel":0},
       "Walk":{"No Fossil Fuel":0}}
#"Ferry":{"Diesel":0.11131,"HFO":0.1131,"No Fossil Fuel":0},
#"Car":{"Hybrid":0.10567,"Petrol":0.18592,"Diesel":0.16453,"No Fossil Fuel":0},
#"Plane":{"Jet-Fuel":0.24298,"No Fossil Fuel":0},
efch4={"Bus":{"Diesel":2e-5,"CNG":2.5e-3,"Petrol":2e-5,"No Fossil Fuel":0},
       "Car":{"Petrol":3.1e-4,"Diesel":3e-6,"No Fossil Fuel":0},
       "Plane":{"No Fossil Fuel":1.1e-4},
       "Ferry":{"Diesel":3e-5,"No Fossil Fuel":0},
       "Motorbike":{"Petrol":2.1e-3,"No Fossil Fuel":0},
       "Scooter":{"No Fossil Fuel":0},
       "Bicycle":{"No Fossil Fuel":0},
       "Walk":{"No Fossil Fuel":0}}
#"Ferry":{"Diesel":3e-5,"HFO":3e-5,"No Fossil Fuel":0},
#"Car":{"Hybrid":1.5e-4,"Petrol":3.1e-4,"Diesel":3e-6,"No Fossil Fuel":0},
#"Plane":{"Jet-Fuel":1.1e-4,"No Fossil Fuel":0},
#+++++++++++++++++++++++

@se_course_app_calculator.route("/se_course/app_calculator", methods=['GET', 'POST'])
@login_required
def app_calculator_entry():
    form = AddRecordForm()
    form.fuel_type.choices = [(fuel, fuel) for fuel in efco2["Plane"].keys()]
    if form.validate_on_submit():
        kms = request.form['kms']
        transport = request.form['transport_type']
        fuel = request.form['fuel_type']

        co2 = float(kms) * efco2[transport][fuel]
        ch4 = float(kms) * efch4[transport][fuel]
        total = co2+ch4

        co2 = float("{:.2f}".format(co2))
        ch4 = float("{:.2f}".format(ch4))
        total = float("{:.2f}".format(total))

        emissions = EmissionsSE(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('se_course_app_calculator.app_calculator_table_graph'))
    return render_template('se_course/app calculator/app_calculator.html', title='App Calculator',
                           legend='App Calculator', paragraph='(Based on the code developed by Gabriel Fuentes for the course ENE425)',
                           form=form)

@se_course_app_calculator.route("/se_course/app_calculator/table_graph", methods=['GET', 'POST'])
@login_required
def app_calculator_table_graph():
    #Table
    entries = EmissionsSE.query.filter_by(author=current_user). \
        filter(EmissionsSE.date> (datetime.now() - timedelta(days=5))).\
        order_by(EmissionsSE.date.desc()).order_by(EmissionsSE.transport.asc()).all()

    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(EmissionsSE.total), EmissionsSE.transport). \
        filter(EmissionsSE.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(EmissionsSE.transport).order_by(EmissionsSE.transport.asc()).all()
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

    #Emissions by date
    emissions_by_date = db.session.query(db.func.sum(EmissionsSE.total), EmissionsSE.date). \
        filter(EmissionsSE.date > (datetime.now() - timedelta(days=5))).filter_by(author=current_user). \
        group_by(EmissionsSE.date).order_by(EmissionsSE.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)

    return render_template('se_course/app calculator/app_calculator_table_graph.html', entries=entries,
                           emissions_by_transport=json.dumps(emission_transport),
                           over_time_emissions=json.dumps(over_time_emissions),
                           dates_label=json.dumps(dates_label)
                           )

@se_course_app_calculator.route('/se_course/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsSE.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('se_course_app_calculator.app_calculator_table_graph'))


@se_course_app_calculator.route('/se_course/fuel_type/<transport>')
def fuel_type(transport):
    Allfuel = efco2[transport].keys()

    fuelArray = []

    for fuel in Allfuel:
        fuelObj = {}
        fuelObj["transport"] = transport
        fuelObj["fuel"] = fuel
        fuelArray.append(fuelObj)

    return jsonify({"fuel_json": fuelArray})

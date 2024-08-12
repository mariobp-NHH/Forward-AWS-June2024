import os
import secrets
import json
from datetime import timedelta, datetime
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, Blueprint
from webse import application, db, bcrypt
from webse.gd_course_app_calculator.forms import AddRecordForm
from webse.models import EmissionsGD
from flask_login import login_user, current_user, logout_user, login_required

gd_course_app_calculator = Blueprint('gd_course_app_calculator', __name__)

#####################################
####   Block 5. App Calculator   ####
#####################################

##Emissions factor per transport in kg per passemger km
##++++++++++++++++++++++
efco2={"Bus":{"Diesel":0.10231,"CNG":0.08,"Petrol":0.10231,"No Fossil Fuel":0},
       "Car":{"Petrol":0.18592,"Diesel":0.16453,"No Fossil Fuel":0},
       "Plane":{"Petrol":0.24298},
       "Ferry":{"Diesel":0.11131, "CNG":0.1131, "No Fossil Fuel":0},
       "Motorbike":{"Petrol":0.09816,"No Fossil Fuel":0},
       "Scooter":{"No Fossil Fuel":0},
       "Bicycle":{"No Fossil Fuel":0},
       "Walk":{"No Fossil Fuel":0}}
#"Ferry":{"Diesel":0.11131,"HFO":0.1131,"No Fossil Fuel":0},
#"Car":{"Hybrid":0.10567,"Petrol":0.18592,"Diesel":0.16453,"No Fossil Fuel":0},
#"Plane":{"Jet-Fuel":0.24298,"No Fossil Fuel":0},
efch4={"Bus":{"Diesel":2e-5,"CNG":2.5e-3,"Petrol":2e-5,"No Fossil Fuel":0},
       "Car":{"Petrol":3.1e-4,"Diesel":3e-6,"No Fossil Fuel":0},
       "Plane":{"Petrol":1.1e-4},
       "Ferry":{"Diesel":3e-5, "CNG":3e-5,"No Fossil Fuel":0},
       "Motorbike":{"Petrol":2.1e-3,"No Fossil Fuel":0},
       "Scooter":{"No Fossil Fuel":0},
       "Bicycle":{"No Fossil Fuel":0},
       "Walk":{"No Fossil Fuel":0}}
#"Ferry":{"Diesel":3e-5,"HFO":3e-5,"No Fossil Fuel":0},
#"Car":{"Hybrid":1.5e-4,"Petrol":3.1e-4,"Diesel":3e-6,"No Fossil Fuel":0},
#"Plane":{"Jet-Fuel":1.1e-4,"No Fossil Fuel":0},
#+++++++++++++++++++++++

@gd_course_app_calculator.route("/green_digitalization_course/app_calculator", methods=['GET', 'POST'])
@login_required
def app_calculator_entry():
    legend='Carbon Emissions Calculator'
    paragraph='(Based on the code developed by Gabriel Fuentes for the course ENE425)'
    form = AddRecordForm()
    form.fuel_type.choices = [(fuel, fuel) for fuel in efco2["Bus"].keys()]
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

        emissions = EmissionsGD(kms=kms, transport=transport, fuel=fuel, co2=co2, ch4=ch4, total=total, author=current_user, 
                student='none', institution='none', year=2023)
        db.session.add(emissions)
        db.session.commit()
        return redirect(url_for('gd_course_app_calculator.app_calculator_table_graph'))
    return render_template('gd_course/app calculator/app_calculator.html', title='Carbon Emissions Calculator', legend=legend, paragraph=paragraph, form=form)

@gd_course_app_calculator.route("/green_digitalization_course/app_calculator/table_graph", methods=['GET', 'POST'])
@login_required
def app_calculator_table_graph():
    #Table
    entries = EmissionsGD.query.filter_by(author=current_user). \
        filter(EmissionsGD.date> (datetime.now() - timedelta(days=5))).filter(EmissionsGD.student=='none').\
        order_by(EmissionsGD.date.desc()).order_by(EmissionsGD.transport.asc()).all()

    #Emissions by category
    emissions_by_transport = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter(EmissionsGD.student=='none').filter_by(author=current_user). \
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

    #Kilometers by category
    kms_by_transport = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.transport). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter(EmissionsGD.student=='none').filter_by(author=current_user). \
        group_by(EmissionsGD.transport).order_by(EmissionsGD.transport.asc()).all()
    kms_transport = [0, 0, 0, 0, 0, 0, 0, 0]
    first_tuple_elements = []
    second_tuple_elements = []
    for a_tuple in kms_by_transport:
        first_tuple_elements.append(a_tuple[0])
        second_tuple_elements.append(a_tuple[1])

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

    if 'Scooter' in second_tuple_elements:
        index_scooter = second_tuple_elements.index('Scooter')
        kms_transport[6]=first_tuple_elements[index_scooter]
    else:
        kms_transport[6]  

    if 'Bicycle' in second_tuple_elements:
        index_bicycle = second_tuple_elements.index('Bicycle')
        kms_transport[0]=first_tuple_elements[index_bicycle]
    else:
        kms_transport[0]    

    if 'Walk' in second_tuple_elements:
        index_walk = second_tuple_elements.index('Walk')
        kms_transport[7]=first_tuple_elements[index_walk]
    else:
        kms_transport[7]          
        

    #Emissions by date (individual)
    emissions_by_date = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter(EmissionsGD.student=='none').filter_by(author=current_user). \
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions = []
    dates_label = []
    for total, date in emissions_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_emissions.append(total)

    #Emissions by date (total)   
    emissions_by_date_total = db.session.query(db.func.sum(EmissionsGD.total), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))). \
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_emissions_total = []
    dates_label_total = []
    for total, date in emissions_by_date_total:
        dates_label_total.append(date.strftime("%m-%d-%y"))
        over_time_emissions_total.append(total) 

    #Kms by date (individual)
    kms_by_date = db.session.query(db.func.sum(EmissionsGD.kms), EmissionsGD.date). \
        filter(EmissionsGD.date > (datetime.now() - timedelta(days=5))).filter(EmissionsGD.student=='none').filter_by(author=current_user). \
        group_by(EmissionsGD.date).order_by(EmissionsGD.date.asc()).all()
    over_time_kms = []
    dates_label = []
    for total, date in kms_by_date:
        dates_label.append(date.strftime("%m-%d-%y"))
        over_time_kms.append(total)    

    return render_template('gd_course/app calculator/app_calculator_table_graph.html', entries=entries,
                           emissions_by_transport=json.dumps(emission_transport),
                           kms_by_transport=json.dumps(kms_transport),
                           over_time_emissions=json.dumps(over_time_emissions),
                           dates_label=json.dumps(dates_label),
                           over_time_emissions_total=json.dumps(over_time_emissions_total),
                           dates_label_total=json.dumps(dates_label_total),
                           over_time_kms=json.dumps(over_time_kms)
                           )

@gd_course_app_calculator.route('/green_digitalization_course/delete-emission/<int:entry_id>')
def delete_emission(entry_id):
    entry = EmissionsGD.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for('gd_course_app_calculator.app_calculator_table_graph'))


@gd_course_app_calculator.route('/green_digitalization_course/fuel_type/<transport>')
def fuel_type(transport):
    Allfuel = efco2[transport].keys()

    fuelArray = []

    for fuel in Allfuel:
        fuelObj = {}
        fuelObj["transport"] = transport
        fuelObj["fuel"] = fuel
        fuelArray.append(fuelObj)

    return jsonify({"fuel_json": fuelArray})

# REST API

stores = [
    {"name": "My Store", 
     "items": 
        [
            {
                "name": "Chair", 
                "price": 15.99
            }
        ]
    }
]

@gd_course_app_calculator.get("/green_digitalization_course/app_calculator/store")
def get_stores():
    return {"stores": stores}

@gd_course_app_calculator.post("/green_digitalization_course/app_calculator/store")
def create_store():   
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@gd_course_app_calculator.post("/green_digitalization_course/app_calculator/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@gd_course_app_calculator.get("/green_digitalization_course/app_calculator/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@gd_course_app_calculator.get("/green_digitalization_course/app_calculator/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404


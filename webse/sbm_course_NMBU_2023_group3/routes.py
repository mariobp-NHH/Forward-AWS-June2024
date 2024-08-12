from flask import render_template, Blueprint
from webse.sbm_course_NMBU_2023_group3.forms import AddRecordForm
from webse.sbm_course_NMBU_2023_group3.carbon_calculator_functions import co2_bus_calculator, co2_car_calculator, co2_plane_calculator, co2_ferry_calculator, co2_motorbike_calculator


sbm_course_NMBU_2023_group3=Blueprint('sbm_course_NMBU_2023_group3',__name__)

@sbm_course_NMBU_2023_group3.route('/sustainable_business_models_course/students_apps/NMBU_2023_group3')
def home():
  return render_template('sbm_course/sbm_NMBU_2023_group3/home.html')

@sbm_course_NMBU_2023_group3.route('/sustainable_business_models_course/students_apps/NMBU_2023_group3/methodology')
def methodology():
  return render_template('sbm_course/sbm_NMBU_2023_group3/methodology.html', title='methodology')

@sbm_course_NMBU_2023_group3.route('/sustainable_business_models_course/students_apps/NMBU_2023_group3/carbon_app', methods=['GET', 'POST'])
def carbon_app():
    form = AddRecordForm()
    if form.validate_on_submit():
        bus_kms = form.bus_kms.data
        car_kms = form.car_kms.data
        plane_kms = form.plane_kms.data
        ferry_kms = form.ferry_kms.data
        motorbike_kms = form.motorbike_kms.data
        scooter_kms = form.scooter_kms.data
        bicycle_kms = form.bicycle_kms.data
        walk_kms = form.walk_kms.data

        bus_type = form.bus_type.data
        car_type = form.car_type.data
        plane_type = form.plane_type.data
        ferry_type = form.ferry_type.data
        motorbike_type = form.motorbike_type.data
        scooter_type = form.scooter_type.data
        bicycle_type = form.bicycle_type.data
        walk_type = form.walk_type.data

        co2_bus = co2_bus_calculator(bus_type, bus_kms)
        co2_car = co2_car_calculator(car_type, car_kms)
        co2_plane = co2_plane_calculator(plane_type, plane_kms)
        co2_ferry = co2_ferry_calculator(ferry_type, ferry_kms)
        co2_motorbike = co2_motorbike_calculator(motorbike_type, motorbike_kms)
        co2_scooter = float(scooter_kms) * 0
        co2_bicycle = float(bicycle_kms) * 0
        co2_walk = float(walk_kms) * 0

        co2_bus = float("{:.2f}".format(co2_bus))
        co2_car = float("{:.2f}".format(co2_car))
        co2_plane = float("{:.2f}".format(co2_plane))
        co2_ferry = float("{:.2f}".format(co2_ferry))
        co2_motorbike = float("{:.2f}".format(co2_motorbike))
        co2_scooter = float("{:.2f}".format(co2_scooter))
        co2_bicycle = float("{:.2f}".format(co2_bicycle))
        co2_walk = float("{:.2f}".format(co2_walk))

        form.bus_co2.data = co2_bus
        form.car_co2.data = co2_car
        form.plane_co2.data = co2_plane
        form.ferry_co2.data = co2_ferry
        form.motorbike_co2.data = co2_motorbike
        form.scooter_co2.data = co2_scooter
        form.bicycle_co2.data = co2_bicycle
        form.walk_co2.data = co2_walk
        return render_template('sbm_course/sbm_NMBU_2023_group3/carbon_app/carbon_app2.html', title='App Calculator', legend='App Calculator', form=form, 
            co2_bus=co2_bus, co2_car=co2_car, co2_plane=co2_plane, co2_ferry=co2_ferry, co2_motorbike=co2_motorbike,
            co2_scooter=co2_scooter, co2_bicycle=co2_bicycle, co2_walk=co2_walk)
    return render_template('sbm_course/sbm_NMBU_2023_group3/carbon_app/carbon_app.html', title='App Calculator', legend='App Calculator', form=form)

    

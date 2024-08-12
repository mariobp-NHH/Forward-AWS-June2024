from flask import Flask, render_template, Blueprint
from webse.se_course_students_apps.forms import AddRecordForm

se_course_students_apps = Blueprint('se_course_students_apps', __name__)

#app = Flask(__name__)
#app.config['SECRET_KEY'] = '3434345791628bb0b13ce0c676dfde280ba245'


@se_course_students_apps.route('/se_course/students_apps/home_developers')
def students_apps_home_developers():
    return render_template('se_course/students apps/home_developers.html')

@se_course_students_apps.route('/se_course/students_apps/app_calculator', methods=['GET', 'POST'])
def students_apps_app_calculator():
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

        if bus_type == 'Bus Diesel':
            co2_bus = float(bus_kms) * 0.10231
        elif bus_type == 'Bus CNG':
            co2_bus = float(bus_kms) * 0.08
        elif bus_type == 'Bus Petrol':
            co2_bus = float(bus_kms) * 0.10231
        else:
            co2_bus = float(bus_kms) * 0

        if car_type == 'Car Petrol':
            co2_car = float(car_kms) * 0.18592
        elif car_type == 'Car Diesel':
            co2_car = float(car_kms) * 0.16453
        else:
            co2_car = float(car_kms) * 0

        if plane_type == 'Plane Jet Fuel':
            co2_plane = float(plane_kms) * 0.24298
        else:
            co2_plane = float(plane_kms) * 0

        if ferry_type == 'Ferry Diesel':
            co2_ferry = float(ferry_kms) * 0.11131
        else:
            co2_ferry = float(ferry_kms) * 0

        if motorbike_type == 'Motorbike Petrol':
            co2_motorbike = float(motorbike_kms) * 0.09816
        else:
            co2_motorbike = float(motorbike_kms) * 0

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
        return render_template('se_course/students apps/app_calculator2.html', title='App Calculator', legend='App Calculator',
                               paragraph='(Based on the code developed by Gabriel Fuentes for the course ENE425)',
                               co2_bus=co2_bus, co2_car=co2_car, co2_plane=co2_plane, co2_ferry=co2_ferry, co2_motorbike=co2_motorbike,
                               co2_scooter=co2_scooter, co2_bicycle=co2_bicycle, co2_walk=co2_walk, form=form)
    return render_template('se_course/students apps/app_calculator.html', title='App Calculator', legend='App Calculator',
                               paragraph='(Based on the code developed by Gabriel Fuentes for the course ENE425)', form=form)




def co2_bus_calculator(bus_type, bus_kms):
    if bus_type == 'Bus Diesel':
        co2_bus = float(bus_kms) * 0.10231
    elif bus_type == 'Bus CNG':
        co2_bus = float(bus_kms) * 0.08
    elif bus_type == 'Bus Petrol':
        co2_bus = float(bus_kms) * 0.10231
    else:
        co2_bus = float(bus_kms) * 0    
    return co2_bus

def co2_car_calculator(car_type, car_kms):
    if car_type == 'Car Petrol':
        co2_car = float(car_kms) * 0.18592
    elif car_type == 'Car Diesel':
        co2_car = float(car_kms) * 0.16453
    else:
        co2_car = float(car_kms) * 0
    return co2_car

def co2_plane_calculator(plane_type, plane_kms):
    if plane_type == 'Plane Jet Fuel':
        co2_plane = float(plane_kms) * 0.24298
    else:
        co2_plane = float(plane_kms) * 0
    return co2_plane

def co2_ferry_calculator(ferry_type, ferry_kms):
    if ferry_type == 'Ferry Diesel':
        co2_ferry = float(ferry_kms) * 0.11131
    else:
        co2_ferry = float(ferry_kms) * 0
    return co2_ferry

def co2_motorbike_calculator(motorbike_type, motorbike_kms):
    if motorbike_type == 'Motorbike Petrol':
        co2_motorbike = float(motorbike_kms) * 0.09816
    else:
        co2_motorbike = float(motorbike_kms) * 0
    return co2_motorbike
    
    
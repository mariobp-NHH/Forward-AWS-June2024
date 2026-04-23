# this is to seperate the functions from the routes, to make the code cleaner and more modular. It also allows us to test the functions separately from the routes.

efco2={'Bus':{'Diesel':0.10231,'CNG':0.08,'Petrol':0.10231,'No Fossil Fuel':0},
    'Car':{'Petrol':0.18592,'Diesel':0.16453,'No Fossil Fuel':0},
    'Plane':{'Petrol':0.24298},
    'Ferry':{'Diesel':0.11131, 'CNG':0.1131, 'No Fossil Fuel':0},
    'Motorbike':{'Petrol':0.09816,'No Fossil Fuel':0},
    'Scooter':{'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}
efch4={'Bus':{'Diesel':2e-5,'CNG':2.5e-3,'Petrol':2e-5,'No Fossil Fuel':0},
    'Car':{'Petrol':3.1e-4,'Diesel':3e-6,'No Fossil Fuel':0},
    'Plane':{'Petrol':1.1e-4},
    'Ferry':{'Diesel':3e-5, 'CNG':3e-5,'No Fossil Fuel':0},
    'Motorbike':{'Petrol':2.1e-3,'No Fossil Fuel':0},
    'Scooter':{'No Fossil Fuel':0},
    'Bicycle':{'No Fossil Fuel':0},
    'Walk':{'No Fossil Fuel':0}}

def carbon_emmissions(kms, transport, fuel):
    co2 = float(kms) * efco2[transport][fuel]
    return co2
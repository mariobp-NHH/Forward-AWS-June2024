efco2={'Bus':{'Diesel':0.025,'Biodiesel':0.007},
  'Car':{'Petrol':0.167,'Diesel':0.137,'Electric Nordic':0.014, 'Electric Europe':0.045},
  'Plane':{'Business':0.298,'Economy':0.118},
  'Ferry':{'Average Ferry':0.226},
  'Motorbike':{'Petrol':0.052 ,'Electric':0.017},
  'Scooter':{'No Fossil Fuel':0},
  'Bicycle':{'No Fossil Fuel':0},
  'Walk':{'No Fossil Fuel':0},
  'Train':{'Diesel':0.091,'Electric Europe':0.024,'Electric Nordic':0.007}
}

def carbon_emissions(kms, transport, fuel):
    co2 = float(kms) * efco2[transport][fuel]
    co2 = round(co2, 2)
    total = co2
    return co2, total

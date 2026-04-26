# Utslippsfaktorer — eneste kilde til sannhet for EcoRoute.
# Alle CO2-faktorer og karbonprisingskonstanter ligger her.
# Metodologi-teamet eier tallene; ikke oppdater uten deres godkjenning.
# ---------------------------------------------------------------------------
# CO2-faktorer: kg CO2 per Tonne-km
# Struktur: [transport_type][subcategory][fuel_type]
# transport_type-nøkler samsvarer med Route.transport_type som lagret i DB: Road | Sea | Air
# ---------------------------------------------------------------------------

EMISSION_FACTORS_CO2 = {
    "Road": {
        "small":  {"Diesel": 0.258, "CNG": 0.229},
        "medium": {"Diesel": 0.160, "CNG": 0.142},
        "large":  {"Diesel": 0.094, "CNG": 0.085, "LNG": 0.090},
    },
    "Sea": {
        "general_cargo_small": {"HFO": 0.0203, "VLSFO": 0.0203, "MDO": 0.0197},
        "general_cargo_large": {"HFO": 0.0122, "VLSFO": 0.0122, "MDO": 0.0119},
        "bulk_carrier_small":  {"HFO": 0.0169, "VLSFO": 0.0169, "MDO": 0.0164},
        "bulk_carrier_large":  {"HFO": 0.0039, "VLSFO": 0.0039, "MDO": 0.0037},
    },
    "Air": {
        "short_haul": {"Jet A/A-1": 1.255},
        "long_haul":  {"Jet A/A-1": 0.503},
    },
}

CARBON_PRICE_EUR_PER_TONNE    = 77.0 #STATISK PRIS
EUR_TO_NOK                    = 11.20 #STATISK KURS 


#kg CO2 for en shipment. 
def calculate_co2_kg(transport_type, subcategory, fuel_type, distance_km, cargo_tonnes):
    co2_kg_per_tonne_km = EMISSION_FACTORS_CO2[transport_type][subcategory][fuel_type]
    tonne_km            = distance_km * cargo_tonnes
    co2_kg              = tonne_km * co2_kg_per_tonne_km
    return co2_kg

#Karbonkostnad i NOK basert på CO2.
def calculate_carbon_cost_nok(co2_kg):
    co2_tonnes       = co2_kg / 1000.0
    carbon_cost_eur  = co2_tonnes * CARBON_PRICE_EUR_PER_TONNE
    carbon_cost_nok  = carbon_cost_eur * EUR_TO_NOK
    return carbon_cost_nok

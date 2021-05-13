from numpy.random import choice, rand

# Negative Events
SICKNESS = 'sickness'
ROAD_CLOSURE = 'road_closure'
CELL_TOWER_OUTAGE = 'cell_tower_outage'
COMBAT = 'combat'
CAR_BREAKDOWN = 'car_breakdown'
ASTEROID = 'asteroid'
CHINESE_ROCKET = 'chinese_rocket'

# Positive Events
WANDERING_MERCHANT = 'wandering_merchant'
    
# COVID strikes, costs medical supplies reduced by doctor
def sickness_event():
    print("COVID strikes!!")
    
    # Check to see if party has doctor, if doctor is present, ask if they want
    # to use doctor's ability to counteract
    
    # if party.doctor_alive():
    #   ask if they want to use it
    
    # If they have medical supplies, take from the supplies first and then set
    # party members to sick
    
    # if party.medical_supplies > 0:
    #   party.medical_supplies -= number_of_supplies
    #   party.set_sick = True

# Road closed/detour, costs extra fuel - reduced by engineer
def road_closure_event():
    print("Road closure! You must take a detour. This will cost extra fuel.")
    # Check to see if engineer is present, ask if they want to use engineers ability
    
    # if party.engineer_alive():
    #   ask if they want to use special power
    
    # If they have fuel in inventory, take from fuel.
    
    # What to do if no fuel is present? Game over?

# Reduced morale, costs extra phone charge - reduced by DJ
def cell_tower_outage():
    print("cell_tower_outage")

# Random enemies that your party, loot extra supplies
def combat():
    print("combat")

def car_breakdown():
    print("car_breakdown")

def asteroid():
    print("asteroid")

def chinese_rocket():
    print("chinese_rocket")

def wandering_merchant():
    print("wandering_merchant")
    
# Event function reference dictionary
events = {
    SICKNESS: sickness_event,
    ROAD_CLOSURE: road_closure_event,
    CELL_TOWER_OUTAGE: cell_tower_outage,
    COMBAT: combat,
    CAR_BREAKDOWN: car_breakdown,
    ASTEROID: asteroid,
    CHINESE_ROCKET: chinese_rocket,
    WANDERING_MERCHANT: wandering_merchant
}

def generate_random_event():
    # List of Events
    list_of_events = [SICKNESS, ROAD_CLOSURE, CELL_TOWER_OUTAGE, COMBAT, CAR_BREAKDOWN, ASTEROID, CHINESE_ROCKET, WANDERING_MERCHANT]
    
    # Probability of each event happening
    distribution_of_events = [0.175, 0.175, 0.175, 0.2, 0.05, 0.025, 0.025, 0.175]
    
    random_event = choice(list_of_events, 1, p=distribution_of_events)
    random_event = random_event[0]
    events[random_event]()

generate_random_event()

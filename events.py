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

EVENT_CONSTANT = 30
    
# COVID strikes, costs medical supplies, reduced by doctor
def sickness_event(party):
    print("COVID strikes!!")
    
    # Check to see if party's doctor is present
    if party.is_alive("doctor"):
        if party.used_ability("doctor"):
            print("Oh no!! Your doctor has already used their special ability.")
            covid_strike_helper(party)
        elif not party.used_ability("doctor"):
            # ask if they want to use it
            print("Your doctor can use their special power to save you all. Would you like to use the doctor's special power? (Y/N) ")
            
            # validation loop
            while True:
                choice = input(">>> ")
                if choice.upper() == "Y":
                    print("You have used your doctor's special power. You will not be able to use their power again.")
                    # set ability used to true, cannot use again
                    party.use_ability("doctor")
                    break
                elif choice.upper() == "N":
                    covid_strike_helper(party)
                    break
                else:
                    print("Please enter Y or N.")
            
    else:
        # Doctor is dead
        print("Your doctor is dead and cannot save your party.")
        covid_strike_helper(party)
            
# helper function to help reduce code in sickness event function
def covid_strike_helper(party):
    if party.hand_sanitizer >= EVENT_CONSTANT:
        print("Your party had to use 50 of your hand sanitizer to avoid gettin sick.")
        party.hand_sanitizer -= EVENT_CONSTANT
    else:
        print("Since your party does not have enough hand sanitizer to protect yourselves, you are all sick.")
        # set party to sick
        party.sick_party()

# Road closed/detour, costs extra fuel - reduced by engineer
def road_closure_event(party):
    print("Road closure! You must take a detour. This will cost extra fuel.")
    # Check to see if engineer is present, ask if they want to use engineers ability
    
    if party.is_alive("engineer"):
        print("Your engineer can use their special power to fuel up the car and save you all. Would you like to use your engineer's special power? (Y/N) ")
        choice = input(">>> ")
    
    # If they have fuel in inventory, take from fuel.
    
    # What to do if no fuel is present? Game over?

# Reduced morale, costs extra phone charge - reduced by DJ
def cell_tower_outage(party):
    print("cell_tower_outage")

# Random enemies that your party, loot extra supplies
def combat(party):
    print("combat")

def car_breakdown(party):
    print("car_breakdown")

def asteroid(party):
    print("asteroid")

def chinese_rocket(party):
    print("chinese_rocket")

def wandering_merchant(party):
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

def generate_random_event(party):
    # List of Events
    list_of_events = [SICKNESS, ROAD_CLOSURE, CELL_TOWER_OUTAGE, COMBAT, CAR_BREAKDOWN, ASTEROID, CHINESE_ROCKET, WANDERING_MERCHANT]
    
    # Probability of each event happening
    distribution_of_events = [0.175, 0.175, 0.175, 0.2, 0.05, 0.025, 0.025, 0.175]
    
    random_event = choice(list_of_events, 1, p=distribution_of_events)
    random_event = random_event[0]
    events[random_event](party)

from assets import game_over
from combat import combat
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
        else:
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
        print("Your party had to use %d of your hand sanitizer to avoid getting sick." % (EVENT_CONSTANT))
        party.hand_sanitizer -= EVENT_CONSTANT
    else:
        print("Since your party does not have enough hand sanitizer to protect yourselves, you are all sick. Your health will decrease at a faster rate.")
        # set party to sick
        party.sick_party()

# Road closed/detour, costs extra fuel - reduced by engineer
def road_closure_event(party):
    print("Road closure! You must take a detour. This will cost extra fuel.")
    
    # Check to see if engineer is present
    if party.is_alive("engineer"):
        # Check to see if engineer has used ability or not
        if party.used_ability("engineer"):
            print("Oh no!! Your engineer has already used their special ability.")
            road_closure_helper(party)
        else:
            # ask if they want to use special ability
            print("Your engineer can use their special power to fuel up the car and save you all. Would you like to use your engineer's special power? (Y/N) ")
            
            # validation loop
            while True:
                choice = input(">>> ")
                if choice.upper() == "Y":
                    print("You have used your engineer's special power. You will not be able to use their power again.")
                    # change ability used to true, party cannot use ablility again
                    party.use_ability("engineer")
                    break
                elif choice.upper() == "N":
                    road_closure_helper(party)
                    break
                else:
                    print("Please enter Y or N.")
    else:
        # Doctor is dead
        print("Your engineer is dead and cannot save your party.")
        road_closure_helper(party)
    
def road_closure_helper(party):
    if party.fuel >= EVENT_CONSTANT:
        party.fuel -= EVENT_CONSTANT
        print("%d of your fuel was used to avoid being stranded." % (EVENT_CONSTANT))
    else:
        print("You do not have enough fuel. Your party is stranded.")
        party.fuel -= EVENT_CONSTANT
        game_over()

# Reduced morale, costs extra phone charge - reduced by DJ
def cell_tower_outage(party):
    print("There is a cell tower down in your area. You don't have signal. Your influencer cannot survive without cell service and dies.")
    # Kill influencer
    party.party_members[3].health = 0
    print("The rest of your party can be saved.")
    # check to see if DJ is alive
    if party.is_alive("dj"):
        # check if the DJ has used special power
        if party.used_ability("dj"):
            print("Oh no!! Your DJ has already used their special ability.")
            cell_tower_outage_helper(party)
        else:
            # ask if they want to use special ability
            print("Your DJ can use their special power to save you all from deathly low morale. Would you like to use your DJ's special power? (Y/N) ")
            
            # validation loop
            while True:
                choice = input(">>> ")
                if choice.upper() == "Y":
                    print("You have used your DJ's special power. You will not be able to use their power again.")
                    # change ability used to true, party cannot use ablility again
                    party.use_ability("dj")
                    break
                elif choice.upper() == "N":
                    road_closure_helper(party)
                    break
                else:
                    print("Please enter Y or N.")
    else:
        print("Your DJ is dead and cannot save your party.")
        
def cell_tower_outage_helper(party):
    if party.phone_charge >= EVENT_CONSTANT:
        party.phone_charge -= EVENT_CONSTANT
        print("%d of your phone charge was used to avoid decreasing morale to a deathly level." % (EVENT_CONSTANT))
    else:
        print("You do not have enough phone charge.")
        party.phone_charge -= EVENT_CONSTANT

# Random enemies that your party, loot extra supplies

def car_breakdown(party):
    print("Your car has broken down... the only thing that can save you is your engineer's special ability to fix the car. Otherwise, your party will not make it.")
    if party.is_alive("engineer"):
        if party.used_ability("engineer"):
            print("Your engineer has already used their ability. Game over.")
            party.fuel = 0
        else:
            print("Yay!!! Your engineer has come to the rescue. Your car is now fixed and your party can continue on your journey.")
    else:
        print("Your engineer is dead. Game over.")
        party.fuel = 0
        game_over()

def asteroid(party):
    sound("explosion.wav")
    print("A HUGE asteroid has fallen on your party. There were no survivors. Game over.")
    kill_party(party)

def chinese_rocket(party):
    sound("missle.wav")
    print("China's rocket fell out of the sky and landed on your party!! None of you survived. Game over.")
    kill_party(party)

def wandering_merchant(party):
    print("You come across a wandering merchant. This merchant is selling special items that will act like a party member's special ability. You may choose to buy one item from the merchant.")
    party.print_party_status()
    print("Your party has $%d available." % (party.money))
    print("""
    ><><><><><><><><><>><><><><><><><><><><><><><><
        What would you like to purchase? (1-5)
    -----------------------------------------------
    [ 1 ] Doctor's ability      $100
    [ 2 ] Engineer's ability    $100
    [ 3 ] Hunter's ability      $100
    [ 4 ] DJ's ability          $100
    [ 5 ] Receive $100
    ------------------------------------------------
    ><><><><><><><><><><><><><><><><><><><><><><><><
    """)
    
    while True:
        choice = input(">>> ")
        
        if choice == "1":
            if party.used_ability("doctor"):
                party.refresh_ability("doctor")
                print("Doctor's ability has been restored.")
                break
            else:
                print("The doctor still has their ability. Please choose another character or choose to receive $100.")
        elif choice == "2":
            if party.used_ability("engineer"):
                party.refresh_ability("engineer")
                print("Engineer's ability has been restored.")
                break
            else:
                print("The engineer still has their ability. Please choose another character or choose to receive $100.")
        elif choice == "3":
            if party.used_ability("hunter"):
                party.refresh_ability("hunter")
                print("Hunter's ability has been restored.")
                break
            else:
                print("The hunter still has their ability. Please choose another character or choose to receive $100.")
        elif choice == "4":
            if party.used_ability("dj"):
                party.refresh_ability("dj")
                print("DJ's ability has been restored.")
                break
            else:
                print("The DJ still has their ability. Please choose another character or choose to receive $100.")
        elif choice == "5":
            party.money += 100
            sound("cash.wav")
            print("You party is now $100 richer!")
            break
        else:
            print("Please enter a number between 1 and 5.")
    
    
# function to set all party members health to 0 aka killing them
def kill_party(party):
    party_members = party.party_members
    for member in party_members:
        member.health = 0
        game_over()
    
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

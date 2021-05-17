#Holds the main game loop


#import classes, music, art, time here
from party import Party
from combat import *
from characters import *
from party import *
from assets import *
from store import *
from events import *
from time import sleep
from pygame import mixer

#Initialize ability to play sound files
mixer.init()
mixer.music.load("audio/title_music.wav")
#Set volume
mixer.music.set_volume(0.7)

def sound(file):
    sound = mixer.Sound("audio/%s" % file)
    return mixer.Sound.play(sound)

#create main loop
running = True
# day = 0

def main():
    day = 0
    while running == True:
        print("\033c")
        if(day == 0):
            print(intro_text)
            pause = input("\nPress any key to continue")
            print("\033c")
            print(character_info)
            pause = input("\nPress any key to continue")
            party = create_party()
        print("\033c")
        

        print("The day is: " + str(day))
        today(day, party) 
        if day > 9:
            break
        #Check to see if anyone has died
        check_dead(party)
                
        #Random event
        generate_random_event(party)
        
        #Check death again
        check_dead(party)
        
        #Check is_alive for each member of party
        #Run main decision function
        decision_menu(party, day)
        
        #Pause
        pause = input("\n\nPress enter to end the day.")
        #Increment fullness, health, morale, and fuel.
        day += 1
        depression(party)
        sickness(party)
        hunger(party)
        spend_fuel(party)


########################################
#Function definitions

def create_party():
        print("\033c")
        print("It's time to assemble your party\n")
        doctorName = input("What is the name of the Doctor? ")
        doctor = Character(doctorName, 100, 100, 100, 1, 2, 3)
        engineerName = input("What is the name of the Engineer? ")
        engineer = Character(engineerName, 100, 100, 100, 2, 2, 2)
        hunterName = input("What is the name of the Hunter? ")
        hunter = Character(hunterName, 100, 100, 100, 3, 3, 2)
        influencerName = input("What is the name of the Influencer? ")
        influencer = Character(influencerName, 100, 100, 100, 3, 3, 3)
        djName = input("What is the name of the DJ? ")
        dj = Character(djName, 100, 100, 100, 2, 2, 1)

        party_list = [doctor, engineer, hunter, influencer, dj]
        party = Party(party_list, 1000, 50, 50, 50, 50, 50)
        return party

#Character selection function
def character_selection():
    print("\033c")
    print(character_info)

# Function to print today's date and location
def today(day, party):
    if day == 0:
        print('')
    elif day == 1:
        print(day_01)
    elif day == 2:
        print(day_02)
    elif day == 3:
        print(day_03)
    elif day == 4:
        print(day_04)
    elif day == 5:
        print(day_05)
    elif day == 6:
        print(day_06)
    elif day == 7:
        print(day_07)
    elif day == 8:
        print(day_08)
    elif day == 9:
        print(day_09)
    elif day == 10:
        print(day_10)
        running == False

#Main decision menu
def decision_menu(party, day):
    run = True
    while run == True:
        # print("The day is: " + str(day))
        print("""
        ><><><><><><><><><>><><><><><><><><><><><><><><
                What do you want to do next?
        -----------------------------------------------
        [ 1 ] Keep Travelling
        [ 2 ] Hunt for Food
        [ 3 ] Enter Store
        [ 4 ] Check Supplies
        [ 5 ] Check Party Status
        [ 6 ] Quit Game
        ------------------------------------------------
        ><><><><><><><><><><><><><><><><><><><><><><><><                
    
        """)
        user_choice = input(">>>  ")
        if user_choice == "1":
            print("The party keeps travelling.")
            run = False
        elif user_choice == "2":
            #Check location 
            if check_location(day) == False:
                print("Enter hunting")
                combat(party)
            else:
                print("You can't hunt in a city")
                pause = input("Press any key to continue")
                print("\033c")
        elif user_choice == "3":
            print("The day is %d" % (day))
            if check_location(day):
                print("Entering store")
                store(party)
            else:
                print("You're not in a city right now.")
                pause = input("Press any key to continue")
                print("\033c")
        elif user_choice == "4":
            party.print_party_supplies()
            pause = input("Press any key to continue")
            print("\033c")
        elif user_choice == "5":
            party.print_party_status()
            pause = input("Press any key to continue")
            print("\033c")
        elif user_choice == "6":
            print("Exiting the game. Thanks for playing!")
            run = False
            exit()
        else:
            print("Invalid input. Please choose from options 1-6.")
            
#Daily incrementing for fullness, health, morale, and fuel

def hunger(party):
    if party.food > 0:
        party.food -= 30
        if party.food <= 0:
            for person in party.party_members:
                person.fullness -= 10*person.hunger_multiplier
    else:
        print("You're out of food!")
        for person in party.party_members:
            person.fullness -= 10*person.hunger_multiplier

def sickness(party):
    if party.hand_sanitizer > 0:
        party.hand_sanitizer -= 30
        if party.hand_sanitizer <= 0:
            for person in party.party_members:
                person.sick == True
    else:
        print("You're out of hand sanitizer!")
        for person in party.party_members:
                person.sick == True
def depression(party):
    for person in party.party_members:
        person.morale -= 10*person.depression_multiplier

def spend_fuel(party):
    if party.fuel > 0:
        party.fuel -= 8
    else:
        print("You're totally out of fuel and stranded.")
        quit()

#Function to check location
def check_location(day):
    print(day)
    if day == 0 or day == 3 or day == 5 or day == 8:
        return True
    else:
        return False

#Check dead conditions
def check_dead(party):
    count = 0
    for person in party.party_members:
        if person.is_alive() == False:
            # party.party_members.remove(person)
            count += 1
            print("\n%s has died" % (person.name))
            if count >= len(party.party_members):
                print("\nYou all died.")
                game_over()
    

#Function to add slow typing effect
def type_text(words):
    for char in words:
        sleep(0.05)
        print(char, end='', flush=True)

################################################
# Executable program 
print("\033c")
mixer.music.play()
#print title screen
main_title()
pause = input("\nPress any key to begin")
#Run main loop
main()
#If the user succeeds, print the end text/credits
end_text = "The game has ended. Thanks for playing"
type_text(end_text)


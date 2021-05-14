#Holds the main game loop


#import classes, music, art, time here
from characters import *
from assets import *
from store import *
from events import *
from time import sleep
#Initialize ability to play sound files
# from pygame import mixer
# mixer.init()

# mixer.Sound.play("audio/bensound-sunny.wav")

#create main loop
running = True
day = 0

def main():
    day = 0
    while running == True:
        print("\033c")
        print("The day is: " + str(day))
        today(day) 

        day += 1
        if day > 10:
            break
        #Random event
        generate_random_event()

        #Run main decision function
        decision_menu()
        
        #Pause
        pause = input("\n\nPress enter to end the day.")
        #Increment fullness, health, and morale.
        depression()
        sickness()
        hunger()

#Character selection function
def character_selection():
    print("\033c")
    print("Your team consists of five specialists: ")

# Function to print today's date and location
def today(day):
    if day == 0:
        print(intro_text)
        pause = input("\nPress any key to continue to character selection")
        character_selection()
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
def print_party_supplies():
    print("Print party supplies")

def print_party_status():
    print("Print party status")


def decision_menu():
    print("""
    ><><><><><><><><><>><><><><><><><><><><><><><><
             What do you want to do next?
    -----------------------------------------------
    [ 1 ] Keep Travelling
    [ 2 ] Stop to Rest
    [ 3 ] Hunt for Food
    [ 4 ] Enter Store
    [ 5 ] Check Supplies
    [ 6 ] Check Party Status
    [ 7 ] Quit Game
    ------------------------------------------------
    ><><><><><><><><><><><><><><><><><><><><><><><><                
    
    """)
    user_choice = input(">>>  ")
    if user_choice == "1":
        print("The party keeps travelling.")
    elif user_choice == "2":
        print("You stop to rest")
    elif user_choice == "3":
        #Check location 
        print("Enter hunting")
    elif user_choice == "4":
        #Check location
        print("Entering store")
        store(Party)
    elif user_choice == "5":
        print_party_supplies()
    elif user_choice == "6":
        print_party_status()
    elif user_choice == "7":
        print("Exiting the game")
        exit()
    else:
        print("Invalid input. Please choose from options 1-6.")
        user_choice = input(">>>  ")

#Combat functionality
def combat():
    pass

#Daily incrementing for fullness, health, and morale
class Party:
    def __init__(self) -> None:
        self.party_members = []

party = Party()

def hunger():
    for person in party.party_members:
        return "Fullness increments down for each player"

def sickness():
    for person in party.party_members:
        if person.sick == True:
            return "Decrease health by ... "

def depression():
    for person in party.party_members:
        return "Decrease morale by ..."


#Function to add slow typing effect
def type_text(words):
    for char in words:
        sleep(0.1)
        print(char, end='', flush=True)

# Executable program 
print("\033c")
#print title screen
main_title()
pause = input("\nPress any key to begin")

main()
end_text = "The game has ended. Thanks for playing"
type_text(end_text)


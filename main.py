#Holds the main game loop


#import classes, music, art, time here
# from characters import *

from assets import *
# from store import *
import time

#Initialize ability to play sound files
# from pygame import mixer


# def sound(file):
#    sound = mixer.Sound(f"audio/{file}")
#    return mixer.Sound.play(sound)

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

        #Run main decision function
        decision_menu()
        
        
        pause = input("\n\nPress enter to end the day.")

        # depression()
        # sickness()
        # hunger()



# Function to print today's date and location
def today(day):
    if day == 0:
        print("We'll go the store now")
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
    [ 6 ] Quit Game
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
        print("Enter store function")
        #store(party)
    elif user_choice == "5":
        print("Print supply list")
    elif user_choice == "6":
        print("Exiting the game")
        exit()
    else:
        print("Invalid input. Please choose from options 1-6.")
        user_choice = input(">>>  ")

def combat():
    pass


# Executable program 
print("\033c")
#print title screen
main_title()
# sound(sunny.wav)
pause = input("\nPress any key to begin")

main()
print("End of game")
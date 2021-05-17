from pygame import mixer

mixer.init()
mixer.music.set_volume(0.3)

# Items
FOOD = 'food'
BULLETS = 'bullets'
FUEL = 'fuel'
PHONE_CHARGE = 'phone_charger'
HAND_SANITIZER = 'hand_sanitizer'

list_of_items = [FOOD, BULLETS, FUEL, PHONE_CHARGE, HAND_SANITIZER]

items = {
    FOOD: 20,
    BULLETS: 30,
    FUEL: 40,
    PHONE_CHARGE: 20,
    HAND_SANITIZER: 5
}

def sound(file):
    sound = mixer.Sound("audio/%s" % file)
    return mixer.Sound.play(sound)

def store(party):
    
    total_amount_spent = 0
    
    while True:
        print("\033c")
        print("Your party has $%d available." % (party.money))
        
        if party.money < 10:
            print("Your party does not have enough money to buy anything from the store.")
            break
        
        print("""
        ><><><><><><><><><>><><><><><><><><><><><><><><
            What would you like to purchase? (1-5)
        -----------------------------------------------
        [ 1 ] Food              $20
        [ 2 ] Hand Sanitizer    $10
        [ 3 ] Fuel              $40
        [ 4 ] Phone Charger     $20
        [ 5 ] Bullets           $30
        [ 6 ] Return to main menu
        ------------------------------------------------
        ><><><><><><><><><><><><><><><><><><><><><><><><      
            
        """)
        choice = input(">>> ")
        
        print("""
        ><><><><><><><><><>><><><><><><><><><><><><><><
                    How many would you like?
        ><><><><><><><><><>><><><><><><><><><><><><><><
              
        """)
        quantity = int(input(">>> "))
        
        if choice == "1":
            item = FOOD
        elif choice == "2":
            item = HAND_SANITIZER
        elif choice == "3":
            item = FUEL
        elif choice == "4":
            item = PHONE_CHARGE
        elif choice == "5":
            item = BULLETS
        elif choice == "6":
            break
        else:
            continue
        
        # total for this specific item
        total = items[item] * quantity
        
        # Check if they have enough money to buy this.
        if party.money - total < 0:
            print("You do not have enough money. Please try again.")
            continue
            
        # decrease party total cash amount
        party.money -= total
        
        # add item(s) to inventory
        if item == FOOD:
            party.food += quantity
        elif item == BULLETS:
            party.bullets += quantity
        elif item == FUEL:
            party.fuel += quantity
        elif item == PHONE_CHARGE:
            party.phone_charge += quantity
        elif item == HAND_SANITIZER:
            party.hand_sanitizer += quantity
        
        # calculate total amount being spent
        total_amount_spent += items[item] * quantity
        
        sound("cash.wav")
        print("That will be $%d for a total of $%d. Your party now has..." % (total, total_amount_spent))
        party.print_party_supplies()
        
        keep_going = input("Would you like to buy something else? (Y/N) ")
        if keep_going.upper() == "N":
            break
        elif keep_going.upper() == "Y":
            continue
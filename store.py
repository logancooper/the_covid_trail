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

def store(party):
    
    total_amount_spent = 0
    
    while True:
        print("Your party has $%d available." % (party.money))
        
        if party.money < 10:
            print("Your party does not have enough money to buy anything from the store.")
            break
        
        print("""
        ><><><><><><><><><>><><><><><><><><><><><><><><
            What would you like to purchase? (1-5)
        -----------------------------------------------
        [ 1 ] Food              $20
        [ 2 ] Bullets           $30
        [ 3 ] Fuel              $40
        [ 4 ] Phone Charger     $20
        [ 5 ] Hand Sanitizer    $10
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
            item = BULLETS
        elif choice == "5":
            item = FUEL
        elif choice == "6":
            item = PHONE_CHARGE
        elif choice == "8":
            item = HAND_SANITIZER
        
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
        
        print("That will be $%d for a total of $%d." % (total, total_amount_spent))
        
        keep_going = input("Would you like to buy something else? (Y/N) ")
        if keep_going.upper() == "N":
            break
        elif keep_going.upper() == "Y":
            continue
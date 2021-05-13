# Items
FOOD = 'food'
BULLETS = 'bullets'
FUEL = 'fuel'
PHONE_CHARGER = 'phone_charger'
HAND_SANITIZER = 'hand_sanitizer'

list_of_items = [FOOD, BULLETS, FUEL, PHONE_CHARGER, HAND_SANITIZER]

items = {
    FOOD: 20,
    BULLETS: 30,
    FUEL: 40,
    PHONE_CHARGER: 20,
    HAND_SANITIZER: 5
}

def store():
    
    items_buying = {}
    total_amount_spent = 0
    
    while True:
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
        
        if choice == "1":
            item = FOOD
        elif choice == "2":
            item = BULLETS
        elif choice == "5":
            item = FUEL
        elif choice == "6":
            item = PHONE_CHARGER
        elif choice == "8":
            item = HAND_SANITIZER
        
        print("""
        ><><><><><><><><><>><><><><><><><><><><><><><><
                    How many would you like?
        ><><><><><><><><><>><><><><><><><><><><><><><><
              
        """)
        quantity = int(input(">>> "))
        
        # add number of items to items buying dictionary
        items_buying[item] = quantity
        
        # calculate total amount being spent
        total_amount_spent += items[item] * quantity
        
        # total for this specific item
        total = items[item] * quantity
        
        print("That will be $%d for a total of $%d." % (total, total_amount_spent))
        
        keep_going = input("Would you like to buy something else? (Y/N) ")
        if keep_going.upper() == "N":
            break
        elif keep_going.upper() == "Y":
            continue
        
    return {
        'items_bought': items_buying,
        'total_spent': total_amount_spent
    }
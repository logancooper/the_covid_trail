# Items
food = 'food'
bullets = 'bullets'
fuel = 'fuel'
phone_charge = 'phone_charger'
hand_sanitizer = 'hand_sanitizer'

list_of_items = [food, bullets, fuel, phone_charge, hand_sanitizer]

items = {
    food: 20,
    bullets: 30,
    fuel: 40,
    phone_charge: 20,
    hand_sanitizer: 5
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
            item = food
        elif choice == "2":
            item = bullets
        elif choice == "5":
            item = fuel
        elif choice == "6":
            item = phone_charge
        elif choice == "8":
            item = hand_sanitizer
        
        # total for this specific item
        total = items[item] * quantity
        
        # Check if they have enough money to buy this.
        if party.money - total < 0:
            print("You do not have enough money. Please try again.")
            continue
            
        # decrease party total cash amount
        party.money -= total
        
        # add item(s) to inventory
        party.item += quantity
        
        # calculate total amount being spent
        total_amount_spent += items[item] * quantity
        
        print("That will be $%d for a total of $%d." % (total, total_amount_spent))
        
        keep_going = input("Would you like to buy something else? (Y/N) ")
        if keep_going.upper() == "N":
            break
        elif keep_going.upper() == "Y":
            continue
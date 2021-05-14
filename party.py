#List of party members
#Money
#Food
#Hand Sanitizer
#Fuel
#Phone Charge
#Bullets




class Party():
    def __init__(self, party_members, money, food, hand_sanitizer, fuel, phone_charge, bullets):
        self.party_members = party_members
        self.money = money
        self.food = food
        self.hand_sanitizer = hand_sanitizer
        self.fuel = fuel
        self.phone_charge = phone_charge
        self.bullets = bullets

    #Print out party status
    def print_party_status(self):
        for character in self.party_members:
            character.print_stats()
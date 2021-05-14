from characters import *
#List of party members
#Money
#Food
#Hand Sanitizer
#Fuel
#Phone Charge
#Bullets

#check if each individual character is alive
#check if each individual character has ability used
#getSick
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
        print("---------Party Status---------")
        for character in self.party_members:
            character.print_stats()
    #print party supplies
    def print_party_supplies(self):
        print("---------Party Supplies---------\nMoney: %d\nFood: %d\nHand Sanitizer: %d\nFuel: %d\nPhone Charge: %d\nBullets: %d" % (self.money,self.food,self.hand_sanitizer,self.fuel,self.phone_charge,self.bullets))

    def is_alive(self, character):
        if(character == 'doctor'):
            return self.party_members[0].is_alive()
        if(character == 'engineer'):
            return self.party_members[1].is_alive()
        if(character == 'hunter'):
            return self.party_members[2].is_alive()
        if(character == 'influencer'):
            return self.party_members[3].is_alive()
        if(character == 'dj'):
            return self.party_members[4].is_alive()

    def sick_party(self):
        for character in self.party_members:
            character.sick = True

    def used_ability(self,character):
        if(character == 'doctor'):
            return self.party_members[0].skillUsed
        if(character == 'engineer'):
            return self.party_members[1].skillUsed
        if(character == 'hunter'):
            return self.party_members[2].skillUsed
        if(character == 'influencer'):
            return self.party_members[3].skillUsed
        if(character == 'dj'):
            return self.party_members[4].skillUsed

    def use_ability(self, character): 
        if(character == 'doctor'):
            return self.party_members[0].use_special_skill()
        if(character == 'engineer'):
            return self.party_members[1].use_special_skill()
        if(character == 'hunter'):
            return self.party_members[2].use_special_skill()
        if(character == 'influencer'):
            return self.party_members[3].use_special_skill()
        if(character == 'dj'):
            return self.party_members[4].use_special_skill()
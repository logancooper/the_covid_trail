from characters import *

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
    #Print out dead if character is dead
    def print_party_status(self):
        print("---------Party Status---------")
        for character in self.party_members:
            if(character.is_alive()):
                character.print_stats()
            else:
                print(character.name + " is dead")
    #print party supplies
    def print_party_supplies(self):
        print("---------Party Supplies---------\nMoney: %d\nFood: %d\nHand Sanitizer: %d\nFuel: %d\nPhone Charge: %d\nBullets: %d" % (self.money,self.food,self.hand_sanitizer,self.fuel,self.phone_charge,self.bullets))

    #check if character is alive
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

    #make the whole party sick
    def sick_party(self):
        for character in self.party_members:
            character.sick = True

    #check if the ability of a party member is used
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

    #use the ability of a specific party member
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

        #use the ability of a specific party member
    def refresh_ablility(self, character): 
        if(character == 'doctor'):
            return self.party_members[0].restore_special_skill()
        if(character == 'engineer'):
            return self.party_members[1].restore_special_skill()
        if(character == 'hunter'):
            return self.party_members[2].restore_special_skill()
        if(character == 'influencer'):
            return self.party_members[3].restore_special_skill()
        if(character == 'dj'):
            return self.party_members[4].restore_special_skill()

    def get_total_health(self):
        total_health = 0
        for character in self.party_members:
            if(character.is_alive()):
                total_health += character.health
        return total_health
    
    def get_total_morale(self):
        total_morale = 0
        for character in self.party_members:
            if(character.is_alive()):
                total_morale += character.health
        return total_morale

    def get_total_fullness(self):
        total_fullness = 0
        for character in self.party_members:
            if(character.is_alive()):
                total_fullness += character.health
        return total_fullness
    
    def total_alive_members(self):
        total_alive = 0
        for character in self.party_members:
            if(character.is_alive()):
                total_alive += 1
        return total_alive
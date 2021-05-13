#THIS IS A COLLECTION OF CLASSES AND FUNCTIONS RELATED TO CHARACTERS
class Character():
    def __init__(self, name, health, fullness, morale, sickness_multiplier, hunger_multiplier, depression_multiplier):
        self.name = name
        self.health = health
        self.fullness = fullness
        self.morale = morale
        self.sick = False
        self.skillUsed = False
        self.sickness_multiplier = 1
        self.hunger_multiplier = 1
        self.depression_multiplier = 1

    #take damage - subtract incoming damage number from health
    def take_damage(self, incoming_damage):
        self.health -= incoming_damage

    #is alive = return true if alive, false if health <= 0
    def is_alive(self):
        if(self.health <= 0):
            return False
        else:
            return True
    #print stats - print name, health, fullness, and morale of the character
    def print_stats(self):
        print("%s is a GENERIC CHARACTER \nHealth: %d\nFullness: %d\nMorale: %d\nSick: %b" % (self.name,self.health,self.fullness,self.morale,self.sick))
    
    #Special Skill
    def special_skill(self):
        self.skillUsed = True




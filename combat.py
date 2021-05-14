import random
from characters import *
from party import *
def combat(party):
    print("You have entered combat!")
    #generate random list of enemies
    enemy_type = generate_random_enemies()
    #
    return

def generate_random_enemies():
    enemy_type = random.randrange(0,3)
    #if enemy_type == 0:

    return enemy_type

class Enemy():
    def __init__(self, power):
        self.power = power
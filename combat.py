import random
from characters import *
from party import *
from pygame import mixer
mixer.init()
mixer.music.set_volume(0.3)


def combat(party):
    print("You have entered combat!")
    #Generate random enemy
    enemy = generate_random_enemy()
    party_health = party.get_total_health()
    #Greet enemy
    print("A " + enemy.name + " approaches!")
    pause = input("\nPress any key to continue")
    print("\033c")

    #While party health + enemy health are > 0, alternate between these
    while ((party_health and enemy.health) > 0):
        print("Party Health: " + str(party_health) + "\nEnemy Health: " + str(enemy.health) + "\n")
        party_health -= enemy_attack(enemy)
        print("Party Health: " + str(party_health) + "\nEnemy Health: " + str(enemy.health) + "\n")
        pause = input("\nPress any key to continue")
        enemy.health -= party_attack(party)
        print("Party Health: " + str(party_health) + "\nEnemy Health: " + str(enemy.health) + "\n")
        pause = input("\nPress any key to continue")
    
    if(party_health <= 0):
        lose_fight(party, enemy)
    if(enemy.health <= 0):
        win_fight(party, enemy)



def lose_fight(party, enemy):
    print("You lost the fight! Your party will take " + str(enemy.power) + " points of damage distributed across all members")
    print("The enemies stole some of your supplies!")
    for character in party.party_list:
        character.health -= enemy.power/party.total_alive_members()
    party.food -= 10
    party.hand_sanitizer -= 10
    party.fuel -= 10
    party.phone_charge -= 10

def win_fight(party, enemy):
    print("You won the fight! Your party scavenges some supplies from the loot")
    party.food += 10
    party.hand_sanitizer += 10
    party.fuel += 10
    party.phone_charge += 10

#Enemy attacks
def enemy_attack(enemy):
    sound("battle.wav")
    print(enemy.name + " attacks the party for " + str(enemy.power) + " Damage!")
    return enemy.power
#Player attacks
def party_attack(party):
    sound("battle.wav")
    party_power = party.get_total_morale()/4 + party.get_total_health()/4
    print("You attack the enemy for " + str(party_power) + " Damage!")
    return party_power

def generate_random_enemy():
    enemy_type = random.randrange(0,3)
    if enemy_type == 0:    
        enemy = Enemy("Gathering of Rabid Millenials", 50, 50)
    if enemy_type == 1:
        enemy = Enemy("Pack of Zombies", 20, 20)
    if enemy_type == 2:
        enemy = Enemy("Group of Anti-Vaxx Karens", 25, 75)
    if enemy_type == 3:
        enemy = Enemy("Rave of Spring Breakers", 75, 25)
    return enemy

class Enemy:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health
        
        
def sound(file):
    sound = mixer.Sound("audio/%s" % file)
    return mixer.Sound.play(sound)
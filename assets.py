#Holds assets for the covid trail gameplay.


#Music
from pygame import mixer

mixer.init()
mixer.music.set_volume(0.3)

def sound(file):
    sound = mixer.Sound("audio/%s" % file)
    return mixer.Sound.play(sound)

#Artwork

def main_title():
   print("""\033[1;32;40m
                                                        Welcome to

 ________  __                         ______    ______   __     __  ______  _______         ________                  __  __ 
/        |/  |                       /      \  /      \ /  |   /  |/      |/       \       /        |                /  |/  |
$$$$$$$$/ $$ |____    ______        /$$$$$$  |/$$$$$$  |$$ |   $$ |$$$$$$/ $$$$$$$  |      $$$$$$$$/______   ______  $$/ $$ |
   $$ |   $$      \  /      \       $$ |  $$/ $$ |  $$ |$$ |   $$ |  $$ |  $$ |  $$ |         $$ | /      \ /      \ /  |$$ |
   $$ |   $$$$$$$  |/$$$$$$  |      $$ |      $$ |  $$ |$$  \ /$$/   $$ |  $$ |  $$ |         $$ |/$$$$$$  |$$$$$$  |$$ |$$ |
   $$ |   $$ |  $$ |$$    $$ |      $$ |   __ $$ |  $$ | $$  /$$/    $$ |  $$ |  $$ |         $$ |$$ |  $$/ /    $$ |$$ |$$ |
   $$ |   $$ |  $$ |$$$$$$$$/       $$ \__/  |$$ \__$$ |  $$ $$/    _$$ |_ $$ |__$$ |         $$ |$$ |     /$$$$$$$ |$$ |$$ |
   $$ |   $$ |  $$ |$$       |      $$    $$/ $$    $$/    $$$/    / $$   |$$    $$/          $$ |$$ |     $$    $$ |$$ |$$ |
   $$/    $$/   $$/  $$$$$$$/        $$$$$$/   $$$$$$/      $/     $$$$$$/ $$$$$$$/           $$/ $$/       $$$$$$$/ $$/ $$/ 
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                         A text-based adventure game by team TBA

""")

def game_over():
   sound("game_over.wav")
   print("""
   
 $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\        $$$$$$\  $$\    $$\ $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|      $$  __$$\ $$ |   $$ |$$  _____|$$  __$$\ 
$$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ |            $$ /  $$ |$$ |   $$ |$$ |      $$ |  $$ |
$$ |$$$$\ $$$$$$$$ |$$\$$\$$ $$ |$$$$$\          $$ |  $$ |\$$\  $$  |$$$$$\    $$$$$$$  |
$$ |\_$$ |$$  __$$ |$$ \$$$  $$ |$$  __|         $$ |  $$ | \$$\$$  / $$  __|   $$  __$$< 
$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |            $$ |  $$ |  \$$$  /  $$ |      $$ |  $$ |
\$$$$$$  |$$ |  $$ |$$ | \_/ $$ |$$$$$$$$\        $$$$$$  |   \$  /   $$$$$$$$\ $$ |  $$ |
 \______/ \__|  \__|\__|     \__|\________|       \______/     \_/    \________|\__|  \__|
                                                                                          
                                                                                          
                                                                                          
""")
   pause = input("Press any key to quit the game.")
   quit()

def success():
   sound("win.wav")
   print("""

  ______   _______   ________   ______   ________         ______   __    __   ______    ______   ________   ______    ______   __ 
 /      \ /       \ /        | /      \ /        |       /      \ /  |  /  | /      \  /      \ /        | /      \  /      \ /  |
/$$$$$$  |$$$$$$$  |$$$$$$$$/ /$$$$$$  |$$$$$$$$/       /$$$$$$  |$$ |  $$ |/$$$$$$  |/$$$$$$  |$$$$$$$$/ /$$$$$$  |/$$$$$$  |$$ |
$$ | _$$/ $$ |__$$ |$$ |__    $$ |__$$ |   $$ |         $$ \__$$/ $$ |  $$ |$$ |  $$/ $$ |  $$/ $$ |__    $$ \__$$/ $$ \__$$/ $$ |
$$ |/    |$$    $$< $$    |   $$    $$ |   $$ |         $$      \ $$ |  $$ |$$ |      $$ |      $$    |   $$      \ $$      \ $$ |
$$ |$$$$ |$$$$$$$  |$$$$$/    $$$$$$$$ |   $$ |          $$$$$$  |$$ |  $$ |$$ |   __ $$ |   __ $$$$$/     $$$$$$  | $$$$$$  |$$/ 
$$ \__$$ |$$ |  $$ |$$ |_____ $$ |  $$ |   $$ |         /  \__$$ |$$ \__$$ |$$ \__/  |$$ \__/  |$$ |_____ /  \__$$ |/  \__$$ | __ 
$$    $$/ $$ |  $$ |$$       |$$ |  $$ |   $$ |         $$    $$/ $$    $$/ $$    $$/ $$    $$/ $$       |$$    $$/ $$    $$/ /  |
 $$$$$$/  $$/   $$/ $$$$$$$$/ $$/   $$/    $$/           $$$$$$/   $$$$$$/   $$$$$$/   $$$$$$/  $$$$$$$$/  $$$$$$/   $$$$$$/  $$/ 
                                                                                                                                  
                                                                                                                                  
                                                                                                                                  
""")
   pause = input("Press any key to end the game.")

#Intro/Background
intro_text = """
The year is 2020       

A mysterious illness has spread across the world, and each day the number of infections is growing.

To make matters worse, supply chain issues have left the country with a severe toilet paper shortage. 

Many have chosen to lock themselves away in their homes, only emerging into the light to receive door dash meal deliveries.

But not you... You've heard of a city in the far west called Portland, where the toilet paper flows freely and avocado toast is served for breakfast, lunch, and dinner.

Today, you set out from Atlanta with a team of capable allies with one goal...

To make it to Portland in the next 10 days, braving disease, disaster, and all kinds of danger.

"""


  

character_info = """ Your team consists of five specialists who each have different qualities and skills.



THE DOCTOR: Able to cure the party's sickness and restore health. Low risk of sickness, moderate hunger, and prone to depression.

THE ENGINEER: Able to repair your vehicle and navigate around obstacles. Medium risk of sickness, medium hunger, and medium risk of depression.
Medium risk of sick

THE HUNTER: Able to hunt for food while in between cities. High risk of sickness, high hunger, and medium risk of depression.

THE INFLUENCER: Special skills: none   High risk of sickness, high hunger, and prone to depression.

THE D.J.: Able to increase the morale of the entire party to counteract cell tower outages. Medium risk of sickness, medium hunger, and low risk of depression
"""


#Text blurbs to introduce each day


day_01 = """
Day One - On the road from Atlanta heading northwest.
"""

day_02 = """
Day Two - Still on the road toward Kansas City. 
We should be there by tomorrow.
"""

day_03 = """
Day Three - You've reached Kansas City, MO. Unfortunately, a freak gasoline fight accident has closed your favorite BBQ joint.
"""

day_04 = """
Day Four - Leaving Kansas City and heading west to Denver. The air is getting cooler.
"""

day_05 = """
Day Five - You've reached Denver, CO -- the Mile High City! Maybe there's time to stop and take in the views.
"""

day_06 = """
Day Six - On the road from Denver, heading northwest
"""

day_07 = """
Day Seven - Still on the road toward Boise, ID
"""

day_08 = """
Day Eight - You've reached Boise, ID -- the last stop before Portland
"""

day_09 = """
Day Nine - On the road toward Portland.
"""

day_10 = """
We made it Portland!! You win!
"""
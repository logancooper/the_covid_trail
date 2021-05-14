#Holds assets for the covid trail gameplay.


#Music



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

def choose_members(): 
   print("First, choose the members of your party: ")
  

character_info = """ Your team consists of five specialists who each have different qualities and skills.
[ 1 ] THE DOCTOR: Able to cure the party's sickness and restore health. Low risk of sickness, moderate hunger, and prone to depression.

[ 2 ] THE ENGINEER: Able to repair your vehicle and navigate around obstacles. Medium risk of sickness, medium hunger, and medium risk of depression.
Medium risk of sick

[ 3 ] THE HUNTER: Able to hunt for food while in between cities. High risk of sickness, high hunger, and medium risk of depression.

[ 4 ] THE INFLUENCER: Special skills: none   High risk of sickness, high hunger, and prone to depression.

[ 5 ] THE D.J.: Able to increase the morale of the entire party to counteract cell tower outages. Medium risk of sickness, medium hunger, and low risk of depression
"""


#Text blurbs to introduce each day


day_01 = """
Day One - We're on the road from Atlanta heading west.
"""

day_02 = """
Day Two - Still on the road toward Kansas City. 
We should be there by tomorrow
"""

day_03 = """
Day Three - You've reached Kansas City, MO
"""

day_04 = """
Day Four - Leaving Kansas City and heading west to Denver.
"""

day_05 = """
Day Five - You've reached Denver, CO.
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
You made it Portland!!
"""
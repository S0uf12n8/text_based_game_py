import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

## player setup ##
class player:
    def __init__(self):
        self.name=''
        self.hp= 0
        self.mp=0
        self.aura=0
        self.status_effects=[]
        self.location = 'start'
myPlayer = player()

#### title screen ###
def title_screen_selection():
    option = input(">")
    if option.lower()== ("play"):
        start_game()
    elif option.lower()==("help"):
        help_menu()
    elif option.lower()==("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help','quit']:
        print("Please enter a Valid Command")
        option=input(">")
        if option.lower()== ("play"):
            start_game()
        elif option.lower()==("help"):
            help_menu()
        elif option.lower()==("quit"):
            sys.exit()
        
def title_screen():
    os.system('clear')
    print("#####################################")
    print("         # wach a 3zi #              ")
    print("#####################################")
    print("              -play-                 ")
    print("              -help-                 ")
    print("              -quit-                 ")
    print("       copyright IBshiinak           ")
    title_screen_selection()
def help_menu():
    print("#####################################")
    print("          # wach a 3zi #             ")
    print("#####################################")
    print("              -wachnta 7mar-         ")
    print("      -ma3linach ha kifach tl3b-     ")
    print("          -up,down,left,right-       ")
    print("    ktb les command bach tkhdmhom    ")
    print("       ktb look bach tchof           ")
    print("             ylh 7yd 3liya           ")


#### game functionalty###
def start_game():
    return




### map ####
"""
a1 a2 a3 a4
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
|  |  |  |  |
-------------
"""


ZONENAME=''
DESCRIPTION = 'description'
EXAMINATION =  'examine'
SOLVED = False
UP = 'up','north'
DOWN = 'down','south'
LEFT = 'left','west'
RIGHT = 'right','east'


solved_place = {'a1':False,'a2':False,'a3':False,'a4':False,
               'b1':False,'b2':False,'b3':False,'b4':False,
                'c1':False,'c2':False,'c3':False,'c4':False,
                'd1':False,'d2':False,'d3':False,'d4':False, 
                }

zonemap = {
    'a1' : {
        ZONENAME : "sta7 ",
        DESCRIPTION = 'description'
        EXAMINATION =  'examine'
        SOLVED = False
        UP = ''
        DOWN = 'b1'
        LEFT = ''
        RIGHT = 'a2'
    },
    'a2' : {
        ZONENAME : "lwste",
        DESCRIPTION = 'description'
        EXAMINATION =  'examine'
        SOLVED = False
        UP = ''
        DOWN = 'b2'
        LEFT = 'a1'
        RIGHT = 'a3'
    },
    'a3' : {
        ZONENAME : "sefly",
        DESCRIPTION = 'description'
        EXAMINATION =  'examine'
        SOLVED = False
        UP = ''
        DOWN = 'b3'
        LEFT = 'a2'
        RIGHT = 'a4'
    },
    'a4' : {
        ZONENAME : "lakabe hh",
        DESCRIPTION = 'description'
        EXAMINATION =  'examine'
        SOLVED = False
        UP = ''
        DOWN = 'b4'
        LEFT = 'a3'
        RIGHT = ''
    },
    'b1' : {
        ZONENAME : "",
        DESCRIPTION = 'description'
        EXAMINATION =  'examine'
        SOLVED = False
        UP = 'a1'
        DOWN = 'c1'
        LEFT = ''
        RIGHT = 'b2'
    },
    'b2' : {
        ZONENAME : 'dar',
        DESCRIPTION = 'hadi hiya dark'
        EXAMINATION =  'sf 9awd matrf3ch liya kri'
        SOLVED = False
        UP = 'a2'
        DOWN = 'c2'
        LEFT = 'b1'
        RIGHT = 'b3'
    },

}

### game intractivity ####
def print_location ():
    print('\n' + ('#'*(4+ len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + '#')
    print('#'+zonemap[myPlayer.position][DESCRIPTION]+ '#')
    print('\n' + ('#'*(4+ len(myPlayer.location))))

def promet():
    print("\n" + "========================")
    print("what would like to do ")
    action = input("> ")
    acceptable_actions = ['move','go','trave','walk','quit','examine','inspect','interact','look']
    while action.lower() not in acceptable_actions :
        print("ach kadir khtar azbi mzyan :  \n")
        print("ila ma3rftich khtar mn hado : ")
        print(acceptable_actions, '\n')
        action = input("> ")
    if action.lower() == 'quit' :
        sys.exit()
    elif action.lower() in ['move','go','trave','walk']:
        player_move(action.lower())
    elif action.lower() in ['examine','inspect','interact','look']:
        player_examain(action.lower())

def player_move(myAction):
    ask = "fin ghad a si zbi  \n"
    dest = input(ask)
    if dest in ['up','north']:
        destinatnion = zonemap[myPlayer.location][UP]
        movement_handler()
    elif dest in ['left','west'] :
        destinatnion = zonemap[myPlayer.location][LEFT]
        movement_handler()
    elif dest in ['east','right'] :
        destinatnion = zonemap[myPlayer.location][RIGHT]
        movement_handler()
    elif dest in ['south','down'] :
        destinatnion = zonemap[myPlayer.location][DOWN]
        movement_handler()

def movement_handler():
    print("\n"+" You have moved to " + destinatnion + ".")
    myPlayer.location = destinatnion
    print_location()


def player_examain(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("you have already exhusted this zone. ")
    else :
        print("you cant tregert puzzle here")
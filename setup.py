from classes.Text import textFunc as text
from classes.Utility import Utilities as util
import classes._Player as _Player
from classes.Database import Database as db
import re
import player_action as action
import textwrap
import os
import loot_table
import sys


        
# if game.db exists return true else return false
def check_for_db():
    if os.path.exists('db/game.db'):
        return True
    else:
        return False
    
def create_db():
    db('db/game.db')
    db.create_game_tables()
    loot_table.setup_inventory()
    print("Database and tables created!")

def validate_name_input(name):
    name_clean = re.sub(r'[^a-zA-Z]', '', name)
    if name_clean != '':
        return name_clean
    elif name_clean == '':
        return False
    else:
        return False
    
       
def setup_player() -> _Player.Player:

    util.clear_term(0)
    
    #### PLAYER CREATION ####
    NAMED = False
    
    while not NAMED:

        util.scroll_text("What is your name?\n", 0.03)
        
        name = input('> ')
        name = validate_name_input(name)
        
        if name != False:
            ply = _Player.Player(name)
            NAMED = True
        else:
            util.scroll_text("Please enter a valid name.\n", 0.05)
            continue
        
    util.clear_term(0)
    
    #### ROLE ASSIGNMENT ####
    ask_role = """
                Please choose one of the following roles: 
                1. Warrior
                2. Mage
                """
    ask_role = textwrap.dedent(ask_role)
    
    util.scroll_text(ask_role, 0.05)
    role_choice = input('> ')
    util.clear_term(0)

    while True:
        if role_choice == '1':
            ply.role = 'Warrior'
            ply.set_player_stats()
            util.scroll_text("You have chosen Warrior", 0.05)
            util.spacing(2)
            input("Press Enter/Return to continue")
            break
        elif role_choice == '2':
            ply.role =  'Mage'
            ply.set_player_stats()
            util.scroll_text("You have chosen Mage", 0.05)
            util.spacing(2)
            input("Press Enter/Return to continue")
            break
        else:
            print('A number was not entered!')
            util.clear_term(1)
            util.scroll_text(ask_role, 0.05)
            role_choice = input('> ')
            continue
    
    util.clear_term(0) 
    text.welcome_speech()
    util.clear_term(0.95)

    return ply     
    
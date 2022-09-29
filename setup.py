from classes.Text import textFunc as text
from classes.Utility import Utilities as util
from classes.Player import Player
from classes.Database import Database as db
import re
import player_action as action
import textwrap
import os
import loot_table


def main_game_loop(player):
    while player.end == False:  
        action.prompt(player)
        
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
    
    
        
def game():
    
    util.clear_term(0)
    
    #### PLAYER NAME SETUP #####
    is_named = False
    role = None
    
    while is_named == False:
        
        util.scroll_text("What is your name?\n", 0.05)
        
        name = input('> ')
        name_clean = re.sub(r'[^a-zA-Z]', '', name)
        
        if name_clean != '':
            player = Player(name_clean, role)
            is_named = True
            break
        elif name_clean == '':
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
            role = 'Warrior'
            player.role = role
            player.set_player_stats(role)
            util.scroll_text("You have chosen Warrior -- here are your starting stats:", 0.05)
            util.spacing(2)
            text.print_player_info(player)
            input("Press Enter/Return to continue")
            break
        elif role_choice == '2':
            role =  'Mage'
            player.role = role
            player.set_player_stats(role)
            util.scroll_text("You have chosen Mage -- here are your starting stats:", 0.05)
            util.spacing(2)
            text.print_player_info(player)
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
    
    is_set_up = True
    
    return (is_set_up, player)           
    
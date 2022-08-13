#pyRPG v2
#Carter Reynolds

from unicodedata import numeric
from classes.Text import textFunc as text
from classes.Utility import Utilities as util
from classes.Player import Player
from dictionaries.world import zonemap_dict, solved_places
import sys
import time
import random as rand
import re

def title_screen(): # Load title screen
    util.clear_term(0)
    text.display_menu(menu='main')
    title_screen_selections()
        
def help_menu():
    util.clear_term(0)   
    text.display_menu(menu='help')
    title_screen_selections()
        
def title_screen_selections(): 
    while True:
        option = input('> ')
        if option == '1':
            setup_game()
            verified = True
        elif option == '2':
            help_menu()
        elif option == '3':
            sys.exit()
        else:
            continue
        
def setup_game():
    util.clear_term(0)
    
    #### PLAYER NAME SETUP #####
    is_named = False
    role = 'null'
    
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
    ask_role = """Please choose one of the following roles:
1. Warrior
2. Mage
"""
    util.scroll_text(ask_role, 0.05)
    role_choice = input('> ')
    util.clear_term(0)

    while True:
        if role_choice == '1':
            role =  'Warrior'
            player.set_player_stats(role)
            util.scroll_text("You have chosen Warrior -- here are your starting stats:", 0.05)
            util.spacing(2)
            text.print_player_info(player)
            input("Press Enter/Return to continue")
            break
        elif role_choice == '2':
            role =  'Mage'
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
    main_game_loop(player)
            
def prompt(player):
    
    system_actions = ['quit']
    move_actions = ['move', 'go', 'travel', 'traverse', 'walk']
    examine_actions = ['examine', 'inspect', 'look']
    
    verify_action = system_actions + move_actions + examine_actions
    
    text.print_player_info(player)
    
    print("What would you like to do?")
    util.spacing(1)
    action = input("> ")
    
    while True:
        if action not in verify_action:
            util.clear_term(0)
            print("Invalid Action... Try Again.\n")
            util.clear_term(1)
            prompt(player)
            continue
        elif action in system_actions:
            if action == 'quit':
                sys.exit()
        elif action in move_actions:
            player_move(action, player)
            break
        elif action in examine_actions:
            player_examine(action, player)
            break   
                     
def player_move(action, player):
    
    util.clear_term(0)
    
    movement_directions = ['up', 'down', 'left', 'right', 'north', 'south', 'east', 'west']
    
    ask = "What direction would you like to move in?"
    
    print(ask + '\n')
    dest = input('> ')
    
    while True:
        if dest not in movement_directions:
            util.clear_term(0)
            print('Invalid Direction!')
            util.clear_term(2)
            player_move(action, player)
            continue
        if dest in movement_directions:
            if dest in ['up', 'north']:
                destination = zonemap_dict[player.location]['UP']
                movement_handler(destination, player)
                break
            elif dest in ['down', 'south']:
                destination = zonemap_dict[player.location]['DOWN']
                movement_handler(destination, player)
                break
            elif dest in ['left', 'west']:
                destination = zonemap_dict[player.location]['LEFT']
                movement_handler(destination, player)
                break
            elif dest in ['right', 'east']:
                destination = zonemap_dict[player.location]['RIGHT']
                movement_handler(destination, player)
                break
            
def movement_handler(destination, player):
    
    util.clear_term(0)
    
    if destination == '':
        print('Unable to move this direction!')
        time.sleep(1.5)
        prompt(player)
    else:
        player.location = destination
        player.alter_stamina(1, 0)
        util.scroll_text("Traveling....", 0.05)
        util.clear_term(2)
        util.scroll_text(("You have arrived at " + destination + "."), 0.05)
        util.clear_term(2)
        text.print_location(player)
    
def player_examine(action, player):
    
    util.clear_term(0)
    
    if zonemap_dict[player.location]['SOLVED'] is True:
        print("You have solved this zone and there is nothing further to examine!")
    else:
        util.scroll_text((zonemap_dict[player.location]['ZONENAME'] + ':\n' + zonemap_dict[player.location]['EXAMINATION']), 0.05)
        util.spacing(2)
        input("Press Enter/Return to continue.")
        prompt(player)
        
def main_game_loop(player):
    while player.end == False:  
        prompt(player)
        
title_screen() # Title Screen starts the game essentially

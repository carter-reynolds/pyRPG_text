from classes.Text import textFunc as text
from classes.Utility import Utilities as util
from dictionaries.world import zonemap_dict, zonemap_meta
import menu
import time
import sys
import encounter as event
import fight
from termcolor import colored as _color


def prompt(player):
    
    PROMPT = True
    
    system_actions = ['quit', 'pause', 'actions']
    move_actions = ['move', 'go', 'travel', 'traverse', 'walk']
    examine_actions = ['examine', 'inspect', 'look']
    combat_actions = ['attack', 'run', 'heal']
    
    valid_actions = system_actions + move_actions + examine_actions + combat_actions
    
    while PROMPT:
        
        util.clear_term(0)
        
        text.get_cur_stats(player)
        
        print("What would you like to do?")
        
        util.spacing(1)
        
        action = input("> ")
        action = action.lower()
        
        if action not in valid_actions:
            util.clear_term(0)
            print("Invalid Action.")
            print(_color("Type 'actions' to see a list of valid actions.", 'red', attrs=['blink', 'bold']))
            util.clear_term(1)
            continue
        elif action in system_actions:
            if action == 'quit':
                sys.exit()
            elif action == 'pause':
                menu.pause_menu(player)
            elif action == 'actions':
                pass
        elif action in move_actions:
            player_move(action, player)
        elif action in examine_actions:
            player_examine(action, player) 
        elif action in combat_actions():
            pass

                    
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
                destination = zonemap_dict[player.location]['MOVEMENT']['UP']
                movement_handler(destination, player)
                break
            elif dest in ['down', 'south']:
                destination = zonemap_dict[player.location]['MOVEMENT']['DOWN']
                movement_handler(destination, player)
                break
            elif dest in ['left', 'west']:
                destination = zonemap_dict[player.location]['MOVEMENT']['LEFT']
                movement_handler(destination, player)
                break
            elif dest in ['right', 'east']:
                destination = zonemap_dict[player.location]['MOVEMENT']['RIGHT']
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
        encounter_enemy = event.encounter_check(destination)
        input("Press Enter/Return to continue.")
        
        if not encounter_enemy:
            
            util.clear_term(0)
            util.scroll_text(("You have arrived at " + destination + "."), 0.05)
            util.clear_term(2)
            prompt(player)
        else:
            util.clear_term(0)
            fight.fight(player)
            util.clear_term(2)
            prompt(player)
            
        util.clear_term(2)
        util.scroll_text(("You have arrived at " + destination + "."), 0.05)
        util.clear_term(2)
        text.print_location(player)
    
def player_examine(action, player):
    
    util.clear_term(0)
    
    if zonemap_meta[player.location]['solved'] is True:
        print("You have solved this zone and there is nothing further to examine!")
    else:
        util.scroll_text((zonemap_dict[player.location]['ZONENAME'] + ':\n' + zonemap_dict[player.location]['EXAMINATION']), 0.05)
        util.spacing(2)
        input("Press Enter/Return to continue.")
        prompt(player)

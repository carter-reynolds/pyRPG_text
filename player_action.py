from classes.Text import textFunc as text
from classes.Utility import Utilities as util
from dictionaries.world import zonemap_dict
import time
import sys

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
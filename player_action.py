from classes.Text import textFunc as text
from classes.Utility import Utilities as util
from dictionaries.world import zonemap_dict, zonemap_meta
from dictionaries.world_strings import action_strings
import menu
import time
import sys
import encounter as event
import fight
from termcolor import colored as _color
import random as rand


# handles most of the command input and movement for the player

def prompt(player):
    
    PROMPT = True
    
    # Define actions by type that can be used in the game
    system_actions = ['quit', 'pause', 'actions']
    move_actions = ['move', 'go', 'travel', 'traverse', 'walk', 'run', 'head']
    examine_actions = ['examine', 'inspect', 'look']
    special_actions = ['rest', 'sit']
    
    # Combine them all together now so we can easily check all of them during input
    valid_actions = system_actions + move_actions + examine_actions + special_actions
    
    message = "" # This will be used to display messages to the player
    
    
    while PROMPT:
        
        util.clear_term(0)
        
        text.get_cur_stats(player) # Prints the current stats of the player such as health, stamina, etc.
        
        print(message)
        
        util.spacing(1)
        
        action = input("What would you like to do?\n> ")
        action = action.lower()
        
        if action not in valid_actions:
            util.clear_term(0)
            print("Invalid Action.")
            print(_color("Type 'actions' to see a list of valid actions.", 'red', attrs=['bold', 'underline']))
            util.clear_term(2)
            continue
        else:
            if action in system_actions:
                if action == 'quit':
                    sys.exit()
                elif action == 'pause':
                    menu.pause_menu(player)
                elif action == 'actions':
                    menu.actions_menu(valid_actions)
                    
            elif action in move_actions:
                player_move(action, player)
                
            elif action in examine_actions:
                player_examine(action, player)
                
            elif action in special_actions:
                if (action == 'rest') or (action == 'sit'):
                    message = check_can_rest(player, action)
                    continue
                
def check_can_rest(player, action):
    
    if action == 'rest':
        
        # Check if the player is in a zone that can be rested in
        PLAYER_CAN_REST = zonemap_meta[player.location]['can_rest']
          
        if PLAYER_CAN_REST is True:
            message = "You have rested and recovered your health and stamina."
            player.rest()  
        else:
            message = "You cannot rest here! You can safely 'sit' to recover some stamina, however."
    
    # We don't want the player to get stranded in a zone with no way to recover stamina, so we'll allow them to sit anywhere
    elif action == 'sit':
        message = "You sit down and relax for a moment. Gain 1 stamina."
        player.alter_stamina(2*player.level+1, 1) # Eventually there will be a modifier for this, but for now it's just 1
        if event.encounter_check(player.location):
            unsafe_strings = action_strings['sitting_unsafe']
            encounter_str = unsafe_strings[rand.randint(0, len(unsafe_strings) - 1)]
            util.clear_term()
            util.scroll_text(encounter_str, 0.05)
            time.sleep(3)
            fight.fight(player)
        else:
            safe_strings = action_strings['sitting_safe']
            message = safe_strings[rand.randint(0, len(safe_strings) - 1)]
            util.clear_term()
            time.sleep(3)

    return message
        
                        

                    
def player_move(action, player):
    
    util.clear_term()
    
    movement_directions = ['up', 'down', 'left', 'right', 'north', 'south', 'east', 'west']
    
    dest = input(f"What direction would you like to {action}?\n> ")
    dest = dest.lower()
    
    while True:
        if dest not in movement_directions:
            util.clear_term()
            print('Invalid Direction!')
            util.clear_term(2)
            player_move(action, player)
        else:
            if dest in ['up', 'north']:
                destination = zonemap_dict[player.location]['MOVEMENT']['UP']
                movement_handler(destination, player)
            elif dest in ['down', 'south']:
                destination = zonemap_dict[player.location]['MOVEMENT']['DOWN']
                movement_handler(destination, player)
            elif dest in ['left', 'west']:
                destination = zonemap_dict[player.location]['MOVEMENT']['LEFT']
                movement_handler(destination, player)
            elif dest in ['right', 'east']:
                destination = zonemap_dict[player.location]['MOVEMENT']['RIGHT']
                movement_handler(destination, player)
            
def movement_handler(destination, player):
    
    util.clear_term()
    
    if destination == '':
        print('Unable to move this direction!')
        time.sleep(1.5)
        prompt(player)
    else:
        player.location = destination
        player.alter_stamina(10, 0)
        util.scroll_text("Traveling....", 0.05)
        encounter_enemy = event.encounter_check(destination)
        
        if not encounter_enemy:
            util.clear_term(2)
            util.scroll_text(("You have arrived at " + zonemap_dict[destination]['ZONENAME'] + "."), 0.05)
            util.clear_term(2)
            prompt(player)
        else:
            util.clear_term(2)
            util.scroll_text("You have encountered an enemy!", 0.05)
            util.clear_term(2)
            fight.fight(player)
            
            REVIVE = False
            
            while not REVIVE:
                # Once the fight finishes, figure out if the player died and offer a revive or quit option.
                if player.cur_health <= 0:
                    util.clear_term()
                    util.scroll_text("You have died!", 0.05)
                    util.scroll_text("Pay 50 gold to revive?", 0.05, 2)
                    answer = input("(Y/N)\n>")
                    answer = answer.lower()
                    
                    if answer == 'y':
                        if player.gold >= 50:
                            player.gold -= 50
                            player.health = player.max_health
                            player.stamina = player.max_stamina
                            util.clear_term()
                            util.scroll_text("You have been revived!", 0.05)
                            util.clear_term(2)
                            REVIVE = True
                        else:
                            util.clear_term()
                            util.scroll_text("You don't have enough gold. Goodbye cruel world.", 0.05)
                            util.clear_term(2)
                            player.end = True
                            menu.main_menu()
                    elif answer == 'n':
                        util.clear_term()
                        util.scroll_text("You have died...", 0.05)
                        util.clear_term(2)
                        player.end = True
                        menu.main_menu()
                    else:
                        util.clear_term()
                        util.scroll_text("Invalid Input!", 0.05)
                        util.clear_term(2)
                        continue
                else:
                    REVIVE = True
                
            util.clear_term()
            util.scroll_text(("You have arrived at " + zonemap_dict[destination]['ZONENAME'] + "."), 0.05)
            util.clear_term(2)
            prompt(player)
    
def player_examine(action, player):
    
    util.clear_term()
    
    if zonemap_meta[player.location]['solved'] is True:
        print("You have solved this zone and there is nothing further to examine!")
    else:
        util.scroll_text((zonemap_dict[player.location]['ZONENAME'] + ':\n' + zonemap_dict[player.location]['EXAMINATION']), 0.05)
        util.spacing(2)
        input("Press Enter/Return to continue.")
        prompt(player)


from classes.Player import Player
from classes.Enemies import Enemy
from classes.Database import Database as db
import random as rand
import player_action as action
from classes.Utility import Utilities as util
from classes.Text import textFunc as text
from termcolor import colored as _color

def fight(player):
    
    RAN_AWAY = False # Used to break out of the fight loop
    
    random_type = rand.randint(0, 3) # Randomly choose an enemy type
    
    # Randomly choose an enemy level based on player level
    if player.level == 0:
        random_level = rand.randint(0, 1)
    elif player.level == 1:
        random_level = rand.randint(0, 2)
    elif player.level == 2:
        random_level = rand.randint(1, 3)
    elif player.level == 3:
        random_level = rand.randint(2, 3)
    else:
        pass

    enemy = Enemy(random_type, random_level) # Create the enemy - set stats by type and level
    
    while not RAN_AWAY: # While the player has not run away
        
        util.clear_term(0)
        
        text.get_enemy_stats(enemy) # Print the enemy stats
        
        PLAYER_ATTACKING = True
        ENEMY_ATTACKING = False
        
        if ENEMY_ATTACKING:
            pass
        else:
            
            message = ""
            
            while PLAYER_ATTACKING:
                
                attack_actions = ["attack", "hit", "fight", "kill", "run"]
                
                util.clear_term(0)
                
                text.get_enemy_stats(enemy) # Print the enemy stats
                print()
                text.get_cur_stats(player) # Print the player stats
                
                util.spacing(1)
                
                print(message, '\n')
                
                action = input("What do you want to do?\n>")
                action = action.lower()
                
                if action in attack_actions: 
                    if action != 'run':
                        pass
                    elif action == 'run':
                        print("You ran away!")
                        PLAYER_ATTACKING = False
                        RAN_AWAY = True
                        break
                    
                    damage = player.cur_attack 
                
                    player_damage_done = enemy.take_damage(damage) 
                
                    if not player_damage_done[0]: # If damage was not done, print the reason 
                        player.cur_health -= (enemy.attack - player.cur_defense)
                        message = player_damage_done[1]
                        
                    else:
                        
                        message = player_damage_done[1] # If damage was done, print the message
                        
                        if enemy._defeated():
                            util.clear_term(0)
                            util.scroll_text(_color(f'You defeated {enemy.name}!\n', 'green'), 0.05)
                            PLAYER_ATTACKING = False
                            ENEMY_ATTACKING = False
                            RAN_AWAY = False
                            break
                        else:
                            continue
                else:
                    continue            
            
        if RAN_AWAY == True:
            LOOTING = False                 
        else: 
            LOOTING = True
        
        while LOOTING:
            action = input("Do you want to loot the enemy?\n> ")
            
            loot_actions = ["yes", "y", "loot", "take"]
            
            if action in loot_actions:
                print("You loot the enemy!")
                player.gold += enemy.gold
                
                util.clear_term(2, f'You gained {str(enemy.gold)} gold!')
                util.clear_term(2, "You found the following items:\n")
                
                for item in enemy.loot:
                    
                    print('\u25BA ' + item + '\n')
                    
                    for key, value in player.inventory.items():
                        if key == item:
                            player.inventory[key] += 1
                        else:
                            player.inventory[item] = 1
                input("Press enter to continue...")
                
                if input:             
                    LOOTING = False
                    break
            else:
                print("You leave the enemy alone.")
                LOOTING = False
                
        return None
            
                        
                   
                
                
                
                
    
        
         
    
    
    
    
    
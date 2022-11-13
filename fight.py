from classes.Enemies import Enemy
import random as rand
from classes.Utility import Utilities as util
from classes.Text import textFunc as text
from termcolor import colored as _color

def fight(player):
    
    """Fight a random enemy
    
    # TODO: This eventually needs massive clean up and refactoring

    Returns:
        None
    """
    
    RAN_AWAY = False # Used to break out of the fight loop
    
    random_type = rand.randint(0, 3) # Randomly choose an enemy type
    
    

    enemy = Enemy(random_type) # Create the enemy - set stats by type and level
    
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
                
                attack_actions = ["attack", "hit", "fight", "kill", "run", "heal"]
                
                util.clear_term(0)
                
                text.get_enemy_stats(enemy) # Print the enemy stats
                util.spacing(1)
                text.get_cur_stats(player) # Print the player stats
                
                util.spacing(1)
                
                print(message, '\n')
                
                action = input("What do you want to do?\n> ")
                action = action.lower()
                
                if action in attack_actions: 
                    if action != 'run':
                        if action == 'heal':
                            player_try_heal = player.use_health_potion() # Try to heal the player
                            
                            # The above returns a tuple: (success bool, message)
                            player_did_heal = player_try_heal[0] # The first value is a boolean that tells us if the player was able to heal
                            message = player_try_heal[1] # The second value is a string that tells us what happened
                            continue
                        else:
                            pass
                    elif action == 'run':
                        print("You ran away!")
                        PLAYER_ATTACKING = False
                        RAN_AWAY = True
                        break
                    
                    
                    damage = player.cur_attack 
                
                    player_damage_done = enemy.take_damage(damage) 
                
                    if not player_damage_done[0]: # If damage was not done, print the reason and take damage
                        player.cur_health -= (enemy.attack - player.cur_defense)
                        message = player_damage_done[1]
                        
                    else:
                        
                        message = player_damage_done[1] # If damage was done, print the message
                        player.alter_stamina(5, 0) # Decrease stamina by 5 since we attacked
                        
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
                
                # TODO: Player still needs to gain experience from defeating an enemy
                
                for item in enemy.loot:
                    
                    print('\u25BA ' + item + '\n')
                    
                    # Check for the item already existing in the player's inventory dictionary
                    if item in player.inventory.keys():
                        player.inventory[item] += 1 # If it does, increment the value by 1
                    else:
                        '''
                            The following conditional statement shouldn't ever run unless the player reloads a game
                            and we added a new object to the game, it will add the new object to the player's inventory
                            when they loot the enemy and find the new item.
                        '''
                        player.inventory[item] = 1 # If it doesn't, add it to the dictionary with a value of 1 
                        
                input("Press enter to continue...")
                
                if input:             
                    LOOTING = False
                    break
            else:
                print("You leave the enemy alone.")
                LOOTING = False
                
        return None
            
                        
                   
                
                
                
                
    
        
         
    
    
    
    
    
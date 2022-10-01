from classes.Player import Player
from classes.Enemies import Enemy
from classes.Database import Database as db
import random as rand
import player_action as action
from classes.Utility import Utilities as util
from classes.Text import textFunc as text

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
            
            while PLAYER_ATTACKING:
                
                util.clear_term(0)
                
                text.get_enemy_stats(enemy) # Print the enemy stats
            
                action = input("What do you want to do? ")
            
                attack_actions = ["attack", "hit", "fight", "kill", "run"]
            
                if action in attack_actions: 
                    if action != 'run':
                        print(f"You attempt to {action} the enemy!")
                    elif action == 'run':
                        print("You ran away!")
                        PLAYER_ATTACKING = False
                        RAN_AWAY = True
                        break
                    
                    damage = player.cur_attack 
                
                    player_damage_done = enemy.take_damage(damage) 
                
                    if not player_damage_done:
                        player.cur_health -= (enemy.attack - player.cur_defense)
                    else:
                        if enemy._defeated():
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
            action = input("Do you want to loot the enemy? ")
            
            loot_actions = ["yes", "y", "loot", "take"]
            
            if action in loot_actions:
                print("You loot the enemy!")
                player.gold += enemy.gold
                
                for _loot in enemy.loot:
                    player.inventory.append(_loot)
                LOOTING = False
            else:
                print("You leave the enemy alone.")
                LOOTING = False
                
        return None
            
   

                        
                    
                
                
                
                
    
        
         
    
    
    
    
    
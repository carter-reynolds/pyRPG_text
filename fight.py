from classes.Player import Player
from classes.Enemies import Enemy
from classes.Database import Database as db
import random as rand
import player_action as action
from classes.Utility import Utilities as util

def fight(player):
    
    run_away = False
    
    random_type = rand.randint(0, 3)
    random_level = rand.randint(0, 3)

    enemy = Enemy(random_type, random_level)
    
    print(f"You are fighting {enemy.name}!")
    
    while not run_away:
        
        print(Enemy.display_stats(enemy))
        
        action = input("What do you want to do? ")
        
        attack_actions = ["attack", "hit", "fight", "kill", "run"]
        
        if action in attack_actions:
            if action != 'run':
                print(f"You attempt to {action} the enemy!")
            elif action == 'run':
                print("You ran away!")
                run_away = True
                break
                
        damage = player.cur_attack
            
        player_damage_done = enemy.take_damage(damage) 
            
        if not player_damage_done:
            player.cur_health -= (enemy.attack - player.cur_defense)
        else:
            continue
        
    if run_away == True:
        looting = False                 
    else: 
        looting = True
    
    while looting:
        action = input("Do you want to loot the enemy? ")
        
        loot_actions = ["yes", "y", "loot", "take"]
        
        if action in loot_actions:
            print("You loot the enemy!")
            player.gold += enemy.gold
            
            for _loot in enemy.loot:
                player.inventory.append(_loot)
            looting = False
        else:
            print("You leave the enemy alone.")
            looting = False
            
    return None
            
   

                        
                    
                
                
                
                
    
        
         
    
    
    
    
    
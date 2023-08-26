from classes.Enemies import Enemy
import random as rand
from classes.Utility import Utilities as util
from classes.Text import textFunc as text
from termcolor import colored as _color
import classes._Player

def fight(ply: classes._Player.Player):
    
    """Fight a random enemy based on the ply's level.

    Returns:
        None
    """

    random_enemy_type = rand.randint(0, 3) 
    
    if ply.level == 0:
        random_enemy_level = rand.randint(0, 1)
    elif ply.level == 1:
        random_enemy_level = rand.randint(0, 2)
    elif ply.level == 2:
        random_enemy_level = rand.randint(1, 3)
    elif ply.level == 3:
        random_enemy_level = rand.randint(2, 3)
    else:
        pass
    
    enemy = Enemy(random_enemy_type, random_enemy_level)
    
    PLAYER_RAN_AWAY = False
    PLAYER_ATTACKING = True
    ENEMY_ATTACKING = False
    PLAYER_DEAD = False
    ENEMY_DEAD = False
    FIGHTING = True
    
    util.clear_term(0)
    
    message = ""
                             
    while FIGHTING:
        
        text.get_enemy_stats(enemy)

        while ENEMY_ATTACKING and PLAYER_DEAD is False:
            util.clear_term(0)
            damage_taken = enemy.attack - ply.cur_defense
            ply.cur_health -= damage_taken if (ply.cur_health - damage_taken) > 0 else ply.cur_health
            
            message = f"{enemy.name} attacks you for {damage_taken} damage!\nYou have {ply.cur_health} health left!" \
                if (ply.cur_health - damage_taken) > 0 \
                    else ""
            
            if ply.cur_health == 0:
                util.clear_term(0)
                util.scroll_text(_color(f'{enemy.name} defeated you!\n', 'red'), 0.05)
                ENEMY_ATTACKING = False
                PLAYER_DEAD     = True
                break
            else:
                ENEMY_ATTACKING  = False
                PLAYER_ATTACKING = True
                continue
            
        if PLAYER_DEAD:
            FIGHTING = False
            continue

        while (PLAYER_ATTACKING and ENEMY_DEAD is False):
            
            attack_actions = ["attack", "hit", "fight", "kill", "run", "heal"]
            
            util.clear_term(0)
            
            text.get_enemy_stats(enemy) # Print the enemy stats
            util.spacing(1)
            text.get_cur_stats(ply) # Print the ply stats
            util.spacing(1)
            
            print(message, '\n')
            
            action = input("What do you want to do?\n> ")
            action = action.lower()
            
            if action in attack_actions:
                
                if action == 'run':
                    print("You ran away!")
                    FIGHTING = False
                    break
                
                if action == 'heal':
                    player_try_heal, message = ply.use_health_potion() # Try to heal the ply
                    continue
                else:
                    damage = ply.cur_attack 
                    player_damage_done, message = enemy.take_damage(damage) 
                
                    if not player_damage_done:
                        ply.cur_health -= (enemy.attack - ply.cur_defense)
                    else:
                        ply.cur_stamina -= 5
                    
                    if enemy._defeated():
                        
                        coin_string = '\u26C1' * enemy.gold
                        util.clear_term(0)
                        util.scroll_text(_color(f'You defeated {enemy.name}!\n', 'green'), 0.05)
                        util.clear_term(2)
                        util.scroll_text(f"You have gained {enemy.gold} gold and {10 * enemy.level} xp!\n", 0.05)
                        util.scroll_text(_color(coin_string, 'yellow'), 0.05)
                        util.clear_term(2, "You found the following items:\n")
                        
                        ply.gold += enemy.gold
                        ply.xp += 10 * enemy.level if enemy.level > 0 else 1
                        ply.level_check()
                        
                        ENEMY_DEAD = True
                        FIGHTING = False
                        
                        for item in enemy.loot:
                            print(f'\u25BA {item}\n')
                            if item in ply.inventory.keys():
                                ply.inventory[item] += 1
                            else:
                                ply.inventory[item] = 1
                                continue  
                    else:
                        ENEMY_ATTACKING = True
                        PLAYER_ATTACKING = False
                        continue
            else:
                continue            
        
    input("Press enter to continue...")   
    return None

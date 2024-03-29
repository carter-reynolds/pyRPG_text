from classes.Database import Database as db
from classes.Utility import Utilities as util
from dictionaries.enemy_types import types, levels
from dictionaries.enemy_names import bandit_names, goblin_names, undead_names, creature_names
from dictionaries.loot import bandit_loot_dict, goblin_loot_dict, undead_loot_dict, creature_loot_dict
import random as rand
import textwrap


# Most of the functions in this class are used to generate enemies for the player to fight.
# The enemies are generated based on the level of the player, and the type of enemy.
    
class Enemy:
    
    # Init Enemy Generation
    def __init__(self, type_, level):
        self.name = self.assign_random_name(type_) 
        self.type = int(type_)    
        self.level = int(level)   
        
        # These are set by the set_stats method after self.level is set  
        self.gold = 0       
        self.health = 0
        self.max_health = 0     
        self.defense = 0    
        self.attack = 0    
        self.loot = self.assign_random_loot(type_, level)
        
        # Extra stuff not really used yet      
        self.weapon = ''   
        self.effect = []    
        self.location = '' 
        self.defeated = 0   
        
        # Set all stats based on level, also sets gold amount
        self.set_stats(level)  
        
        
        
    def random_level(self):
        return rand.randint(0, 3)
    
    def assign_random_name(self, type_):
        
        random_bandit = rand.randint(0, (len(bandit_names) - 1))
        random_goblin = rand.randint(0, (len(goblin_names) - 1))
        random_undead = rand.randint(0, (len(undead_names) - 1))
        random_creature = rand.randint(0, (len(creature_names) - 1))
        
        if type_ == 0:
            name = bandit_names[random_bandit]
        elif type_ == 1:
            name = goblin_names[random_goblin]
        elif type_ == 2:
            name = undead_names[random_undead]
        elif type_ == 3:
            name = creature_names[random_creature]
        else:
            pass
        
        return name
    
    
    # Assign some random loot to the enemy
    def assign_random_loot(self, _type, level):
        
        loot = []
        
        if level == 0:
            number_of_loot = rand.randint(1, 2)
        if level == 1:
            number_of_loot = rand.randint(2, 3)
        if level == 2:
            number_of_loot = rand.randint(3, 5)
        if level == 3:
            number_of_loot = rand.randint(3, 7)
        
        for i in range(number_of_loot):
            if _type == 0:
                random_loot = bandit_loot_dict[rand.randint(0, 8)]
                loot.append(random_loot)
            elif _type == 1:
                random_loot = goblin_loot_dict[rand.randint(0, 7)]
                loot.append(random_loot)
            elif _type == 2:
                random_loot = undead_loot_dict[rand.randint(0, 11)]
                loot.append(random_loot)
            elif _type == 3:
                random_loot = creature_loot_dict[rand.randint(0, 3)]
                loot.append(random_loot)
            else:
                pass 
        return loot
      
    # Set up all stats based on level
    def set_stats(self, level):
        
        if level == 0:
            self.health = rand.randint(1, 10)
            self.max_health = self.health
            self.defense = rand.randint(1, 10)
            self.attack = rand.randint(1, 10)
            self.gold = rand.randint(1, 10) * 1
        elif level == 1:
            self.health = rand.randint(10, 20)
            self.max_health = self.health
            self.defense = rand.randint(10, 20)
            self.attack = rand.randint(10, 20)
            self.gold = rand.randint(10, 20) * 2
        elif level == 2:
            self.health = rand.randint(20, 30)
            self.max_health = self.health
            self.defense = rand.randint(20, 30)
            self.attack = rand.randint(20, 30)
            self.gold = rand.randint(20, 30) * 3
        elif level == 3:
            self.health = rand.randint(30, 40)
            self.max_health = self.health
            self.defense = rand.randint(30, 40)
            self.attack = rand.randint(30, 40)
            self.gold = rand.randint(30, 40) * 4
        else:
            self.health = None
            self.max_health = None
            self.defense = None
            self.attack = None
            self.gold = None
        
      
    def take_damage(self, damage):
        
        damage = damage - int(self.defense / 1.33)  # Damage is reduced by 1/3 of defense
        
        if damage < 0:
            damage = 0
            message = "The {}'s defense was too strong!".format(self.name)
            return False, message
        else:
            self.health -= damage
            message = f"You deal {damage} damage!\n{self.name} has {self.health} health left!"
            if self.health < 0:
                self.health = 0
                
            return True, message

       
    def _defeated(self):
        if self.health <= 0:
            self.defeated = 1
            return True
        else:
            return False
        
        
   
        
        
    
    
        


                
            
    

     

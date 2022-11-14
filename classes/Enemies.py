from dictionaries.enemy_names import (
    bandit_names, goblin_names, undead_names, creature_names
)

from dictionaries.loot import (
    bandit_loot_dict, goblin_loot_dict, 
    undead_loot_dict, creature_loot_dict
)

from dictionaries.enemy_types import (
    types, levels
)

from classes.Database import Database as db
from classes.Utility import Utilities as util
from classes.Player import Player
import random as rand
import textwrap


# Most of the functions in this class are used to generate enemies for the player to fight.
# The enemies are generated based on the level of the player, and the type of enemy.
    
class Enemy:
    
    
    
    # ENEMY GEN CONSTANTS #
    
    DEFENSE_MODIFIER = 1.33
    
    LEVEL_LOOT_MODIFIERS = {
        0: 1,
        1: 2,
        2: 3,
        3: 4
    }
    
    STATS_MODIFIERS = {
        0: 1,
        1: 1.5,
        2: 2,
        3: 2.5
    }
    
    ENEMY_NAMES = [
        bandit_names,
        goblin_names,
        undead_names,
        creature_names
    ]
    
    LOOT_DICTIONARIES = [
        bandit_loot_dict, 
        goblin_loot_dict, 
        undead_loot_dict, 
        creature_loot_dict
    ]
    
    
    # Init Enemy Generation
    def __init__(self, type_,):
        self.type = type_    
        self.level = self.random_level()
        self.name = self.assign_random_name()    
        
        # These are set by the set_stats method after self.level is set  
        self.gold = 0       
        self.health = 0
        self.max_health = 0     
        self.defense = 0    
        self.attack = 0    
        self.loot = self.assign_random_loot()
        
        # Extra stuff not really used yet      
        self.weapon = ''   
        self.effect = []    
        self.location = '' 
        self.defeated = False  
        
        # Set all stats based on level, also sets gold amount
        self.set_stats() 
        
    
    def random_level(self):
        return rand.randint(0, 3)
    
    def assign_random_name(self):
        return rand.choice(Enemy.ENEMY_NAMES[self.type])
        
    
    # Assign some random loot to the enemy
    def assign_random_loot(self):
        
        level_modifier = Enemy.LEVEL_LOOT_MODIFIERS[self.level]
        
        loot_dict = Enemy.LOOT_DICTIONARIES[self.type]
        
        number_of_loot = (rand.randint(0, 4) * level_modifier)
        
        loot = []

        for i in range(number_of_loot):
            random_item = rand.randint(0, (len(loot_dict) - 1))
            loot.append(loot_dict[random_item])
                
        return loot
    
      
    # Set up all stats based on level
    def set_stats(self):
        
        stat_mod = Enemy.STATS_MODIFIERS[self.level]
        
        self.health += (rand.randint(1, 10) * stat_mod)
        self.attack += (rand.randint(1, 10) * stat_mod)
        self.defense += (rand.randint(1, 10) * stat_mod)
        self.gold += (rand.randint(5, 10) * stat_mod)
        self.max_health = self.health
        
        
        
      
    def take_damage(self, damage):
        
        damage_inflicted = damage - (self.defense / Enemy.DEFENSE_MODIFIER)  # Damage is reduced by 1/3 of defense
        
        if damage_inflicted < 0:
            damage_inflicted = 0
            message = f"{self.name}: defense was too strong!"
            return False, message
        else:
            self.health -= damage
            
            if self.health <= 0:
                self.defeated = True
                self.health = 0 # Just in case it goes below 0
                
            message = f"You deal {damage} damage!\n{self.name} has {self.health} health left!"
              
            return True, message

       
    def _defeated(self):
        return self.defeated
        
        
   
        
        
    
    
        


                
            
    

     

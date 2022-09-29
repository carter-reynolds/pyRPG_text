from dictionaries.loot import(bandit_loot_dict, 
                              goblin_loot_dict, 
                              undead_loot_dict, 
                              creature_loot_dict)

from dictionaries.loot_descriptions import (
    bandit_loot_descriptions, 
    special_bandit_loot_descriptions, 
    goblin_loot_descriptions, 
    special_goblin_loot_descriptions, 
    undead_loot_descriptions,
    special_undead_loot_descriptions,
    creature_loot_descriptions,
    special_creature_loot_descriptions
)

from classes.Player import Player
from classes.Database import Database as db

class Item():
    def __init__(self, item, quantity=0, weight=0):
        self.item = ''
        self.quantity = 0
        self.weight = 0
        
    def increase_quantity(self, amount):
        for i in range(amount):
            self.quantity += 1
    
    def add_to_player_inventory(self, player):
        pass
    
            
    
        
    
                

    
    
    
    
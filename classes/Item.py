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

class Item():
    def __init__(self, name, description, value, weight, _type):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight
        self._type = _type

    # Create a function that creates items based on the dictionaries in loot.py
    def create_item(self, item_dict, desc_dict):
        
        for key, value in zip(item_dict, desc_dict): # pythonically iterate through the dictionaries and zip them together
            print(key, value)
            item_and_descriptions = (key, value)  # Tuple time
            
        # Create an empty list to hold the items
        global_valid_items = []
        # Loop through the dictionary
        for key, value in item_dict.global_valid_items():
            # Create an item object
            item = Item(value, "This is a description", 0, 0, "General")
            # Append the item to the list
            global_valid_items.append(item)
        # Return the list
        return global_valid_items
    
    create_item(bandit_loot_dict, bandit_loot_descriptions)
    
    
    
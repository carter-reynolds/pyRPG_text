import dictionaries.loot as loot
import dictionaries.loot_descriptions as desc

"""
No clue what the functionality of this should be yet

Returns:
a table containing all the loot items in rough order of enemy type
"""

# Define all this ugly mess
bandit_loot_list = list(loot.bandit_loot_dict.values())
goblin_loot_list = list(loot.goblin_loot_dict.values())
undead_loot_list = list(loot.undead_loot_dict.values())
creature_loot_list = list(loot.creature_loot_dict.values())
special_bandit_loot = list(loot.special_bandit_loot.values())
special_goblin_loot = list(loot.special_goblin_loot.values())
special_undead_loot = list(loot.special_undead_loot.values())
special_creature_loot = list(loot.special_creature_loot.values())


def get_full_loot_table():
        
    # Create a list of all the loot lists
    loot_tables = [
        bandit_loot_list, 
        goblin_loot_list, 
        undead_loot_list, 
        creature_loot_list,
        special_bandit_loot,
        special_goblin_loot,
        special_undead_loot,
        special_creature_loot
    ]
    
    # Create an empty list to hold the items from all indiv. loot tables
    full_loot_table = []
    
    for l in loot_tables:
        for i in l:
            full_loot_table.append(i)
    
    full_loot_table = list(dict.fromkeys(full_loot_table))
            
    return full_loot_table

print(get_full_loot_table())
    
    
    
    




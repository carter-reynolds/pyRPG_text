from dictionaries.enemy_types import types, levels
from dictionaries.enemy_names import bandit_names, goblin_names, undead_names, big_spider_names
import random as rand

class Enemy:
    def __init__(self, name, type): # Only name and type will be required for now
        
        self.name = name    # The name of the enemy
        self.type = type    # What type of enemy they are
        self.level = 0
        self.health = 0     # How much health the enemy has
        self.defense = 0    # How well they can defend
        self.attack = 0     # How much damage they would do
        self.loot = []      # Loot they would drop, if any, will likely be randomly assigned
        self.weapon = ''    # Weapon they are using - should contribute to damage
        self.effect = []    # Random effect
        
        
    def rand_enemy_level(): # Returns a random level
        rand_level = rand.randint(0, 3) # 4 Levels
        level_len = len(levels[rand_level]) # Get the length of the list of adjectives describing the level
        rand_adj = rand.randint(0, level_len - 1) # Get a random adjective from the list
        
        return levels[rand_level][rand_adj] # Return the adjective
    
    
    def rand_enemy_type(): # Returns a random enemy type
        rand_type = rand.randint(0, len(types) - 1) # Get a random type
        return types[rand_type] # Return the type
        
    
    def rand_enemy_name(enemy_type): # Returns a random enemy name based on type
        if type == 'Bandit': # If the type is a bandit
            rand_name = rand.randint(0, len(bandit_names) - 1) # Get a random bandit name
            return bandit_names[rand_name] # Return the name
        elif type == 'Goblin':
            rand_name = rand.randint(0, len(goblin_names) - 1)
            return goblin_names[rand_name]
        elif type == 'Undead':
            return 'Undead'
        elif type == 'Big Spider':
            return 'Big Spider'
        
    # Create enemy
    def create_enemy():
        Enemy.type = Enemy.rand_enemy_type()
        Enemy.name = Enemy.rand_enemy_name(Enemy.type)
        Enemy.level = Enemy.rand_enemy_level()

        if Enemy.type == 'Bandit':
            Enemy.health = 10
            Enemy.defense = 2
            Enemy.attack = 5
        elif Enemy.type == 'Goblin':
            Enemy.health = 15
            Enemy.defense = 2
            Enemy.attack = 5
        
        

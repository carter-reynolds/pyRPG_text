from classes.Database import Database as db
from dictionaries.enemy_types import types, levels
from dictionaries.enemy_names import bandit_names, goblin_names, undead_names, creature_names
from dictionaries.loot import bandit_loot_dict, goblin_loot_dict, undead_loot_dict, creature_loot_dict
import random as rand

class Enemy:
    def __init__(self): # Only name and type will be required for now
        self.name = ""    # The name of the enemy
        self.type = ""    # What type of enemy they are
        self.level = ""      # The level of the enemy
        self.health = 0     # How much health the enemy has
        self.defense = 0    # How well they can defend
        self.attack = 0     # How much damage they would do
        self.loot = []      # Loot they would drop, if any, will likely be randomly assigned
        self.weapon = ''    # Weapon they are using - should contribute to damage
        self.effect = []    # Random effect
    
            
    def random_level(self):
        return levels[rand.randint(0, 3)]
    
    def assign_random_loot(self, number_of_loot):
        
        for i in range(number_of_loot):
            if self.type == types[0]:
                random_loot = bandit_loot_dict[rand.randint(0, 8)]
                self.loot.append(random_loot)
            elif self.type == types[1]:
                random_loot = goblin_loot_dict[rand.randint(0, 8)]
                self.loot.append(random_loot)
            elif self.type == types[2]:
                random_loot = undead_loot_dict[rand.randint(0, 12)]
                self.loot.append(random_loot)
            elif self.type == types[3]:
                random_loot = creature_loot_dict[rand.randint(0, 4)]
                self.loot.append(random_loot)
            else:
                pass
        
    # Make a random enemy with type of bandit
    def make_bandit(self):
        
        self.name = bandit_names[rand.randint(0, 9)]
        self.type = types[0]
        self.level = self.random_level()
        
        stats = self.set_stats()
        
        if self.level == levels[0]:
            return self.assign_random_loot(1)
        elif self.level == levels[1]:
            return self.assign_random_loot(2)
        elif self.level == levels[2]:
            return self.assign_random_loot(3)
        elif self.level == levels[3]:
            return self.assign_random_loot(4)
        
        return stats
            
        
        
    # Make a random enemy with type of goblin
    def make_goblin(self):
        self.name = goblin_names[rand.randint(0, 9)]
        self.type = types[1]
        self.level = levels[rand.randint(0, 3)]
        
        random_loot = goblin_loot_dict[rand.randint(0, 8)]
        
        for i in range(0, self.level):
            self.loot.append(random_loot)
            
        self.set_stats()
    
    # Make a random enemy with type of undead
    def make_undead(self):
        self.name = undead_names[rand.randint(0, 2)]
        self.type = types[2]
        self.level = levels[rand.randint(0, 3)]
        
        random_loot = undead_loot_dict[rand.randint(0, 12)]
        
        for i in range(0, self.level):
            self.loot.append(random_loot)
        
        self.set_stats()
    
    # Make a random enemy with type of creature
    def make_creature(self):
        self.name = creature_names[rand.randint(0, 2)]
        self.type = types[3]
        self.level = levels[rand.randint(0, 3)]
        
        random_loot = creature_loot_dict[rand.randint(0, 4)]
        
        for i in range(0, self.level):
            self.loot.append(random_loot)
            
        self.set_stats()
    
    
    
    # set up enemy stats based on type
    def set_stats(self):
        
        # Set up all stats based on level
        if self.level == levels[0]:
            self.health = rand.randint(1, 10)
            self.defense = rand.randint(1, 10)
            self.attack = rand.randint(1, 10)
        elif self.level == levels[1]:
            self.health = rand.randint(10, 20)
            self.defense = rand.randint(10, 20)
            self.attack = rand.randint(10, 20)
        elif self.level == levels[2]:
            self.health = rand.randint(20, 30)
            self.defense = rand.randint(20, 30)
            self.attack = rand.randint(20, 30)
        elif self.level == levels[3]:
            self.health = rand.randint(30, 40)
            self.defense = rand.randint(30, 40)
            self.attack = rand.randint(30, 40)
        else:
            pass
      
    # Display all enemy stats
    def display_stats(self):
        print('Name: {}'.format(self.name))
        print('Type: {}'.format(self.type))
        print('Level: {}'.format(self.level))
        print('Health: {}'.format(self.health))
        print('Defense: {}'.format(self.defense))
        print('Attack: {}'.format(self.attack))
        print('Loot ID: {}'.format(self.loot))
        print('Weapon ID: {}'.format(self.weapon))
        print('Effects: {}'.format(self.effect))
        


                
            
    

     

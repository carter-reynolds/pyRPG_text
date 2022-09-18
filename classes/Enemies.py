from dictionaries.enemy_types import types, levels
from dictionaries.enemy_names import bandit_names, goblin_names, undead_names, creature_names
import random as rand

class Enemy:
    def __init__(self): # Only name and type will be required for now
        self.name = ""    # The name of the enemy
        self.type = 0    # What type of enemy they are
        self.level = 0      # The level of the enemy
        self.health = 0     # How much health the enemy has
        self.defense = 0    # How well they can defend
        self.attack = 0     # How much damage they would do
        self.loot = []      # Loot they would drop, if any, will likely be randomly assigned
        self.weapon = ''    # Weapon they are using - should contribute to damage
        self.effect = []    # Random effect

    # Make a random enemy with type of bandit
    def make_bandit(self):
        self.name = bandit_names[rand.randint(0, 9)]
        self.type = types[0]
        self.level = levels[rand.randint(0, 3)]
        self.set_stats()
    
    # Make a random enemy with type of goblin
    def make_goblin(self):
        self.name = goblin_names[rand.randint(0, 9)]
        self.type = types[1]
        self.level = levels[rand.randint(0, 3)]
        self.set_stats()
    
    # Make a random enemy with type of undead
    def make_undead(self):
        self.name = undead_names[rand.randint(0, 2)]
        self.type = types[2]
        self.level = levels[rand.randint(0, 3)]
        self.set_stats()
    
    # Make a random enemy with type of creature
    def make_creature(self):
        self.name = creature_names[rand.randint(0, 2)]
        self.type = types[3]
        self.level = levels[rand.randint(0, 3)]
        self.set_stats()
    
    # set up enemy stats based on type
    def set_stats(self):
        # Set up all stats based on level
        if self.level == levels[0]:
            self.health = rand.randint(1, 10)
            self.defense = rand.randint(1, 10)
            self.attack = rand.randint(1, 10)
            self.loot = rand.randint(0, 10)
            self.weapon = rand.randint(0, 2) # Weak weapon  
        elif self.level == levels[1]:
            self.health = rand.randint(10, 20)
            self.defense = rand.randint(10, 20)
            self.attack = rand.randint(10, 20)
            self.loot = [rand.randint(10, 20), rand.randint(0, 10)]
            self.weapon = rand.randint(3, 5) # Average weapon
        elif self.level == levels[2]:
            self.health = rand.randint(20, 30)
            self.defense = rand.randint(20, 30)
            self.attack = rand.randint(20, 30)
            self.loot = [
                rand.randint(20, 30),
                rand.randint(10, 20), 
                rand.randint(0, 10)
            ]
            self.weapon = rand.randint(6, 8) # Strong Weapons
        elif self.level == levels[3]:
            self.health = rand.randint(30, 40)
            self.defense = rand.randint(30, 40)
            self.attack = rand.randint(30, 40)
            self.loot = [   # 
                rand.randint(30, 40),
                rand.randint(20, 30),
                rand.randint(10, 20), 
                rand.randint(0, 10)
            ]
            self.weapon = rand.randint(9, 11) # Elite Weapons
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
        


                
            
    

     

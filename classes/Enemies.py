from classes.Database import Database as db
from classes.Utility import Utilities as util
from dictionaries.enemy_types import types, levels
from dictionaries.enemy_names import bandit_names, goblin_names, undead_names, creature_names
from dictionaries.loot import bandit_loot_dict, goblin_loot_dict, undead_loot_dict, creature_loot_dict
import random as rand

class Enemy:
    def __init__(self): # Only name and type will be required for now
        self.name = ""   # The name of the enemy
        self.type = ""    # What type of enemy they are
        self.level = 0      # The level of the enemy
        self.health = 0     # How much health the enemy has
        self.defense = 0    # How well they can defend
        self.attack = 0     # How much damage they would do
        self.loot = []      # Loot they would drop, if any, will likely be randomly assigned
        self.weapon = ''    # Weapon they are using - should contribute to damage
        self.effect = []    # Random effect
        self.location = ''  # Location of the enemy
        
    def random_level(self):
        return rand.randint(0, 3)
    
    
    # Assign some random loot to the enemy
    def assign_random_loot(self, number_of_loot):
        
        loot = []
        
        for i in range(number_of_loot):
            if self.type == types[0]:
                random_loot = bandit_loot_dict[rand.randint(0, 9)]
                loot.append(random_loot)
            elif self.type == types[1]:
                random_loot = goblin_loot_dict[rand.randint(0, 8)]
                loot.append(random_loot)
            elif self.type == types[2]:
                random_loot = undead_loot_dict[rand.randint(0, 12)]
                loot.append(random_loot)
            elif self.type == types[3]:
                random_loot = creature_loot_dict[rand.randint(0, 4)]
                loot.append(random_loot)
            else:
                pass 
        return loot
        
    # Make a random enemy with type of bandit
    def make_bandits(self):
        
        print("Making bandits")
        
        active_bandits = []
            
        for name in bandit_names:
            
            print(name)
        
            self.name = bandit_names[name]  # assign the unique name to the enemy
            self.type = types[0]                # assign the type 'Bandit'
            self.level = self.random_level()    # assign a random level
            
            self.set_stats()  # set all other stats based on the level we just set
            
            
            # set quantity of loot based on level
            if self.level == 0:
                self.loot = self.assign_random_loot(1)
            elif self.level == 1:
                self.loot = self.assign_random_loot(2)
            elif self.level == 2:
                self.loot = self.assign_random_loot(3)
            elif self.level == 3:
                self.loot = self.assign_random_loot(4)
            
            # Finally, add the bandit enemy to the list of active bandits
            active_bandits.append([self.name, self.type, self.level, self.health, self.defense, self.attack, self.loot])
        
        return active_bandits
        
            
        
    # Make a random enemy with type of goblin
    def make_goblins(self):
        
        print("Making goblins")
        
        active_goblins = []
            
        for name in goblin_names:
            
            print(name)
        
            self.name = goblin_names[name]  # assign the unique name to the enemy
            self.type = types[1]                # assign the type 'Goblin'
            self.level = self.random_level()    # assign a random level
            
            self.set_stats()  # set all other stats based on the level we just set
            
            
            # set quantity of loot based on level
            if self.level == 0:
                self.loot = self.assign_random_loot(1)
            elif self.level == 1:
                self.loot = self.assign_random_loot(2)
            elif self.level == 2:
                self.loot = self.assign_random_loot(3)
            elif self.level == 3:
                self.loot = self.assign_random_loot(4)
            
            # Finally, add the bandit enemy to the list of active bandits
            active_goblins.append([self.name, self.type, self.level, self.health, self.defense, self.attack, self.loot])
             
        return active_goblins
        
    # Make a random enemy with type of undead
    def make_undead(self):
        
        print("Making undead")
        
        active_undead = []
            
        for name in undead_names:
            
            print(name)
        
            self.name = undead_names[name]
            self.type = types[2]
            self.level = self.random_level()

            self.set_stats()    # set all other stats based on the level we just set
        
            # set quantity of loot based on level
            if self.level == 0:
                self.loot = self.assign_random_loot(3)
            elif self.level == 1:
                self.loot = self.assign_random_loot(6)
            elif self.level == 2:
                self.loot = self.assign_random_loot(9)
            elif self.level == 3:
                self.loot = self.assign_random_loot(12)
            
            # Finally, add the bandit enemy to the list of active bandits
            active_undead.append([self.name, self.type, self.level, self.health, self.defense, self.attack, self.loot])
        
        return active_undead
        
    # Make a random enemy with type of creature
    def make_creature(self):
        
        print("Making creatures")
        
        active_creatures = []
            
        for name in creature_names:
            
            print(name)
        
            self.name = creature_names[name]
            self.type = types[3]
            self.level = self.random_level()

            self.set_stats()    # set all other stats based on the level we just set
        
            # set quantity of loot based on level
            if self.level == 0:
                self.loot = self.assign_random_loot(1)
            elif self.level == 1:
                self.loot = self.assign_random_loot(2)
            elif self.level == 2:
                self.loot = self.assign_random_loot(3)
            elif self.level == 3:
                self.loot = self.assign_random_loot(4)
            
            # Finally, add the bandit enemy to the list of active bandits
            active_creatures.append([self.name, self.type, self.level, self.health, self.defense, self.attack, self.loot])
        
        return active_creatures
        
    def make_enemies(self):
        self.make_bandits()
        self.make_goblins()
        self.make_undead()
        self.make_creature()

        
      
    # Set up all stats based on level
    def set_stats(self):
        if self.level == 0:
            self.health = rand.randint(1, 10)
            self.defense = rand.randint(1, 10)
            self.attack = rand.randint(1, 10)
        elif self.level == 1:
            self.health = rand.randint(10, 20)
            self.defense = rand.randint(10, 20)
            self.attack = rand.randint(10, 20)
        elif self.level == 2:
            self.health = rand.randint(20, 30)
            self.defense = rand.randint(20, 30)
            self.attack = rand.randint(20, 30)
        elif self.level == 3:
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
        


                
            
    

     

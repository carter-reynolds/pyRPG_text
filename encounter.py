import random as rand
from dictionaries.world import zonemap_dict, zonemap_enemies
import time
import sys
from classes.Player import Player
from classes.Enemies import Enemy
from classes.Database import Database as db
from classes.Utility import Utilities as util
import random as rand

def encounter_check(location=""):
    
    random = rand.randint(0, 100)
        
    if random <= 50:
        print("Enemy encountered!")
        return True
    else:
        return False


import random as rand

def encounter_check(location=""):
    
    random = rand.randint(0, 100)
        
    if random <= 49:
        return True
    else:
        return False


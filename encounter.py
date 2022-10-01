import random as rand

def encounter_check(location=""):
    
    random = rand.randint(0, 100)
        
    if random <= 50:
        print("Enemy encountered!")
        return True
    else:
        return False


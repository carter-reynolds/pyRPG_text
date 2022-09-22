#pyRPG v2
#Carter Reynolds

import menu
import setup
from classes.Database import Database as db
from classes.Enemies import Enemy


def main():
    
    # Modes/Settings
    RUNNING = True
    MENU = True
    PLAY = False

    while RUNNING:
        if MENU:
            MENU = menu.display()
            if not MENU:
                PLAY = True
        elif PLAY:
    
            # check if game.db exists
            if not setup.check_for_db():
                # if not, create it
                setup.create_db()
            else:
                pass
            
            enemy = Enemy()
           
            for bandit in enemy.make_bandits():
                name = bandit[0]
                type = bandit[1]
                level = bandit[2]
                health = bandit[3]
                defense = bandit[4]
                attack = bandit[5]
                weapon = ''
                loot = str(bandit[6])
                effects = ''
                       
                sql = '''INSERT INTO enemies (name, type, level, health, attack, defense, weapon, loot, effects) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                    
                db.execute(sql, (name, type, level, health, attack, defense, weapon, loot, effects))
                
            '''     
            input("halt")
            
            goblins = enemy.make_goblins()
            for goblin in goblins:
                print(goblin)
            input("halt")
            
            undeads = enemy.make_undead()
            for undead in  undeads:
                print(undead)
            input("halt")
            
            creatures = enemy.make_creature()
            for creature in creatures:
                print(creature)
            input("halt")
            '''
            
            setup.game()
        else:
            MENU = True
            
main()



       

      
   
        
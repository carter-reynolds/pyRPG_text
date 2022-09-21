#pyRPG v2
#Carter Reynolds

import menu
import setup
from classes.Database import Database
from classes.Enemies import Enemy
import loot_table
import time

# This function will move in due time. its only here for testing purposes
def add_enemies_to_table():
        enemy = Enemy()
        for i in range(3):
            enemy.make_bandit()  # inserts 3 bandits into enemies table
            time.sleep(2)
            enemy.make_goblin()  # inserts 3 goblins into enemies table
            #enemy.make_creature()
            #enemy.make_undead()
            


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
            # most of this is here for debugging and testing purposes
            Database(filename = 'db/game.db')
            Database.create_game_tables()
            print("Tables created")
            time.sleep(5)
            add_enemies_to_table()
            print("enemies added")
            loot_table.setup_inventory()
            setup.game()
        else:
            MENU = True
            
main()



       

      
   
        
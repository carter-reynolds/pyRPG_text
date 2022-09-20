#pyRPG v2
#Carter Reynolds

import menu
import setup
from classes.Database import Database
from classes.Enemies import Enemy

def add_enemies_to_table():
        enemy = Enemy()
        for i in range(5):
            enemy.make_bandit()
            query = '''
            INSERT INTO enemies (name, type, level, health, defense, attack, loot)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            Database.execute(query, (enemy.name, enemy.type, enemy.level, enemy.health, enemy.defense, enemy.attack, ''))


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
            Database(filename = 'game.db')
            Database.create_game_tables()
            add_enemies_to_table()
            setup.game()
        else:
            MENU = True
            
main()



       

      
   
        
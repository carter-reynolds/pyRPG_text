#pyRPG v2
#Carter Reynolds

import menu
import setup
from classes.Database import Database as db


def main():
    
    # Modes/Settings
    RUNNING = True
    MENU = True
    SETUP = False
    PLAY = False

    while RUNNING:
        if MENU:
            MENU = menu.display()
            if not MENU:
                SETUP = False
                
                while not SETUP:
                    _setup = setup.game()
                    player = _setup[1]
                    _setup = _setup[0]
                    if _setup == True:
                        SETUP = True
                    else:
                        continue            
                PLAY = True       
        if PLAY:    
            # check if game.db exists
            if not setup.check_for_db():
                # if not, create it
                setup.create_db()
            else:          
                setup.main_game_loop(player)  
          
main()



       

      
   
        
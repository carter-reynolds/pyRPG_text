#pyRPG v2
#Carter Reynolds

import menu
import setup

# Main game controller - you run this to start playing

def main():
    
    # Modes/Settings
    RUNNING = True
    MENU = True
    SETUP = False
    PLAY = False

    while RUNNING:
        if MENU:
            MENU = menu.main_menu()
            if not MENU:
                while not SETUP:
                    if not setup.check_for_db():
                        # if not, create it
                        setup.create_db()
                    else:  
                        _setup, player = setup.game() # Returns a tuple: (Boolean, type<Player.object>)
                        
                        if _setup == True:
                            SETUP = True
                        else:
                            continue 
                PLAY = True 
            else:
                continue      
        if PLAY:    
            # check if game.db exists
            if not setup.check_for_db():
                # if not, create it
                setup.create_db()
            else:          
                setup.main_game_loop(player)  

          
main()

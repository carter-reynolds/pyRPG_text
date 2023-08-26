#pyRPG v2
#Carter Reynolds

import menu
import setup
import player_action as action

# Main game controller - you run this to start playing

def main():
    
    # Modes / States
    RUNNING = True
    MENU    = True
    SETUP   = False
    PLAY    = False

    while RUNNING:
        while MENU:
            
            MENU = menu.main_menu()
            
            if not MENU:
                while not SETUP:
                    if setup.check_for_db() is False:
                        setup.create_db()
                    ply = setup.setup_player()
                    SETUP = True
                    PLAY = True 
            else:
                continue      
        if PLAY:    
            # check if game.db exists
            if not setup.check_for_db():
                # if not, create it
                setup.create_db()
            else:          
                while ply.end == False:  
                    action.prompt(ply)
                else:
                    exit() 

          
main()

#pyRPG v2
#Carter Reynolds

import menu
import setup


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
            setup.game()
        else:
            MENU = True
            
main()



       

      
   
        
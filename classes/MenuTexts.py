   
class Menu:
    
    def __init__(self):
        pass
    
    def display(menu):
            
            if menu == 'help':
                
                print('**************************************************')
                print('* pyRPG: A text-based RPG that no one asked for! *')
                print('**************************************************')
                print('*  - Type up, down, left, right to move          *')
                print('*  - Type "look" to inspect something            *')
                print('*  - Type "actions" for other available actions  *')
                print('*  - Don\'t die                                  *')
                print('*                  + Back (1) +                  *')
                print('*                  + Quit (2) +                  *')
                print('**************************************************')      
            
            elif menu == 'main':
                
                print('**************************************************')
                print('*                  ~  pyRPG  ~                   *')
                print('*     A text-based RPG that no one asked for!    *')
                print('**************************************************')
                print('*                                                *')
                print('*     Play (1) - Start a new game                *')
                print('*     Help (2) - View the help menu              *')
                print('*     Quit (3) - Quit the game                   *')
                print('*     Debug (4) - Run debug command              *')
                print('*                                                *')
                print('*                   Version: 0                   *')
                print('**************************************************')
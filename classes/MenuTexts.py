
class Menu:
    
    def __init__(self):
        pass
    
    @staticmethod
    def display(menu, df=None):
            
            if menu == 'help':
                
                print('**************************************************')
                print('* pyRPG: A text-based RPG that no one asked for! *')
                print('**************************************************')
                print('*  - Type up, down, left, right to move          *')
                print('*  - Type "look" to inspect something            *')
                print('*  - Type "actions" for other available actions  *')
                print('*  - Don\'t die                                  *')
                print('*                  + Back (1) +                  *')
                print('*                                                *')
                print('**************************************************')      
            
            elif menu == 'main':
                
                print('**************************************************')
                print('*                  ~  pyRPG  ~                   *')
                print('*     A text-based RPG that no one asked for!    *')
                print('**************************************************')
                print('*                                                *')
                print('*     (1) - Start a new game                     *')
                print('*     (2) - View the help menu                   *')
                print('*     (3) - Quit the game                        *')
                print('*                                                *')
                print('*                                                *')
                print('*                   Version: 0                   *')
                print('**************************************************')

            elif menu == 'pause':
                    
                print('**************************************************')
                print('*                  ~  pyRPG  ~                   *')
                print('*     A text-based RPG that no one asked for!    *')
                print('**************************************************')
                print('*                                                *')
                print('*     (1) - View your inventory                  *')
                print('*     (2) - Save the game                        *')
                print('*     (3) - Return to the game                   *')
                print('*                                                *')
                print('*                   Version: 0                   *')
                print('**************************************************')
                
            elif (menu == 'inventory'):
                
                print("Items  |  Quantity")
                
                for item in df:
                    if df[item] > 0: # Only display items that have a quantity greater than 0
                        print(f"{item}    x{df[item]}")
                    else:
                        pass
                    
                print('Enter (1) to return to the game')

            
                
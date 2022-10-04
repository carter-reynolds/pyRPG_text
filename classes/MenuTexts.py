from termcolor import colored as _color

# This class is used to store all the text that is displayed in the menu
# This class will eventually be used to automatically render windows based on the text and the size of the window

class Menu:
    
    def __init__(self):
        pass
    
    @staticmethod
    def display(menu, df=None):
            
            if menu == 'help':
                
                print('**************************************************')
                print('* pyRPG: A text-based RPG that no one asked for! *')
                print('**************************************************')
                print('*  help text here                                *')
                print('*                                                *')
                print('*                                                *')
                print('*                                                *')
                print('*                                                *')
                print('*                                                *')
                print('*                                                *')
                print('*                  + Back (1) +                  *')
                print('**************************************************')      
            
            elif menu == 'main':
                
                print('**************************************************')
                print('*                  ~  pyRPG  ~                   *')
                print('*     A text-based RPG that no one asked for!    *')
                print('**************************************************')
                print('*                                                *')
                print('*     (1) - Start a new game                     *')
                print('*     (2) - Load saved character                 *')
                print('*     (3) - View the Help Menu                   *')
                print('*                                                *')
                print('*     (4) - Quit the game                        *')
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
                print('*                                                *')
                print('**************************************************')
                
            elif (menu == 'inventory'):
                
                print(f"{_color('Items', 'red', attrs=['bold'])}  |  {_color('Quantity', 'yellow', attrs=['bold'])}")
                
                
                for item in df: # This is no longer actually a dataframe, but a dictionary :shrug:
                    
                    quantity = df[item] #
                    
                    if quantity > 0: # Only display items that have a quantity greater than 0
                        print(f"{_color(item, 'red')} {_color('x' + str(quantity), 'yellow')}")
                    else:
                        pass
                    
                print('Enter (1) to return to the game')

            
                
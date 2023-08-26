from termcolor import colored as _color
from tabulate import tabulate

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
                
                
                ''' new inventory display:
                ╭──────────────────────┬────────────╮
                │ Item                 │   Quantity │
                ├──────────────────────┼────────────┤
                │ Health Potion        │          2 │
                ├──────────────────────┼────────────┤
                │ Fingerless Gloves    │          1 │
                ├──────────────────────┼────────────┤
                │ Leather Boots        │          1 │
                ╰──────────────────────┴────────────╯
                orders from highest to lowest quantity 
                and auto hides anything 0 quantity
                '''  

                items = list(df.keys())
                quantities = list(df.values())
                items_and_quantities = zip(items, quantities)
                items_and_quantities = sorted(items_and_quantities, key=lambda x: x[1], reverse=True)
                pretty_inv = tabulate(items_and_quantities, headers=['Item', 'Quantity'], tablefmt='rounded_grid', showindex=False)  
                print(pretty_inv)
                print('Enter to return to the game')

            
                
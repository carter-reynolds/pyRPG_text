from termcolor import colored as _color
from tabulate import tabulate
import pandas as pd

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
                items = []
                quantities = []
                
                for key in df.keys():
                    items.append(key)
                    
                for value in df.values():
                    quantities.append(value)
                    
                df_ = pd.DataFrame({'Item': items, 'Quantity': quantities})
                df_.sort_values(by=['Quantity'], inplace=True, ascending=False)
                df_.drop(df_[df_['Quantity'] == 0].index, inplace=True)
                
                pretty_inv = tabulate(df_, headers='keys', tablefmt='rounded_grid', showindex=False)
                        
                print(pretty_inv)
                    
                print('Enter to return to the game')

            
                
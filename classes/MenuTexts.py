from termcolor import colored as _color
from textbox import make_text_box
from textwrap import dedent

# This class is used to store all the text that is displayed in the menu
# This class will eventually be used to automatically render windows based on the text and the size of the window

class Menu:
    
    def __init__(self):
        pass
    
    @staticmethod
    def display(menu, inventory=None):
            
            if menu == 'help':
                make_text_box(title="", text="This is the help menu. You can use the arrow keys to navigate the menu." 
                                             "Press enter to select an option. Press escape to exit the menu.", 
                                             choices=['1. Back'])            
            elif menu == 'main':
                
                menu_text = "Select an option when you are ready to proceedccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
                make_text_box(title="Menu Menu:", text=menu_text, choices=['1. New Game', '2. Help', '3. Exit'])

            elif menu == 'pause':
                make_text_box(title="", text="Pause Menu", choices=['1. View Inventory', '2. Save Game', '3. Return'])
                
            elif (menu == 'inventory'):
                print(f"{_color('Items', 'red', attrs=['bold'])}  |  {_color('Quantity', 'yellow', attrs=['bold'])}")
                
                for item in inventory: 
                    
                    quantity = inventory[item] 
                    
                    if quantity > 0: 
                        print(f"{_color(item, 'red')} {_color('x' + str(quantity), 'yellow')}")
                    else:
                        pass
                    
                print('Enter (1) to return to the game')

            
                
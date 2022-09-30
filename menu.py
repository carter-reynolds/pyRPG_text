from classes.MenuTexts import Menu
from classes.Utility import Utilities as util
from classes.Enemies import Enemy
import setup
import sys



def display(): # Load title screen
    
    util.clear_term(0)
    Menu.display(menu='main')
    
    MENU = True
    
    while MENU:
        
        option = input('> ')
        
        if option == '1':
            break
        elif option == '2':
            help_menu()
        elif option == '3':
            return sys.exit()
        elif option == '4': # Debug
            continue
        else:
            continue
        
    return False
        
def help_menu():
    util.clear_term(0)   
    Menu.display(menu='help')
    
    while True:
        option = input('> ')
        if option == '1':
            display()
        elif option == '2':
            return sys.exit()
            

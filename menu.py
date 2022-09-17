from classes.Text import textFunc as text
from classes.Utility import Utilities as util
import setup
import sys

def title_screen(): # Load title screen
    util.clear_term(0)
    text.display_menu(menu='main')
    title_screen_selections()
        
def help_menu():
    util.clear_term(0)   
    text.display_menu(menu='help')
    title_screen_selections()
        
def title_screen_selections(): 
    while True:
        option = input('> ')
        if option == '1':
            setup.setup_game()
        elif option == '2':
            help_menu()
        elif option == '3':
            pass
        elif option == '4':
            sys.exit()   
        else:
            continue
from classes.MenuTexts import Menu as menuText
from classes.Utility import Utilities as util
from classes.Enemies import Enemy
from classes._Player import Player
import sys

# Functions for interacting with menus

def main_menu(): # Load title screen
    
    MAIN = True
    
    while MAIN:
        
        util.clear_term(0)
        
        menuText.display(menu='main', df=None)
        
        option = input('> ')
    
        try:
            option_ = int(option)
            if option_ == 1:
                return False
            elif option_ == 2:
                help_menu()
            elif option_ == 3:
                return sys.exit()
            else:
                continue
        except ValueError as error:
            util.clear_term(0)
            print("error: enter in a number")
            util.clear_term(2)
            continue
               
    return False

        
def help_menu():
    
    HELP = True
    
    while HELP:
        
        util.clear_term(0)
        
        menuText.display(menu='help')
        
        option = input('> ')
        
        if option == '1':
            break 
        else:
            continue
    
    return False

def actions_menu(action_list):
    ACTIONS = True
    
    util.clear_term()
    
    while ACTIONS:
        
        for action in action_list:
            print(action)
            
        option = input('Press enter to continue')
        
        break
    
    return
    
        
    
        
def pause_menu(player: Player):
    
    PAUSE = True
    INVENTORY = False
    
    util.clear_term(0)
    menuText.display(menu='pause')
    
    while PAUSE:
        
        option = input('> ')
        
        if option == '1':
            
            INVENTORY = True
            
            inventory = player.inventory
            
            util.clear_term(0)
            menuText.display(menu='inventory', df=inventory)
            
            while INVENTORY:
                
                option = input('> ')
                
                if option == '1':
                    INVENTORY = False
                else:
                    continue
            break
        
        elif option == '2':
            break
        elif option == '3':
            break
        else:
            continue
        
    return False



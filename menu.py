from classes.MenuTexts import Menu as menuText
from classes.Utility import Utilities as util
from classes.Enemies import Enemy
from classes.Player import Player
import sys

# Functions for interacting with menus

def main_menu(): # Load title screen
    
    while True:
        
        util.clear_term(0)
        
        menuText.display(menu='main')
        
        try:
            
            option = int(input('> '))
            
            if option == 1: 
                return False
            
            elif option == 2:               
                help_menu()
                
            elif option == 3:             
                return sys.exit()
            
            else:           
                continue
            
        except ValueError:
            util.clear_term(2, message="error: enter in a number")
            continue

        
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
    
    util.clear_term()
    
    while True:
        
        for action in action_list:
            print(action)
            
        input('Press enter to continue')
        
        return False

    
        
    
        
def pause_menu(player):
    
    PAUSE = True
    INVENTORY = False
    
    util.clear_term(0)
    menuText.display(menu='pause')
    
    while PAUSE:
        
        option = input('> ')
        
        if option == '1':
            
            inventory = player.inventory
            
            util.clear_term(0)
            menuText.display(menu='inventory', inventory=inventory)
            
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



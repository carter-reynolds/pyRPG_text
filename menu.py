from classes.MenuTexts import Menu
from classes.Utility import Utilities as util
from classes.Enemies import Enemy
import setup
import sys
from termcolor import colored



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
        
        # Lazy debug mode, just write the shit into the menu lol
        elif option == '4':
            # Make 5 random bandit enemy objects
            for i in range(0, 5):
                enemy = Enemy()
                enemy.make_bandit()
                
                # Print out the enemy's stats as an f string
                print(f'Name: {colored(enemy.name, "red")}\n' 
                      f'Type: {enemy.type}\n'
                      f'Level: {enemy.level}\n'
                      f'Health: {enemy.health}\n'
                      f'Defense: {enemy.defense}\n'
                      f'Attack: {enemy.attack}\n'
                      f'Loot: {enemy.loot}\n')
                """ 
                TODO: eventually, since there will be probably be not
                    a lot of enemies in total to beat the game, I will need
                    to convert most of the dictionaries into lists and
                    drop some loot items from the list when they are assigned.
                 
                """
            #continue
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
            

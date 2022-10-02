import time
import os
import sys
import random as rand
import pandas as pd

class Utilities:
    
    @staticmethod
    def clear_term(delay=0, message='', func=None):
        
        time.sleep(delay)
        
        OS = os.name
        
        if OS == 'nt':
            os.system('cls')   
        else:
            os.system('clear')
            
        if message != '':
            Utilities.scroll_text(message, 0.05)
        else:
            pass
        
        if func == None:
            pass
        else:
            return func
            
       
    
    @staticmethod        
    def spacing(amount):
        for x in range(amount):
            print('')
    
    
    @staticmethod        
    def scroll_text(text, speed, delay=0):
        time.sleep(delay)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
    
    
    @staticmethod        
    def excluded_random(r1, r2, exclude_list):
        print("Excluded random called: ", r1, r2, exclude_list)
        return rand.choice([i for i in range(r1,r2) if i not in [exclude_list]])
    
    
    @staticmethod
    def timer():
        cur = time.time()
        return cur

    
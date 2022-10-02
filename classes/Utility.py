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
    
    
    @staticmethod
    def build_dataframe(_list=[], mode=0):
        """Builds a dataframe from a list. Supports two modes:

        Args:
            _list (list): A list to be converted to a dataframe
            mode (int, optional): Mode 0 - just converts a list to a dataframe
            mode (int, optional): Mode 1 - converts a list and totals the values to a new column

        Returns:
            df_0: Dataframe of list items with index
            df_1: Dataframe of list items deduped and totaled
        """        
        if mode == 0:
            df_0 = pd.DataFrame(_list)
            return df_0
        elif mode == 1:
            # create a dataframe from the list without index
            
            df_1 = pd.DataFrame({'Item':_list})
            df_1 = df_1.groupby(df_1.columns.tolist(), as_index=True).size()
            print(df_1)
            return df_1
        else:
            pass
        
    
import platform
import time
import os
import sys
import random as rand
import pandas as pd

class Utilities:
    
    @staticmethod
    def clear_term(delay):
        system_type = platform.system()
        time.sleep(delay)
        
        # TODO - there's a one-liner for this but :shrug:
        if system_type == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    
    @staticmethod        
    def spacing(amount):
        for x in range(amount):
            print('')
    
    
    @staticmethod        
    def scroll_text(text, speed):
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
            
            df_1 = pd.DataFrame(_list, columns=['Item'])
            df_1 = df_1.groupby(df_1.columns.tolist(), as_index=False).size()
            return df_1
        else:
            pass
import platform
import time
import os
import sys
import random as rand

class Utilities:
    
    def clear_term(delay):
        system_type = platform.system()
        time.sleep(delay)
        
        # TODO - there's a one-liner for this but :shrug:
        if system_type == "Windows":
            os.system('cls')
        else:
            os.system('clear')
            
    def spacing(amount):
        for x in range(amount):
            print('')
            
    def scroll_text(text, speed):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
            
    def excluded_random(r1, r2, exclude_list):
        print("Excluded random called: ", r1, r2, exclude_list)
        return rand.choice([i for i in range(r1,r2) if i not in [exclude_list]])
    
    def timer():
        cur = time.time()
        return cur

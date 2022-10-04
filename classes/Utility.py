import time
import os
import sys
import random as rand

# Random utility functions for the game to use that didn't need to clog up other files

class Utilities:
    
    @staticmethod
    def clear_term(delay=0, message='', func=None):
        """Clears the terminal screen

        Args:
            delay (int, optional): Delay in seconds. Defaults to 0.
            message (str, optional): Message to display. Defaults to ''.
            func (function, optional): Function to call. Defaults to None.

        Returns:
            None | func(): Calls function if specified
        """
        
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
    def spacing(amount=1):
        """Adds spacing between lines of text

        Args:
            amount (int, optional): The number of lines to skip. Defaults to 1.
        """
        for x in range(amount):
            print('')
    
    
    @staticmethod        
    def scroll_text(text, speed, delay=0):
        """Scrolls text across the screen

        Args:
            text (str): The text to scroll
            speed (float|int): The speed at which the text scrolls
            delay (int, optional): The delay, in seconds, before the text scrolls. Defaults to 0.
        """
        time.sleep(delay)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
 
    
    @staticmethod
    def timer():
        """Returns the current time in seconds

        Returns:
            cur (float): The current time in seconds
        """
        cur = time.time()
        return cur

    
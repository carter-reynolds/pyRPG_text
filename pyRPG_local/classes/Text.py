from dictionaries.world import zonemap_dict, solved_places
from classes.Utility import Utilities as util

class textFunc:
            
    def print_location(player): 
    
        zone_name = zonemap_dict[player.location]['ZONENAME']
        zone_description = zonemap_dict[player.location]['DESCRIPTION']
        
        arrival_str = (zone_name + ' - ' + zone_description)

        print(arrival_str)
        util.spacing(2)
    
    def welcome_speech(): 
           
        welcome_speeches = [    
            "Welcome to the world!"
        ]
        
        for speech in welcome_speeches:
            util.scroll_text(speech, 0.05)
            
    def print_player_info(player):
        print("Name:\t", player.name)
        print("Role:\t", player.role)
        print("Health:\t", player.cur_health)
        print("Mana:\t", player.cur_mana)
        print("Stamina:", player.cur_stamina)
        print("Effects:", player.effects)
        print("Items:\t", player.items)
        print("Carry Weight:", player.cur_carry_weight)
        util.spacing(1)
        print("Current Location: ", player.location)
        util.spacing(2)
        
    def display_menu(menu):
        
        if menu == 'help':
            
            print('**************************************************')
            print('* pyRPG: A text-based RPG that no one asked for! *')
            print('**************************************************')
            print('*  - Type up, down, left, right to move          *')
            print('*  - Type "look" to inspect something            *')
            print('*  - Type "actions" for other available actions  *')
            print('*  - Don\'t die                                  *')
            print('*                  + Play (1) +                  *')
            print('*                  + Quit (3) +                  *')
            print('**************************************************')      
        
        elif menu == 'main':
            
            print('**************************************************')
            print('*                  ~  pyRPG  ~                   *')
            print('*     A text-based RPG that no one asked for!    *')
            print('**************************************************')
            print('*                                                *')
            print('*     Play (1) - Start a new game                *')
            print('*     Help (2) - View the help menu              *')
            print('*     Quit (3) - Quit the game                   *')
            print('*                                                *')
            print('*                   Version: 0                   *')
            print('**************************************************') 
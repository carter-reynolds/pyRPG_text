from distutils.fancy_getopt import wrap_text
from dictionaries.world import zonemap_dict, solved_places
from classes.Utility import Utilities as util
import textwrap


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
        
        player_stats_text = f"""
        Name: {player.name}
        Role: {player.role}
        Health: {player.cur_health}
        Mana: {player.cur_mana}
        Stamina: {player.cur_stamina}
        Effect: {player.effects}
        Inventory: {player.inventory}
        Carry Weight: {player.cur_carry_weight}

        Current Location: {player.location}
        
        """
        fixed_player_text = textwrap.dedent(player_stats_text)
        print(fixed_player_text)
        
         
     
from dictionaries.world import zonemap_dict
from dictionaries.enemy_types import types, levels
from classes.Utility import Utilities as util
from textwrap import dedent
from termcolor import colored as _color

# Pretty much anything that displays text to the player often is in this class

class textFunc:
    
    
    @staticmethod
    # TODO: MOVE THIS TO THE PLAYER CLASS        
    def print_location(player): 
    
        zone_name = zonemap_dict[player.location]['ZONENAME']
        zone_description = zonemap_dict[player.location]['DESCRIPTION']
        
        arrival_str = (zone_name + ' - ' + zone_description)

        print(arrival_str)
        util.spacing(2)

    
    @staticmethod
    def welcome_speech(): 
           
        welcome_speeches = [    
            "Welcome to the world!"
        ]
        
        for speech in welcome_speeches:
            util.scroll_text(speech, 0.05)
            
    
    @staticmethod
    # TODO: DELETE THIS AND/OR MOVE INTO PLAYER CLASS           
    def print_player_info(player):
        
        player_stats_text = f"""
        Name: {player.name}
        Role: {player.role}
        Health: {player.cur_health}
        Mana: {player.cur_mana}
        Attack: {player.cur_attack}
        Stamina: {player.cur_stamina}
        Effect: {player.effects}
        Inventory: {player.inventory}
        Carry Weight: {player.cur_carry_weight}

        Current Location: {zonemap_dict[player.location]['ZONENAME']} - {player.location}
        
        """
        fixed_player_text = dedent(player_stats_text)
        print(_color(fixed_player_text, 'green'))
        
    
    @staticmethod
    # TODO: MOVE THIS TO A NEW 'GAME' CLASS
    def print_bar(curr, max, level, color='white'):

            # all bars are 20 chars long, scale the given values
            bar_width = 20
            scale = bar_width / max
            progress_earned = int(curr * scale)
            progress_remaining = int((max - curr) * scale)

            # account for rounding
            if (progress_earned + progress_remaining < bar_width):
                progress_remaining += 1

            # build strings for the bar itself
            earned_bar = progress_earned * '\u2588'
            remaining_bar = progress_remaining * '\u2591'
            
            bar = _color(earned_bar + remaining_bar + ' ' + str(curr) + '/' + str(max) + '\n', color)
            
            return bar

    
    @staticmethod
    # TODO: MOVE THIS TO THE PLAYER CLASS
    def get_cur_stats(player):
        
        health = player.cur_health
        max_health = player.max_health
        stamina = player.cur_stamina
        max_stamina = player.max_stamina
        mana = player.cur_mana
        max_mana = player.max_mana
        level = player.level
        gold = player.gold
        name = player.name
        location = player.location
        role = player.role
        
        health_bar = textFunc.print_bar(health, max_health, None, 'red')
        stamina_bar = textFunc.print_bar(stamina, max_stamina, None, 'green')
        mana_bar = textFunc.print_bar(mana, max_mana, None, 'blue')
        
        player_text_header = f"❱❱❱ {name} | {role} | {zonemap_dict[location]['ZONENAME']} | Level: {str(level)} ❰❰❰"
        
        colored_header = _color(player_text_header.upper(), 'red', attrs=['bold'])
        colored_gold = _color('\u26C1 '+ str(gold), 'yellow')

        print(f"{colored_header}" + "\n\n" + 
              _color(" HEALTH  ", 'white', 'on_red', attrs=['bold']) + f"{health_bar}" + "\n" + 
              _color(" STAMINA ", 'white', 'on_green', attrs=['bold']) + f"{stamina_bar}" + "\n" + 
              _color(" MAGIC   ", 'white', 'on_blue', attrs=['bold']) + f"{mana_bar}" + "\n" + 
              f"{colored_gold}" + "\n")
    
    
    @staticmethod
    # TODO: MOVE THIS TO THE ENEMY CLASS
    def get_enemy_stats(enemy):
            
            health = enemy.health
            max_health = enemy.max_health
            enemy_type = enemy.type
            level = enemy.level
            
            health_bar = textFunc.print_bar(health, max_health, level, 'red')
            
            enemy_text_header = f"* {enemy.name} | {types[enemy_type]} | Level: {str(level)} *"
            
            colored_header = _color(enemy_text_header.upper(), 'red', attrs=['bold'])
            
            print(f"{colored_header}" + "\n\n" + 
                  f"{health_bar}" + "\n")
            
    # TODO: MAKE SYSTEM FUNCTION TO COLOR CERTAIN TEXT SUCH AS ERRORS VS NORMAL TEXT
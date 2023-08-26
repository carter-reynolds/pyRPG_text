from classes.Database import Database as db
from classes._Player import Player as player
from classes.Enemies import Enemy as enemy
import time

"""
Start testing loading and saving data
Currently not being used
"""

def load_player_data():
    player_data = db.get_all_rows('player')
    # player_data = [(1, 'Carter', '1', 'Warrior', '100', 'B2', 120, 10, 15, 'Dulled Short Sword', '', '', '')]
    
    timer_start = time.time()
    
    player.name = player_data[0][1]
    player.level = player_data[0][2]
    player.role = player_data[0][3]
    player.gold = player_data[0][4]
    player.location = player_data[0][5]
    player.cur_health = player_data[0][6]
    player.cur_defense = player_data[0][7]
    player.cur_attack = player_data[0][8]
    player.weapon = player_data[0][9]
    player.effects = player_data[0][10]
    
    print(player.name, player.level, player.role, player.gold, player.location, player.cur_health, player.cur_defense, player.cur_attack, player.weapon, player.effects)
        
    timer_final = time.time() - timer_start
    
    print(f"Finished loading player data after {timer_final} seconds.")

    
def load_enemy_data():
    enemy_data = db.get_all_rows('enemies')
    
    timer_start = time.time()
    
    for i in range(len(enemy_data)):
        enemy.name = enemy_data[i][1]
        enemy.type = enemy_data[i][2]
        enemy.level = enemy_data[i][3]
        enemy.health = enemy_data[i][4]
        enemy.defense = enemy_data[i][5]
        enemy.attack = enemy_data[i][6]
        enemy.loot = enemy_data[i][7]
        enemy.weapon = enemy_data[i][8]
    
    timer_final = time.time() - timer_start
    
    print(f"Finished loading enemy data after {timer_final} seconds.")
    
    
def save_player_data():
    timer_start = time.time()
    
    sql = '''
        UPDATE player
        SET name = ?, role = ?, level = ?, gold = ?, 
            location = ?, health = ?, defense = ?, attack = ?, 
            weapon = ?, shield = ?, armor = ?, effect = ?
        WHERE id = 1;
    '''
    db.execute(sql, (player.name, player.role, player.level, player.gold, player.location, player.cur_health, player.cur_defense, player.cur_attack, player.weapon, '', '', ''))
    
    timer_final = time.time() - timer_start
    
    print(f"Finished saving player data after {timer_final} seconds.")

    
def save_enemy_data():
    timer_start = time.time()
    
    # we update by name because names are unique and removed from the name table
    # when one is assigned to an enemy
    sql = f'''
        UPDATE enemies
        SET name = ?, type = ?, level = ?, health = ?, 
            defense = ?, attack = ?, loot = ?, weapon = ?
        WHERE name = {enemy.name};
    '''
    db.execute(sql, (enemy.name, enemy.type, enemy.level, enemy.health, enemy.defense, enemy.attack, enemy.loot, enemy.weapon))
    
    timer_final = time.time() - timer_start
    
    print(f"Finished saving enemy data after {timer_final} seconds.")
    
    
def load_game_data():
    load_player_data()
    load_enemy_data()
    
def save_game_data():
    save_player_data()
    save_enemy_data()
    
load_player_data()

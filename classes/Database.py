import sqlite3
from classes.Utility import Utilities as util

# Really poorly coded database class, but barely being used, so it's okay for now until I can get around to it

class Database:
    def __init__(self, filename="game.db", **kwargs):
        self.filename = kwargs.get(filename)
        
    
    @staticmethod 
    def create_game_tables():
        
        timer_start = util.timer()
    
        db = sqlite3.connect('pyRPG_text/data/game.db')
        
        with open('pyRPG_text/data/initial_table_setup.sql', 'r') as f:
            sql = f.read()
            db.executescript(sql)
            db.commit()
            db.close()
        f.close()
        
        timer_final = util.timer() - timer_start
        
        print("Finished creating tables. Took {} seconds.".format(timer_final))
    
    @staticmethod      
    def execute(sql, params = ()):
        db = sqlite3.connect('pyRPG_text/data/game.db')
        cursor = db.cursor()
        cursor.execute(sql, params)
        db.commit()
        db.close()
    
    @staticmethod 
    # create function to get rows from table
    def get_all_rows(table):
        db = sqlite3.connect('pyRPG_text/data/game.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {}".format(table))
        rows = cursor.fetchall()
        db.close()
        return rows
    
    @staticmethod 
    def add_item(item, quantity):
        db = sqlite3.connect('pyRPG_text/data/game.db')
        cursor = db.cursor()
        cursor.execute( """
                        INSERT INTO inventory (name, quantity) 
                        VALUES (?, ?)
                            WHERE name = (?)""", (item, quantity, item))
        db.commit()
        db.close()
    
    @staticmethod     
    def get_random_level_enemy(type, level):
        db = sqlite3.connect('pyRPG_text/data/game.db')
        cursor = db.cursor()
        cursor.execute( """
                    SELECT * FROM enemies
                        WHERE type = ?
                            AND level = ?
                            AND is_defeated = 0
                        LIMIT 1
                        """, (type, level))
                       
        

   
    
   
        
        
    

   
import sqlite3

class Database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('game.db')
        pass
    
    def create_game_tables():
        sql = '''
            CREATE TABLE IF NOT EXISTS enemies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                type TEXT,
                level TEXT,
                loot TEXT,
                health INTEGER,
                defense INTEGER,
                attack INTEGER,
                weapon TEXT,
                effect TEXT);
                
            CREATE TABLE IF NOT EXISTS player (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                level TEXT,
                role TEXT,
                gold TEXT,
                location TEXT,
                health INTEGER,
                defense INTEGER,
                attack INTEGER,
                weapon TEXT,
                shield TEXT,
                armor TEXT,
                effect TEXT);
                
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                type TEXT,
                description TEXT,
                value INTEGER,
                weight INTEGER);
        '''
        
        db = sqlite3.connect('game.db')
        db.executescript(sql)
        db.commit()
        db.close()
        
    def execute(sql, params = ()):
        db = sqlite3.connect('game.db')
        cursor = db.cursor()
        cursor.execute(sql, params)
        db.commit()
        db.close()
        
   
    
   
        
        
    

   
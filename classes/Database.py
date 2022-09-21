from fileinput import filename
import sqlite3

class Database:
    def __init__(self, filename,**kwargs):
        self.filename = kwargs.get(filename)
        
    
    def create_game_tables():
    
        db = sqlite3.connect('db/game.db')
        
        with open('db/query/initial_table_setup.sql', 'r') as f:
            sql = f.read()
            db.executescript(sql)
            db.commit()
            db.close()
        f.close()
          
    def execute(sql, params = ()):
        print("connecting")
        db = sqlite3.connect('db/game.db')
        print("connected")
        cursor = db.cursor()
        cursor.execute(sql, params)
        db.commit()
        print(sql)
        db.close()
    
    # create function to get rows from table
    def get_all_rows(table):
        db = sqlite3.connect('db/game.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM {}".format(table))
        rows = cursor.fetchall()
        db.close()
        return rows
   
    
   
        
        
    

   
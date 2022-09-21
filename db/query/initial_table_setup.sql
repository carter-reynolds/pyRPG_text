-- SQLite
-- Initial SQL queries to set up the tables the game needs
CREATE TABLE IF NOT EXISTS enemies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, type TEXT, level INTEGER,
        loot TEXT, health INTEGER, defense INTEGER,
        attack INTEGER, weapon TEXT, effect TEXT);

CREATE TABLE IF NOT EXISTS player (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, level INTEGER, role TEXT,
        gold TEXT, location TEXT, health INTEGER,
        defense INTEGER, attack INTEGER, weapon TEXT,
        shield TEXT, armor TEXT, effect TEXT);
                
CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, type TEXT, description TEXT,
        value INTEGER, weight INTEGER);
        
CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, quantity INTEGER);
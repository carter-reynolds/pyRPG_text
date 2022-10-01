from classes.Database import Database as db
    
class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.end = False
        
        self.gold = 100
        self.weapon = ''
        self.location = 'B2'
        
        self.level = 0
        self.xp = 0
        
        self.inventory = ['Test', 'Test', 'Test', 'Test 2']
        
        self.base_health = 0
        self.max_health = 0
        self.cur_health = self.max_health       
        
        self.base_mana = 0
        self.max_mana = 0
        self.cur_mana = self.max_mana
        
        self.base_stamina = 0
        self.max_stamina = 0
        self.cur_stamina = self.max_stamina
        
        self.base_defense = 0
        self.max_defense = 0
        self.cur_defense = self.max_defense
        
        self.base_attack = 0
        self.max_attack = 0
        self.cur_attack = self.max_attack
        
        self.max_carry_weight = 0 
        self.cur_carry_weight = self.max_carry_weight
        
        self.effects = []
        
    def write_player_data(self):
        sql = '''
            INSERT INTO player (name, role, level, gold, location, health, defense, attack, weapon, shield, armor, effects)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
        db.execute(sql, (self.name, self.role, self.level, self.gold, self.location, self.cur_health, self.cur_defense, self.cur_attack, self.weapon, '', '', ''))
        
    def set_player_stats(self, role):
        if role == 'Warrior':
            self.max_health = 120
            self.max_mana = 40
            self.max_stamina = 100
            self.max_defense = 10
            self.max_attack = 15
            self.max_carry_weight = 100
            self.cur_health = self.max_health
            self.cur_mana = self.max_mana
            self.cur_stamina = self.max_stamina
            self.cur_defense = self.max_defense
            self.cur_attack = self.max_attack
            self.cur_carry_weight = self.max_carry_weight
            self.weapon = 'Dulled Short Sword'     
        elif role == 'Mage':
            self.max_health = 85
            self.max_mana = 100
            self.max_stamina = 75
            self.max_defense = 10
            self.max_attack = 5
            self.max_carry_weight = 100
            self.cur_mana = self.max_mana
            self.cur_stamina = self.max_stamina
            self.cur_defense = self.max_defense
            self.cur_attack = self.max_attack
            self.cur_carry_weight = self.max_carry_weight
            self.weapon = 'Cracked Oak Staff'
        self.write_player_data()
        
                   
    def alter_stamina(self, amount, direction):
        if direction == 0:
            self.cur_stamina -= amount
        elif direction == 1:
            self.cur_stamina += amount
        else:
            pass
             
    def alter_health(self, amount, direction):
        if direction == 0:
            self.cur_health -= amount
        elif direction == 1:
            self.cur_health += amount
        else:
            pass
        
    def alter_mana(self, amount, direction):
        if direction == 0:
            self.cur_mana -= amount
        elif direction == 1:
            self.cur_mana += amount
        else:
            pass
        
    def place_inventory_item(self, items):
        for item in items:
            self.inventory = self.inventory.append(item)
            
        inventory = self.inventory
        
        # combine items and their quantities
        for item in inventory:
            if item in inventory:
                item.quantity += 1
                inventory.remove(item)
                
    def get_player(self):
        player = self
        
        return player
                


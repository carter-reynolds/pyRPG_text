from classes.Database import Database as db
import loot_table

# This class creates and tracks all of the player's stats and inventory
    
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
        
        self.inventory = Player.construct_inventory_items()
        
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
            self.weapon = ''     
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
            self.weapon = ''
        self.write_player_data()
        
    def rest(self):
        self.cur_stamina = self.max_stamina
        self.cur_health = self.max_health
        
    
    def use_health_potion(self):
        if self.cur_health == self.max_health:
            message = 'You are already at full health.'
            return False, message
        else:
            '''
                If for whatever reason the player is missing the health potion item
                in the inventory, this next code will add it back in.
            '''
            try:
                if self.inventory['Health Potion'] > 0:
                    message = 'You use a health potion and gain 25 health.'
                    self.cur_health + 25
                    return True, message
            except KeyError:
                message = "You don't have any health potions."
                self.inventory['Health Potion'] = 0
                return False, message
            
            else:
                message = print('You do not have any health potions.')
                return False, message
        
                   
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
                
    
    def construct_inventory_items():
        inventory_dict = {}
        
        inventory_list = loot_table.get_full_loot_table()
        
        for item in inventory_list:
            inventory_dict[item] = 0
            
        print(inventory_dict)
        
        return inventory_dict
    
    
                


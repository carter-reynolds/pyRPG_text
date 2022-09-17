class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.end = False
        
        self.start_path = 0     # Determines one of 3 story paths that result in different starting variables
        
        self.gold = 100
        self.weapon = ''
        self.location = 'B2'
        
        self.level = 1
        self.xp = 0
        self.xp_multiplier = 0
        
        self.items = []
        self.weapons = []
        self.pockets = []
        self.effects = []
        
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
        
    def set_player_stats(self, role):
        if role == 'Warrior':
            self.role = 'Warrior'
            self.max_health = 120
            self.max_mana = 20
            self.max_stamina = 150
            self.max_defense = 10
            self.max_attack = 15
            self.max_carry_weight = 100
            self.cur_health = 120
            self.cur_mana = 20
            self.cur_stamina = 150
            self.cur_defense = 10
            self.cur_attack = 15
            self.cur_carry_weight = 100
            self.weapon = 'Dulled Short Sword'     
        elif role == 'Mage':
            self.role = 'Mage'
            self.max_health = 85
            self.max_mana = 100
            self.max_stamina = 75
            self.max_defense = 10
            self.max_attack = 5
            self.max_carry_weight = 100
            self.cur_health = 85
            self.cur_mana = 100
            self.cur_stamina = 75
            self.cur_defense = 10
            self.cur_attack = 5
            self.cur_carry_weight = 100
            self.weapon = 'Cracked Oak Staff'
                   
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


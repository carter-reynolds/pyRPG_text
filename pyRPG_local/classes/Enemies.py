class Enemy:
    def __init__(self, name, type): # Only name and type will be required for now
        
        self.name = name    # The name of the enemy
        self.type = type    # What type of enemy they are
        self.level = 0
        self.health = 0     # How much health the enemy has
        self.defense = 0    # How well they can defend
        self.attack = 0     # How much damage they would do
        self.loot = []      # Loot they would drop, if any, will likely be randomly assigned
        self.weapon = ''    # Weapon they are using - should contribute to damage
        self.effect = []    # Random effect

"""
Define Enemy Configurations
"""

# Set up types of enemies we'll encounter
types = {
    0: "Bandit",
    1: "Goblin",
    2: "Undead",
    3: "Creature"
}

# 4 Enemy Levels, each can have a different adjective associates
# Example: Level 0 could be Feeble, Weak, ... etc
levels = {
    0: ["Feeble", "Weak"],
    1: ["Regular", "Normal"],
    2: ["Trained", "Seasoned", "Hardened", "Veteren", "Dangerous"],
    3: ["Berserker", "Heavy", "Deadly", "Insane"]
}

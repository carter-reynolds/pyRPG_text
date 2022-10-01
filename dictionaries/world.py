# Info we need to build and interact with the world:

zonemap_meta = {
    'A1': {'enemies': [], 'quests': [], 'items':[], 'can_rest': True, 'start_quests': True, 'solved': False},
    'A2': {'enemies': [], 'quests': [], 'items':[], 'can_rest': False, 'start_quests': False, 'solved': False},
    'A3': {'enemies': [], 'quests': [], 'items':[], 'can_rest': False, 'start_quests': False, 'solved': False},
    'B1': {'enemies': [], 'quests': [], 'items':[], 'can_rest': False, 'start_quests': False, 'solved': False},
    'B2': {'enemies': [], 'quests': [], 'items':[], 'can_rest': True, 'start_quests': False, 'solved': False},
    'B3': {'enemies': [], 'quests': [], 'items':[], 'can_rest': False, 'start_quests': False, 'solved': False},
    'C1': {'enemies': [], 'quests': [], 'items':[], 'can_rest': False, 'start_quests': False, 'solved': False},
    'C2': {'enemies': [], 'quests': [], 'items':[], 'can_rest': False, 'start_quests': False, 'solved': False},
    'C3': {'enemies': [], 'quests': [], 'items':[], 'can_rest': False, 'start_quests': False, 'solved': False}
}

zonemap_dict = {
    'A1': {
        'ZONENAME': 'Town',
        'DESCRIPTION':'A Town',
        'EXAMINATION': 'A quaint little town. Here you can buy/sell/trade items and start new quests!',
        'MOVEMENT':{
            'UP': '',
            'DOWN': 'B1',
            'LEFT': '',
            'RIGHT': 'A2'
        }
    },
    'A2':{
        'ZONENAME': 'The Wildlands',
        'DESCRIPTION':'The Wildlands, a place of nature and wonder. Monsters lurk, foes hides, and secrets await.',
        'EXAMINATION': 'You see a stick and some beetles... wow',
        'MOVEMENT':{
            'UP': '',
            'DOWN': 'B2',
            'LEFT': 'A1',
            'RIGHT': 'A3'
        }
    },
    'A3':{
        'ZONENAME': 'Decrepit Forest',
        'DESCRIPTION':'A shady forest, full of monsters and secrets.',
        'EXAMINATION': 'Rumors say there is a castle somewhere in this forest.',
        'MOVEMENT':{
            'UP': '',
            'DOWN': 'B3',
            'LEFT': 'A2',
            'RIGHT': ''
        }
    },
    'B1':{
        'ZONENAME': 'West River',
        'DESCRIPTION':'A peaceful river, with a bridge to the far east.',
        'EXAMINATION': 'If you had a fishing rod, you could catch some fish here.',
        'MOVEMENT':{
            'UP': 'A1',
            'DOWN': 'C1',
            'LEFT': '',
            'RIGHT': 'B2'
        }
    },
    'B2':{
        'ZONENAME': 'Homestead',
        'DESCRIPTION':'This is your homestead and land.',
        'EXAMINATION': 'You see your house, your barn, and your fields. Seems like a good place to "rest" and "save".',
        'MOVEMENT':{
            'UP': "A2",
            'DOWN': "C2",
            'LEFT': "B1",
            'RIGHT': "B3"
        }
    },
    'B3':{
        'ZONENAME': 'Stone Bridge',
        'DESCRIPTION':'A stone bridge, with a river to the far west and a dark forest to the north.',
        'EXAMINATION': 'examine',
        'MOVEMENT':{
            'UP': 'A3',
            'DOWN': 'C3',
            'LEFT': 'B2',
            'RIGHT': ''
        }
    },
    'C1':{
        'ZONENAME': 'A Dark Cave',
        'DESCRIPTION':'A dank wet cave... No clue what you\'ll find in here. May want to bring a torch!',
        'EXAMINATION': 'You look down. Bones crunch beneath your feet. You have no intention on being added to the them.',
        'MOVEMENT':{    
            'UP': 'B1',
            'DOWN': '',
            'LEFT': '',
            'RIGHT': 'C2'
        }
    },
    'C2':{
        'ZONENAME': 'example zone',
        'DESCRIPTION':'description',
        'EXAMINATION': 'examine',
        'MOVEMENT':{
            'UP': 'B2',
            'DOWN': '',
            'LEFT': 'C1',
            'RIGHT': 'C3'
        }
    },
    'C3':{
        'ZONENAME': 'example zone',
        'DESCRIPTION':'description',
        'EXAMINATION': 'examine',
        'MOVEMENT':{
            'UP': 'B3',
            'DOWN': '',
            'LEFT': 'C2',
            'RIGHT': ''
        }
    }  
}
solved_places = {
    'A1': False, 'A2': False, 'A3': False, 
    'B1': False, 'B2': False, 'B3': False, 
    'C1': False, 'C2': False, 'C3': False
}

zonemap_dict = {
    'A1': {
        'ZONENAME': 'Town',
        'DESCRIPTION':'A Town',
        'EXAMINATION': 'A quaint little town. Here you can buy/sell/trade items and start new quests!',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'B1',
        'LEFT': '',
        'RIGHT': 'A2'
    },
    'A2':{
        'ZONENAME': 'The Wildlands',
        'DESCRIPTION':'The Wildlands, a place of nature and wonder. Monsters lurk, foes hides, and secrets await.',
        'EXAMINATION': 'You see a stick and some beetles... wow',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'B2',
        'LEFT': 'A1',
        'RIGHT': 'A3'
    },
    'A3':{
        'ZONENAME': 'example zone',
        'DESCRIPTION':'description',
        'EXAMINATION': 'examine',
        'SOLVED': False,
        'UP': '',
        'DOWN': 'B3',
        'LEFT': 'A2',
        'RIGHT': ''
    },
    'B1':{
        'ZONENAME': 'example zone',
        'DESCRIPTION':'description',
        'EXAMINATION': 'examine',
        'SOLVED': False,
        'UP': 'A1',
        'DOWN': 'C1',
        'LEFT': '',
        'RIGHT': 'B2'
    },
    'B2':{
        'ZONENAME': 'Homestead',
        'DESCRIPTION':'This is your homestead and land.',
        'EXAMINATION': 'It\'s a nice place! You see the following things near by: \'tree\', \'lake\', \'cabin\'',
        'SOLVED': False,
        'UP': "A2",
        'DOWN': "C2",
        'LEFT': "B1",
        'RIGHT': "B3"
    },
    'B3':{
        'ZONENAME': 'example zone',
        'DESCRIPTION':'description',
        'EXAMINATION': 'examine',
        'SOLVED': False,
        'UP': 'A3',
        'DOWN': 'C3',
        'LEFT': 'B2',
        'RIGHT': ''
    },
    'C1':{
        'ZONENAME': 'A Dark Cave',
        'DESCRIPTION':'A dank wet cave... No clue what you\'ll find in here. May want to bring a torch!',
        'EXAMINATION': 'You look down. Bones crunch beneath your feet. You have no intention on being added to the them.',
        'SOLVED': False,
        'UP': 'B1',
        'DOWN': '',
        'LEFT': '',
        'RIGHT': 'C2'
    },
    'C2':{
        'ZONENAME': 'example zone',
        'DESCRIPTION':'description',
        'EXAMINATION': 'examine',
        'SOLVED': False,
        'UP': 'B2',
        'DOWN': '',
        'LEFT': 'C1',
        'RIGHT': 'C3'
    },
    'C3':{
        'ZONENAME': 'example zone',
        'DESCRIPTION':'description',
        'EXAMINATION': 'examine',
        'SOLVED': False,
        'UP': 'B3',
        'DOWN': '',
        'LEFT': 'C2',
        'RIGHT': ''
    }   
}
# NPC names dictionaries

npc_dialogue_data = {
     
    ## Shop Keeper Example Data ##
    "Shop Keeper": {
        
        "services":{
            "inquire": "example inquiry response",
            "provided": "example provided response"
        },
        
        "general": {
            "name": "The Shop Keeper",
            "backstory": "example backstory",
            "description": "example description",
            
            "greetings": {
                "hello": {
                    "hello1":"example hello response",
                    "hello2":"example hello response",
                    "hello3":"example hello response",
                },
                
                "goodbye": {
                    "goodbye1":"example goodbye response",
                    "goodbye2":"example goodbye response",
                    "goodbye3":"example goodbye response",
                },
            },
            
            "rumors": {
                "rumor1": "example rumor1", # assign a choice from list of random rumors?
            }
        },
        
        "quest": {
            "quest 1": {
                "start": "example quest start dialogue ",
                "end": "example quest end dialogue",
                "description": "example quest description",
            }
        }   
    }
}       


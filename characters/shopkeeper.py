

def shop_keeper_barter(player):
    print("Shopkeeper: Hello there, " + player.name + ". What can I do for you?")
    print("1. Buy")
    print("2. Sell")
    print("3. Leave")
    choice = input("> ")
    if choice == "1":
        print("Shopkeeper: What would you like to buy?")
        print("1. Health Potion")
        print("2. Mana Potion")
        print("3. Leave")
        choice = input("Choice: ")
        if choice == "1":
            if player.gold >= 10:
                player.gold -= 10
                player.inventory['Health Potion'] += 1
                print("Shopkeeper: Here you go.")
            else:
                print("Shopkeeper: You don't have enough gold.")
        elif choice == "2":
            if player.gold >= 10:
                player.gold -= 10
                player.inventory['Mana Potion'] += 1
                print("Shopkeeper: Here you go.")
            else:
                print("Shopkeeper: You don't have enough gold.")
        elif choice == "3":
            return
        else:
            print("Shopkeeper: I don't understand.")
            shop_keeper_barter(player)
    elif choice == "2":
        print("Shopkeeper: What would you like to sell?")
        print("1. Health Potion")
        print("2. Mana Potion")
        print("3. Leave")
        choice = input("Choice: ")
        if choice == "1":
            if player.inventory['Health Potion'] >= 1:
                player.inventory["Health Potion"] -= 1
                player.gold += 10
                print("Shopkeeper: Thank you.")
            else:
                print("Shopkeeper: You don't have any Health Potions.")
        elif choice == "2":
            if player.inventory['Mana Potion'] >= 1:
                player.inventory["Mana Potion"] -= 1
                player.gold += 10
                print("Shopkeeper: Thank you.")
            else:
                print("Shopkeeper: You don't have any Mana Potions.")
        elif choice == "3":
            return
        else:
            print("Shopkeeper: I don't understand.")
            shop_keeper_barter(player)
    elif choice == "3":
        print("Shopkeeper: Goodbye.")
    else:
        print("Shopkeeper: I don't understand.")
        shop_keeper_barter(player)
        


    
    
        
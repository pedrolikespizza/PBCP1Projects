# pb period 1 combat fighting game project


import random

def create_character():
    

    name = input("enter your characters name: ")

    print("choose your combat class:")
    print("1. fighter")
    print("2. wizard")
    print("3. archer")

    while True:
        choice = input(" input 1 2 or 3: ")

        if choice == "1":
            character_class = "fighter"
            health = 120
            attack = 20
            defense = 8
            break
        elif choice == "2":
            character_class = "wizard"
            health = 90
            attack = 30
            defense = 3
            break
        elif choice == "3":
            character_class = "archer"
            health = 100
            attack = 25
            defense = 5
            break
        else:
            print("not apart of the 3 numbers. enter 1, 2, or 3.")

    print("this is your character")
    print("name:", name)
    print("class:", character_class)
    print("health:", health)
    print("attack:", attack)
    print("defense:", defense)

    return name, character_class, health, attack, defense

def show_health(player_health, monster_health):
    print("this is your health:", max(0, player_health))
    print("this the monsters health:", max(0, monster_health))

def player_turn(name, health, attack, monster_health, defense):
    print("it is your turn to attack")
    print("1. attack - do a normal amount of dmg")
    print("2. heavy attack - do a extra amount of dmg")
    print("3. shield - reduce the incoming attack")
    print("4. hp potion - gain health")

    while True:
        choice = input(" choose a option for combat (1-4): ")

        if choice == "1":
            damage = random.randint(attack - 5, attack + 5)
            monster_health = damage
            print(name, "attacked the monster")
            print(name," dealt", damage, "dmg")
            break

        elif choice == "2":
            damage = random.randint(attack + 5, attack + 15)
            monster_health = damage
            print(name, "used heavy attack")
            print(name, " dealt", damage, "dmg")
            break

        elif choice == "3":
            defense += 10
            print(name, "defends instead of attacking for some reason")
            print(name, "has extra defense for the next attack from the monster")
            break

        elif choice == "4":
            healing = random.randint(15, 25)
            health += healing
            print(name, "used a healing potion")
            print(name, "got", healing, "health")
            break

        else:
            print("not apart of the choosen numbers. (1-4)")

    return health, monster_health, defense

def monster_turn(health, monster_attack, defense):

    choice = random.choice(["attack", "heavy", "defend"])

    if choice == "attack":
        damage = random.randint(monster_attack - 5, monster_attack + 5)
        damage = max(0, damage - defense)
        health -= damage
        print("The monster attacked")
        print("the monster did", damage, "dmg to you")

    elif choice == "heavy":
        damage = random.randint(monster_attack + 5, monster_attack + 15)
        damage = max(0, damage - defense)
        health -= damage
        print("the monster decided to do a heavy attack on you")
        print("the monster did", damage, "dmg to you")

    else:
        print("the monster is scared and wants to defend its self")
        print("it will have extra defense on the next play")

    defense = 0

    return health, defense

def combat():
    name, character_class, health, attack, defense = create_character()

    monster_health = 100
    monster_attack = 15

    
    print(" a scary big poopy head monster came out of nowhere and wants to hurt you...")
    print(name," has to slime out the big poopy head monster to stay alive")

    first_turn = random.choice(["player", "monster"])

    if first_turn == "player":
        print(name, " gets to attack first")
    else:
        print("the big poopy head monster gets to attack first")

    current_turn = first_turn

   
    while health > 0 and monster_health > 0:

        show_health(health, monster_health)

        if current_turn == "player":
            health, monster_health, defense = player_turn(
                name, health, attack, monster_health, defense
            )
            current_turn = "monster"

        else:
            health, defense = monster_turn(
                health, monster_attack, defense
            )
            current_turn = "player"

    if health <= 0:
        print("you got killed by the poopy head monster...")
        print("the poopy head monster sadly wins")
    else:
        print("good job. im so proud of you" + name + " ")
        print("you killed the poopy head monster")
        print("you win gg")

combat()
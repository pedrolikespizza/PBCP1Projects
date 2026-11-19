# pb period 1 combat fighting game project

import random


# Character creation
def create_character():
    print("welcome to the game.")

    name = input(" what your name:").strip()

    while name == "":
        print(" not a name try again")
        name = input(" whats your name: ").strip()

    print("choose a character")
    print("1. fighter")
    print("2. wizard")
    print("3. archer")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()

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
            print("invalid lil tung. enter 1, 2, or 3.")

    player = {
        "name": name,
        "class": "character_class",
        "health": "health",
        "max_health": "health",
        "attack": "attack",
        "defense": "defense",
        "guard": False
    }

    print("this is your character")
    print("Name:", name)
    print("Class:", character_class)
    print("Health:", health)
    print("Attack:", attack)
    print("Defense:", defense)

    return player


# Display character health
def show_status(player, monster):
    print(player["name"], "hp:", player["health"])
    print(monster["name"], "hp:", monster["health"])
    print("------------------------------")


# Player's turn
def user_turn(player, monster):
    print("\n" + player["name"] + "'s Turn!")
    print("\nChoose your action:")
    print("1. Normal Attack - Regular damage")
    print("2. Heavy Attack - More damage, less accuracy")
    print("3. Defend - Reduce incoming damage")
    print("4. Heal - Restore health")

    while True:
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            damage = player["attack"] + random.randint(1, 5)
            monster["health"] -= damage
            player["guard"] = False
            print("\nYou used Normal Attack!")
            print("You dealt", damage, "damage!")

        elif choice == "2":
            if random.random() < 0.70:
                damage = player["attack"] * 2 + random.randint(1, 5)
                monster["health"] -= damage
                print("\nYour Heavy Attack hit!")
                print("You dealt", damage, "damage!")
            else:
                print("\nYour Heavy Attack missed!")
            player["guard"] = False

        elif choice == "3":
            player["guard"] = True
            print("\nYou raised your defense!")
            print("You will take reduced damage next turn.")

        elif choice == "4":
            healing = random.randint(15, 25)
            old_health = player["health"]
            player["health"] = min(
                player["max_health"],
                player["health"] + healing
            )
            actual_healing = player["health"] - old_health
            player["guard"] = False
            print("\nYou used Heal!")
            print("You restored", actual_healing, "health!")

        else:
            print("Invalid choice! Please enter a number from 1-4.")
            continue

        break

    if monster["health"] < 0:
        monster["health"] = 0


# Monster's turn
def monster_turn(player, monster):
    print("\n" + monster["name"] + "'s Turn!")

    action = random.choice(["attack", "heavy", "heavy"])

    if action == "attack":
        damage = monster["attack"] + random.randint(1, 5)
        print("The monster uses a normal attack!")

    else:
        damage = monster["attack"] * 2
        print("The monster uses a powerful attack!")

    damage -= player["defense"]

    if player["guard"]:
        damage = damage // 2
        print("Your defense reduces the damage!")

    damage = max(1, damage)

    player["health"] -= damage

    if player["health"] < 0:
        player["health"] = 0

    player["guard"] = False

    print("The monster dealt", damage, "damage!")


# Main combat game
def combat():
    player = create_character()

    monster = {
        "name": "Dragon",
        "health": 150,
        "attack": 15
    }

    print("\n================================")
    print("A wild Dragon appears!")
    print("Prepare for battle, " + player["name"] + "!")
    print("================================")

    # Randomly choose who goes first
    first_turn = random.choice(["player", "monster"])

    if first_turn == "player":
        print("\nYou get the first turn!")
    else:
        print("\nThe Dragon gets the first turn!")

    # Combat loop
    while player["health"] > 0 and monster["health"] > 0:

        if first_turn == "player":
            user_turn(player, monster)

            if monster["health"] <= 0:
                break

            monster_turn(player, monster)

        else:
            monster_turn(player, monster)

            if player["health"] <= 0:
                break

            user_turn(player, monster)

        show_status(player, monster)

    # Determine winner
    print("\n================================")
    print("          BATTLE OVER!")
    print("================================")

    if player["health"] > 0:
        print("Congratulations,", player["name"] + "!")
        print("You defeated the Dragon!")
        print("YOU WIN!")
    else:
        print("The Dragon defeated you.")
        print("GAME OVER!")

    print("\nFinal Health:")
    print(player["name"] + ":", player["health"])
    print("Dragon:", monster["health"])


# Start the game
combat()
# pb period 1 fix the game project

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False:
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number: # i put in a colon. it was a syntax error it stopped the code from running in the first place
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print("Your guesses per round: " + str(scores)) # i put a string. it was a runtime error. it stoped code from running once it hit line 33

total = 0
for score in scores: # i took away the second total = 0. it was a logic error. it made the code run badly
    total = total + score

average = total / rounds
print("Your average guesses per round was " + str(round(average, 2))) 

best_round = scores[0]
for i in range(1, rounds): # i took away the - 1. it was a logic error. it prevented the loop from working properly
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")
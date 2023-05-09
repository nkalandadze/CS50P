# დავალება #25 - Guessing Game
import random

# Prompts the user for a level, n. 
while True:
    try:
        level = int(input("Level: "))

# If the user does not input a positive integer, the program should prompt again.      
        if level > 0:
            break
    except:
        pass

# Randomly generates an integer between 1 and n inclusive
random_number = random.randint(0,level)

# Prompts the user to guess that integer.
while True:
    try:
        guess_number = int(input("Guess: "))
# If the guess is not a positive integer, the program should prompt the user again.
        if guess_number > 0:

# If the guess is the same as that integer, the program should output Just right! and exit.
            if guess_number == random_number:
                print("Just right!")
                break

# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
            elif guess_number > random_number:
                print("Too large!")

# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
            else:
                print("Too small!")
    except:
        pass










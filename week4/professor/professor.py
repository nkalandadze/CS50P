# დავალება #26 - Little Professor
import random

def main():
    # get the level of game
    level = get_level()

    # calculate total score
    score = get_score(level)

    #print final score
    print(f"Score: {score}")


# give user 10 equations and calculate their score for each correct answer
def get_score(level):
    rounds = 10
    score = 0
    while rounds > 0:
        x = generate_integer(level)
        y = generate_integer(level)

        if play_round(x,y) == True:
            score = score + 1
        rounds = rounds - 1

    return score

# in each round give user 3 chances to get correct answer
def play_round(x,y):
    attempts = 3
    while attempts > 0:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                attempts = attempts - 1 
                print("EEE")
        except:
            attempts = attempts - 1
            print("EEE") 
    print(f"{x} + {y} = {x + y}")
    return False


# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except:
            pass

# returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99) 
    else:
        return random.randint(100,999) 


if __name__ == "__main__":
    main()
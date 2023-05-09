import random

def main():
    print("Welcome to Rock, Paper, Scissors game!")
    user_score = 0
    computer_score = 0
    play_game = True

    while play_game:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result, winner = get_winner(user_choice, computer_choice)
        print(result)

        # add score to winner
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        print(f"User score: {user_score}")
        print(f"Computer score: {computer_score}")

        # if user or computer score gets 3 point, the final result is displayed and user is asked if they want to play again
        if user_score == 3:
            print("You won the game! 🎉")
            print("Thank you for playing with me.")
            user_score = 0
            computer_score = 0
            play_game = play_again()
        elif computer_score == 3:
            print("You lost the game! 😕")
            print("Thank you for playing with me.")
            user_score = 0
            computer_score = 0
            play_game = play_again()
            

# get user choice
def get_user_choice():
    user_choice = input("Enter you choice (rock, paper or scissors): ").lower().strip()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose from the list (rock, paper, scissors): ")
        user_choice = input("Enter you choice (rock, paper or scissors): ").lower().strip()
    return user_choice

# generate random computer choice
def get_computer_choice():
    computer_choice = random.choice(["rock", "paper", "scissors"])
    return computer_choice

# determine winner
def get_winner(user_choice, computer_choice):
    # rock beats scissors, scissors beats paper, paper beats rock
    if user_choice == computer_choice:
        return "It's a tie", None
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return f"You played {user_choice.title()}\nComputer played {computer_choice.title()}\nYou won! {user_choice.title()} beats {computer_choice.title()}", "user"
    else:
        return f"You played {user_choice.title()}\nComputer played {computer_choice.title()}\nYou lost! {computer_choice.title()} beats {user_choice.title()}", "computer"

# play again or not ?
def play_again():
    play_again = input("Do you want to play again. Enter Y or N: ").lower().strip()
    if play_again == "y":
        return True
    else:
        return False

if __name__ == "__main__":
    main()
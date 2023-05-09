# Rock, Paper, Scissors Game

My name is Nini from Tbilisi, Georgia

## Video Demo: https://www.youtube.com/watch?v=dpttgkFIl9s

## Description:

This is a simple implementation of the classic game **"Rock, Paper, Scissors"** using **Python**.

This project implements a basic version of the game "Rock, Paper, Scissors", where the user can play against the computer. User selects their choice (rock, paper, or scissors), while the computer randomly generates its choice. The winner is determined based on the game rules:

```
- rock beats scissors
- paper beats rock
- scissors beats paper
```

Scores are tracked throughout the game.

## Features

To build the game following functions are used:

- **get_user_choice()**: asks user to input their choice. If user enters other then "rock", "paper" or "scissors" case insensitively, following output is shown: **"Invalid input. Please choose from the list (rock, paper, scissors)"** and user is asked to enter input again.

- **get_computer_choice()**: randomly generates computer choice from the list: (rock, paper, scissors).

- **get_winner()**: function has who arguments: user_choice and computer_choice. Based on general rule function has two outputs: result and winner.
  For example, if user_choice is "rock" and computer_choice is "scissors", result is: **"You won! Rock beats Scissors"** and winner is **"user"**.
  If user_choice and computer_choice are the same result is: **"It's a tie"** and winner is **None**.

- **play_again()**: asks user if they want to play again.

- After each round scores are tracked and the results are displayed. When user or computer score gets 3, winner of the game is displayed and user is asked if they want to play again.

## Test file features

In the test file three functions are tested:

- **get_winner()**: all nine scenarios are tested. In three of them result is tie (`test_tie()`). In three user is winner (`test_user_winning()`) and in another 3 computer is winner (`test_computer_winning()`).
- **test_get_user_choice()**: unittest.mock.patch() function is used to replace input() function to simulate user input and test function's behavior.
- **test_get_computer_choice()**: unittest.mock.patch() function is used to replace random.choice() function to control random choice and test function's behavior.

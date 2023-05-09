from project import get_winner, get_user_choice, get_computer_choice
from unittest.mock import patch

# test get_winner function with 9 different scenarios
# test when user wins
def test_user_winning():
    assert get_winner("rock", "scissors") == ("You played Rock\nComputer played Scissors\nYou won! Rock beats Scissors", "user")
    assert get_winner("paper", "rock") == ("You played Paper\nComputer played Rock\nYou won! Paper beats Rock", "user")
    assert get_winner("scissors", "paper") == ("You played Scissors\nComputer played Paper\nYou won! Scissors beats Paper", "user")

# test when computer wins
def test_computer_winning():
    assert get_winner("rock", "paper") == ("You played Rock\nComputer played Paper\nYou lost! Paper beats Rock", "computer")
    assert get_winner("paper", "scissors") == ("You played Paper\nComputer played Scissors\nYou lost! Scissors beats Paper", "computer")
    assert get_winner("scissors", "rock") == ("You played Scissors\nComputer played Rock\nYou lost! Rock beats Scissors", "computer")

# test when it's a tie
def test_tie():
    assert get_winner("rock", "rock") == ("It's a tie", None)
    assert get_winner("paper", "paper") == ("It's a tie", None)
    assert get_winner("scissors", "scissors") == ("It's a tie", None)


def test_get_user_choice():
    with patch("builtins.input", return_value="rock"):
        assert get_user_choice() == "rock"
    with patch("builtins.input", return_value="paper"):
        assert get_user_choice() == "paper"
    with patch("builtins.input", return_value="scissors"):
        assert get_user_choice() == "scissors"
    

def test_get_computer_choice():
    with patch("random.choice", return_value="rock"):
        assert get_computer_choice() =="rock"
    with patch("random.choice", return_value="paper"):
        assert get_computer_choice() =="paper"
    with patch("random.choice", return_value="scissors"):
        assert get_computer_choice() =="scissors"

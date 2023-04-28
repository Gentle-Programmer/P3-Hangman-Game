import random

def dispaly_welcome():
    logo = r"""
  +---+
  |   |
      |
      |
      |
      |
========='''"""
    print(logo)
    print("Welcome to Hangman")
    start_game = input("Do you want to start the game? (y/n): ").lower()
    return start_game == "y"

if dispaly_welcome():
    print("Let's get started")
else:
    print("Goodbye!")

def get_name():
    pass

def select_random_word():
    pass

def get_use_guess():
    return input("Enter a letter: ").lower()



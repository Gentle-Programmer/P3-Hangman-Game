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
    return input("Enter your name: ")

def select_random_word():
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    return random.choice(words)

def get_user_guess():
    return input("Enter a letter: ").lower()

def display_game_status():
    hangman_parts = [
       r"""
  +---+
  |   |
      |
      |
      |
      |
=========''', r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''] 
    

import random
from hangman_logo import HANGMAN_LOGO, HANGMAN_STAGES

def dispaly_welcome():
    print(HANGMAN_LOGO)
    print("Welcome to Hangman!")


def get_name():
    return input("Enter your name: ")

def select_random_word():
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    return random.choice(words)

def get_user_guess():
    return input("Enter a letter: ").lower()

def display_game_status():
  pass

    
def main_game_loop():
    pass
  

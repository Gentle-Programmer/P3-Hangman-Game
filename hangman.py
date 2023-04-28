import random
from hangman_logo import HANGMAN_LOGO, HANGMAN_STAGES

def dispaly_welcome():
    print(HANGMAN_LOGO)
    print("Welcome to Hangman!")

def start_game():
    user_input = input("Do you want to start the game? (yes/no): ").lower()
    return user_input == 'yes'

def get_name():
    return input("Please enter your name: ")

def select_random_word():
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
    return random.choice(words)

def mask_word(word):
    return "_" * len(word)

def display_game_status(masked_word):
    print(HANGMAN_STAGES[6 - attemps_remaining])


def get_user_guess():
    return input("Enter a letter: ").lower()


    
def main_game_loop():
    word = select_random_word()
    masked_word = mask_word()
    attemps_remaining = 6
    wrong_guesses
  

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

def display_game_status(masked_word, attemps_remaining, wrong_guesses):
    print(HANGMAN_STAGES[6 - attemps_remaining])
    print(f"Word: {masked_word}")
    print(f"Attemps remaining: {attemps_remaining}")
    print(f"Wrong guesses: {', '.join(wrong_guesses) }")

def get_user_guess():
    return input("Enter a letter (a single letter): ").lower()

def update_game_status(user_guess, word, masked_word, attemps_remaining, wrong_guesses):
    if user_guess in word:
        new_masked_word = ""
        for letter, masked_letter in zip(word, masked_word):
            if letter == user_guess:
                new_masked_word += letter
            else:
                new_masked_word += masked_letter
        return new_masked_word, attemps_remaining, wrong_guesses
    

def main_game_loop():
    word = select_random_word()
    masked_word = mask_word()
    attemps_remaining = 6
    wrong_guesses = []

    while attemps_remaining > 0 and masked_word != word:
        display_game_status(masked_word, attemps_remaining, wrong_guesses)
        user_guess = get_user_guess()
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Invalid input. Please enter a single letter.")
        elif user_guess in wrong_guesses or user_guess in masked_word:
            print("You-ve already guessed that letter.")
        else:
            pass
  

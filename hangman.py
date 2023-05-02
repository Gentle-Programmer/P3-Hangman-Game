import random
import pyinputplus as pypi
from hangman_logo import HANGMAN_LOGO, HANGMAN_STAGES
from hangman_google import append_data_to_sheet, get_all_data, SHEET
from datetime import datetime


def dispaly_welcome():
    print(HANGMAN_LOGO)
    print("Welcome to Hangman!")
    print("In this game, you have to guess the word by syggesting individual "
          "letters. You have 6 attemps to guess the word. Good luck!")


def start_game():
    user_input = pypi.inputYesNo("Do you want to start the game?"
                                 "(yes/no): ").lower()
    return user_input == 'yes'


def get_name():
    return input("Please enter your name: ")


def select_random_word():
    words = ['apple', 'banana', 'orange', 'grape', 'kiwi',
             'strawberry', 'melon', 'pineapple', 'mango',
             'papaya', 'peach', 'apricot', 'coconut']
    return random.choice(words)


def mask_word(word):
    return "_" * len(word)


def display_game_status(masked_word, attemps_remaining, wrong_guesses):
    print(HANGMAN_STAGES[6 - attemps_remaining])
    print(f"Word: {masked_word}")
    print(f"Attemps remaining: {attemps_remaining}")
    print(f"Wrong guesses: {', '.join(map(str, wrong_guesses)) }")


def get_user_guess():
    return input("Enter a letter (a single letter): ").lower()


def update_game_status(user_guess, word, masked_word,
                       attemps_remaining, wrong_guesses):
    if user_guess in word:
        new_masked_word = ""
        for letter, masked_letter in zip(word, masked_word):
            if letter == user_guess:
                new_masked_word += letter
            else:
                new_masked_word += masked_letter
        return new_masked_word, attemps_remaining, wrong_guesses
    else:
        attemps_remaining -= 1
        wrong_guesses.append(user_guess)
        return masked_word, attemps_remaining, wrong_guesses


def display_game_result(result):
    if result:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost.")


def display_previous_scores():
    print("\nPrevious users scores: ")
    worksheet = SHEET.worksheet("scores")
    data = worksheet.get_all_records()
    for record in data:
        print(f"{record['timestamp']} - {record['name']} - {record['score']}")


def play_again():
    return pypi.inputYesNo("\nDo you want to play again? (yes/no)").lower() == 'yes'


def main_game_loop():
    dispaly_welcome()
    if start_game():
        name = get_name()
        
        while True: 
            word = select_random_word()
            masked_word = mask_word(word)
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
                    masked_word, attemps_remaining, wrong_guesses = (
        update_game_status(
            user_guess, word, masked_word, attemps_remaining, wrong_guesses
        )
)
            result = masked_word == word
            display_game_result(result)
            score = attemps_remaining
            current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            append_data_to_sheet([current_time,name, score])
            display_previous_scores()

            if not play_again():
                break
    else:
        print("Goodbye")


main_game_loop()

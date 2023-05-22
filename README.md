# P3-Hangman-Game


## Overview
This is a simple text-based Hangman game written in Python. The player has to guess a randomly chosen word by suggesting individual letters. The player has 6 attempts to guess the word. After each game, the player's score and game timestamp are stored in a Google Sheet. Previous users' scores are displayed after each game, and the player is asked if they want to play again.

The live site can be found [here](https://hangman-game-9.herokuapp.com/)


## User Stories

1. As a player, I want to see a welcome message and the game's rules when I start the game.
2. As a player, I want to be able to enter my name.
3. As a player, I want to be prompted to guess a letter.
4. As a player, I want to see the number of attempts remaining and the wrong guesses I've made so far.
5. As a player, I want to know if I've won or lost the game.
6. As a player, I want to see the previous users' scores after each game.
7. As a player, I want to be asked if I want to play again after each game.


## Flowchart

1. Start. Display welcome message and instructions
2. Ask the user if they want to start the game
If yes, continue to step 4
If no, proceed to step 13
3. Get the user's name
4. Select a random word from the list
5. Mask the word with underscores. Set the initial values for attempts remaining and wrong guesses.
6. Display the game status (masked word, attempts remaining, and wrong guesses).
7. Get user input for a letter.
8. Update the game status based on the user's input.
9. Check if the user has won, lost, or if the game is still ongoing
If the user has won or lost, proceed to step 12.
10. If the game is still ongoing, return to step 8.
11. Display the game result, send and display the score, and ask if the user wants to play again
If yes, return to step 5. If no, proceed to step 13.
12. End the program.


## Libraries Used

random: to select a random word from the list of words.
pyinputplus: to validate user input (e.g., checking if input is "yes" or "no").
gspread: to interact with Google Sheets API for storing and retrieving scores.
google-auth: to authenticate with Google Sheets API.
datetime: to record the timestamp of each game.


## Code Explanation
The code consists of several functions that handle different aspects of the game:

1. dispaly_welcome(): displays the welcome message and game rules.
2. start_game(): asks the user if they want to start the game.
3. get_name(): gets the player's name.
4. select_random_word(): selects a random word from a list of words.
5. mask_word(): masks the word with underscores.
6. display_game_status(): displays the game status (masked word, attempts remaining, wrong guesses).
7. get_user_guess(): gets a letter guessed by the user.
8. update_game_status(): updates the game status based on the user's guess.
9. display_game_result(): displays the game result (win/lose).
10. display_previous_scores(): displays the previous users' scores.
11. play_again(): asks the user if they want to play again.
12. main_game_loop(): the main game loop that calls other functions and manages the game flow.


## Possible Improvements

1. Add more words to the list or fetch words from an external API to increase the game's difficulty.
2. Improve the user interface, e.g., by using a library like curses to create a more interactive terminal-based interface.
3. Implement a leaderboard feature to display the top 10 players based on their scores.
4. Add difficulty levels, e.g., by limiting the number of attempts or increasing the complexity of words.


## How to Run the Game

1. Install the required packages by running pip install -r requirements.txt.
2. Set up the Google Sheets API and obtain the creds.json file as described in the Google Sheets API documentation.
3. Create a Google Sheet and update the SHEET variable in the hangman_google.py file with the name of the sheet.
4. Run the hangman.py script to start the game: python hangman.py.

Enjoy the game!


## References and Learning Materials

Python Official Documentation: The official Python documentation is a comprehensive resource covering all aspects of the Python programming language. It includes tutorials, guides, and reference materials for various Python libraries and functions. [Link](https://docs.python.org/3/)

Google Sheets API: The Google Sheets API documentation provides a detailed guide on how to interact with Google Sheets using various programming languages, including Python. This guide covers authentication, reading and writing data, and working with spreadsheets. [Link](https://developers.google.com/sheets/api/guides/concepts)

gspread library: The gspread library is a popular Python library that simplifies working with the Google Sheets API. It provides an easy-to-use interface for interacting with Google Sheets. The GitHub repository includes extensive documentation and examples. [Link](https://github.com/burnash/gspread)

pyinputplus library: The pyinputplus library is a Python module for validating user input. This library allows you to add input validation features to your Python programs easily. The GitHub repository includes documentation and examples. [Link](https://github.com/asweigart/pyinputplus)

YouTube Tutorials: [How to Code a Game of Hangman... The EASY Way!! (Beginner Python Tutorial)](https://www.youtube.com/watch?v=cJJTnI22IF8); [How To Code Hangman In Python | Tutorial For Beginners](https://www.youtube.com/watch?v=pFvSb7cb_Us)

Enjoy playing!
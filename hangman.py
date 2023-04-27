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

dispaly_welcome()
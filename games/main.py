import sys
import os

# Ensure the parent directory is in the Python path
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import rock_paper_scissors as rps
import guess_the_number as gtn
import tic_tac_toe as ttt

def main():
    print("Choose a game to play:")
    print("1. Rock, Paper, Scissors")
    print("2. Guess the Number")
    print("3. Tic-Tac-Toe")
    choice = input("Enter the number of the game you want to play: ")

    if choice == '1':
        print(rps.play())
    elif choice == '2':
        print(gtn.play())
    elif choice == '3':
        print(ttt.play())
    else:
        print("Invalid choice. Please choose a valid game number.")

if __name__ == "__main__":
    main()


##8.Importing Modules Using a Name Given in a String Problem: Example Case
'''import importlib


def dynamic_import(module_name):§
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError:
        print(f"Module {module_name} could not be imported.")
        return None


def main():
    # Example: Let’s say the user selects which game module to import
    user_choice = input("Enter the module to import (e.g., 'rock_paper_scissor.game_logic'): ")

    # Dynamically import the chosen module
    game_module = dynamic_import(user_choice)

    if game_module:
        result = game_module.play('rock')  # Example argument
        print(result)


if __name__ == "__main__":
    main()'''


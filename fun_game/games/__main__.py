import sys
import os

# Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import rock_paper_scissor as rps
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










'''import sys
import os

# Adjust the path to include the root of the ZIP file
sys.path.insert(0, os.path.dirname(__file__))


# Import the modules relative to the root of the ZIP file
import rock_paper_scissor as rps
import guess_the_number as gtn
import tic_tac_toe as ttt


def main():
    print("Choose a game to play:")
    print("1. Rock, Paper, Scissors")
    print("2. Guess the Number")
    print("3. Tic-Tac-Toe")

    choice = input("Enter the number of the game you want to play: ")

    if choice == '1':
        user_choice = rps.user_input.get_user_choice()
        result = rps.game_logic.play(user_choice)
        print(result)
    elif choice == '2':
        print(gtn.play())
    elif choice == '3':
        print(ttt.play())
    else:
        print("Invalid choice. Please choose a valid game number.")


if __name__ == "__main__":
    main()'''

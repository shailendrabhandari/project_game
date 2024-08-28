import sys
import os

# Add the directory containing the 'rock_paper_scissors' module to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'classic')))

# Now you can import the module
import rock_paper_scissor as rps

def main():
    user_choice = rps.get_user_choice()
    result = rps.play(user_choice)
    print(result)

if __name__ == "__main__":
    main()

# rock_paper_scissors/game_logic.py

import random

def play(user_choice):
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user_choice == computer:
        return f"Both chose {user_choice}. It's a tie!"

    if is_win(user_choice, computer):
        return f"User wins! {user_choice} beats {computer}"

    return f"Computer wins! {computer} beats {user_choice}"


def is_win(player, opponent):
    return (player == 'rock' and opponent == 'scissors') or \
           (player == 'scissors' and opponent == 'paper') or \
           (player == 'paper' and opponent == 'rock')


import random

def play():
    user = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return f"Both chose {user}. It's a tie!"

    if is_win(user, computer):
        return f"User wins! {user} beats {computer}"

    return f"Computer wins! {computer} beats {user}"

def is_win(player, opponent):
    return (player == 'rock' and opponent == 'scissors') or \
        (player == 'scissors' and opponent == 'paper') or \
        (player == 'paper' and opponent == 'rock')


__all__ = ['play', 'is_win']  # Only export the 'play' function

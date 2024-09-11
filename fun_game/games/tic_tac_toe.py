import random


def play():
    board = [' ' for _ in range(9)]  # A list to hold the board spaces
    print_board(board)

    while ' ' in board:
        player_move(board)
        print_board(board)
        if check_winner(board, 'X'):
            return "You win!"
        if ' ' not in board:
            break

        computer_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            return "Computer wins!"

    return "It's a tie!"


def print_board(board):
    for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print()


def player_move(board):
    while True:
        try:
            move = int(input("Choose a position from 1-9: ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move. Position already taken or out of range, try again.")
        except ValueError:
            print("Please enter a number.")


def computer_move(board):
    possible_moves = [i for i, x in enumerate(board) if x == ' ']
    move = random.choice(possible_moves)  # Computer picks a random valid spot
    board[move] = 'O'


def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


if __name__ == "__main__":
    result = play()
    print(result)

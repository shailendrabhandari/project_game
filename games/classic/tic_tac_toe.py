def play():
    board = [' ' for _ in range(9)]  # A list to hold the board spaces
    print_board(board)

    while ' ' in board:
        player_move(board)
        if check_winner(board, 'X'):
            return "You win!"
        if ' ' not in board:
            break
        
        computer_move(board)
        if check_winner(board, 'O'):
            return "Computer wins!"
        
        print_board(board)

    return "It's a tie!"

def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def player_move(board):
    move = int(input("Choose a position from 1-9: ")) - 1
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Position already taken, try again.")
        player_move(board)

def computer_move(board):
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            break

def check_winner(board, player):
    # Winning conditions
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
                      (0, 4, 8), (2, 4, 6)]            # Diagonal
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)
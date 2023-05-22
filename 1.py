# Import the necessary modules
import random

# Define the game board
board = [[' ' for i in range(3)] for j in range(3)]

# Define the players
players = ['X', 'O']

# Get the current player
current_player = random.choice(players)

# Start the game loop
while True:

    # Get the player's move
    move = input('Player {}'.format(current_player) + ', please enter your move (1-9): ')

    # Validate the move
    if move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        print('Invalid move. Please try again.')
        continue

    # Make the move
    row = int(move) // 3
    col = int(move) % 3
    board[row][col] = current_player

    # Check for a winner
    winner = check_winner(board)
    if winner is not None:
        print('Winner is {}!'.format(winner))
        break

    # Check for a tie
    if is_tie(board):
        print('Tie game!')
        break

    # Switch players
    current_player = players[players.index(current_player) ^ 1]

# Define a function to check for a winner
def check_winner(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return board[row][0]
        if board[0][row] == board[1][row] == board[2][row] != ' ':
            return board[0][row]
        if board[row][0] == board[1][1] == board[2][2] != ' ':
            return board[row][0]
        if board[2][0] == board[1][1] == board[0][2] != ' ':
            return board[2][0]
    return None

# Define a function to check for a tie
def is_tie(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True
from random import *

board = []

for x in range(5):
    board.append(["0"]*5)

def print_board(board):
    for i in board:
        print(" ".join(i))
print("Lets play battleships")
print_board(board)

def random_row(board):
    return randint(0, len(board)-1)
def random_col(board):
    return randint(0, len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Column: "))

if guess_row == ship_row and guess_col == ship_col:
        print("Congrats, you sank my battleship!")

else:
    if guess_row>=6 or guess_col>=6:
        print("Out of range")        
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = 'X'
        print_board(board)
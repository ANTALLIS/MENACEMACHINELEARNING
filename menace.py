import random
from tttAI import *

def playRandomMove(game_board):
    # Chooses a random position on the board and returns a number
    play_pos = []
    
    for i in range(9):
        if game_board[i] == "-":
            play_pos.append(i)
    
    random.shuffle(play_pos)
    if len(play_pos) == 0:
        return None
    return play_pos[0]

def rotateBoard(game_board):
        # Returns a new board that is rotated clockwise 90 degrees
        new_board = []
        rotations = [2, 5, 8, 1, 4, 7, 0, 3, 6]
        for i in range(9):
                new_board.append(game_board[rotations[i]])
        return new_board
        
def printBoard(j):
    print(j[6] + "|" + j[7] + "|" + j[8])
    print("-" * 5)
    print(j[3] + "|" + j[4] + "|" + j[5])
    print("-" * 5)
    print(j[0] + "|" + j[1] + "|" + j[2])
        

game_board = ["-"]*9

for i in range(4):
    printBoard(game_board)
    print("\n")
    game_board[playRandomMove(game_board)] = "X"
    printBoard(game_board)
    print("\n")
    game_board[getComputerMove(game_board)] = "O"

printBoard(game_board)
print("\n")
game_board = rotateBoard(game_board)
printBoard(game_board)
print("\n")
game_board = rotateBoard(game_board)
printBoard(game_board)
print("\n")

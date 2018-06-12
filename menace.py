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
# beads
# 4 for first move
# 3 for second
# 3 for third
# 2 for fourth
# 1 for last

def checkUniqueMove(game_board):
        # Returns -1 if the move is unique, otherwise returns the index in the aray
        # rotations
        test_board = game_board
        k = 0
        for i in boxes:
        	for j in range(4):# Checking each reflection and rotation
        		for l in range(2):
        			if test_board == i[0]:
        				return k
        			test_board = reflectBoard_y(test_board)
        		test_board = rotateBoard(test_board)
        	k += 1
        return -1 
        	

def menacePlayMove(game_board, move_num):
        # Returns a new board with a move randomly chosen from a matchbox
        new_board = game_board
        unique_index = checkUniqueMove(game_board)
        if unique_index == -1:
        	# If the box doesn't exist then create it
                beads = []
                for i in range(9):
                	beads[i] = move_num%2 + 1 # Adjust the number of beads for the move
                boxes.append([game_board, beads])
                unique_index = len(boxes)
                
        boxes_used.append(unique_index)
        
        # TODO: Play move
        
def trainMenace(mode, first):
	game_board = ["-"]*9
	if mode == 0:# Against Random
		
	elif mode == 1:# Against Optimal
	
	elif mode == 2:# Against Human
	
	elif mode == 3:# Against Itself
            
def rotateBoard(game_board):
        # Returns a new board that is rotated clockwise 90 degrees
        new_board = []
        rotations = [2, 5, 8, 1, 4, 7, 0, 3, 6]
        for i in range(9):
                new_board.append(game_board[rotations[i]])
        return new_board

def reflectBoard_y(game_board):
        # Returns a new board that is reflected in the y-axis
        new_board = []
        reflection = [2, 1, 0, 5, 4, 3, 8, 7, 6]
        for i in range(9):
                new_board.append(game_board[reflection[i]])
        return new_board

def reflectBoard_x(game_board):
        # Returns a new board reflected in the x-axis
        new_board = []
        new_board = reflectBoard_y(rotateBoard(rotateBoard(game_board)))
        return new_board

def checkWinningMove(game_board):
        winning_pos = [[6, 7, 8],# Horizontal
                       [3, 4, 5],
                       [0, 1, 2],
                       [6, 3, 0],# Vertical
                       [7, 4, 1],
                       [8, 5, 2],
                       [6, 4, 2],# Diagonal
                       [8, 4, 0],]
        
        j = game_board
        for i in winning_pos:
                if j[i[0]] != "-" and j[i[0]] == j[i[1]] == j[i[2]]:
                        return True
        return False

def askForMove(board):
    printBoard(board)
    while True:
        pos = input("Where would you like to place your symbol (1 - 9): ") - 1
        if pos > 8 or pos < 0:
            print("Not valid")
            continue
        elif board[pos] != "-":
            print("Something is already there")
            continue
        return pos

def printBoard(j):
    # Prints the board in a more easy to read format
    print(j[6] + "|" + j[7] + "|" + j[8])
    print("-" * 5)
    print(j[3] + "|" + j[4] + "|" + j[5])
    print("-" * 5)
    print(j[0] + "|" + j[1] + "|" + j[2])

def main():
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

move_num = 4
f = open("MENACE_LOG.txt", "w")        
game_board = ["-"]*9
boxes_used = []
#boxes = [[["-", "-", "-", "-", "-", "-", "-", "-", "-"], {"0":4, "1":4, "2":4, "3":4, "4":4, "5":4, "6":4, "7":4, "8":4}]]
boxes = [[["-", "-", "-", "-", "-", "-", "-", "-", "-"], [4, 4, 4, 4, 4, 4, 4, 4, 4]]]
f.close()

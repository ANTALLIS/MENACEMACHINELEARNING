import random
from tttAI import *

def playRandomMove(game_board):
    # Chooses a random position on the board and returns the position(0-8); Returns False if the board is full
    play_pos = []
    
    for i in range(9):# Checking for free positions
        if game_board[i] == "-":
            play_pos.append(i)# If found, adds them to the list
    
    random.shuffle(play_pos)# Choose a random postition from the list
    if len(play_pos) == 0:
        print("Game board full.")
		return False
    return play_pos[0]

# beads(playing first):
# 4 for first move
# 3 for second
# 3 for third
# 2 for fourth
# 1 for last

def checkUniqueMove(game_board):
        # Returns False if the move is unique, otherwise returns the index in the array
        test_board = game_board.copy()
        k = 0
        for i in boxes:
        	for j in range(4):# Checking each reflection and rotation
        		for l in range(2):
        			if test_board == i[0]:
        				return k
        			test_board = reflectBoard_y(test_board)
        		test_board = rotateBoard(test_board)
        	k += 1
        return False
        	

def menacePlayMove(game_board, move_num):
        # Returns a new board with a move randomly chosen from a matchbox
        new_board = game_board.copy()
        unique_index = checkUniqueMove(game_board)
        if unique_index == False:
        	# The bead box doesn't exist so create it
                beads = []
                for i in range(9):
                	beads[i] = beadnum(move_num) # Adjust the number of beads for the move
                boxes.append([game_board, beads])
                unique_index = len(boxes)
                
        boxes_used.append(unique_index)
        
        # TODO: Play move

def beadnum(turn):
	return 4

def findFreePositions(game_board):
	# Looks for free positions("-") and returns a list of them; Returns False if the board is full
	free_pos_array = []
	for i, symbol in enumerate(game_board):
		if symbol == "-"
			free_pos_array.add(i)
	if len(free_pos_array) == 0:
		return False
	return free_pos_array

def trainMenace(mode, first):
	game_board = ["-"]*9
	winflag = 0
	if mode == 0:# Against Random
		while True:
			playMenace(game_board)
			winflag = checkWin(game_board)
			if winflag: break

			playRandom(game_board)
			winflag = checkWin(game_board)
			if winflag: break
			
	elif mode == 1:# Against Optimal
		print("Not yet implemented.")
		pass
	elif mode == 2:# Against Human
		print("Not yet implemented.")
		pass
	elif mode == 3:# Against Itself
		print("Not yet implemented.")
		pass

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
		# Returns the row and column of the winning move if there is one, otherwise returns False
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
                        return i
        return False

def askForMove(board):
    printBoard(board)
    while True:
        pos = input("Where would you like to place your symbol (1 - 9): ") - 1
        if pos > 8 or pos < 0:
            print("Not valid")
        elif board[pos] != "-":
            print("Something is already there")
		else:
        	return pos

def printBoard(j):
    # Prints the board in a more easy to read format
    print(j[6] + "|" + j[7] + "|" + j[8])
    print("-" * 5)
    print(j[3] + "|" + j[4] + "|" + j[5])
    print("-" * 5)
    print(j[0] + "|" + j[1] + "|" + j[2])
	print("")

def main():# Main game loop (?)
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

move_num = 4# TODO: Replace with automatic detection of end of game
WIN_REWARD = 3
LOSS_PENALTY = -1
DRAW_REWARD = 0

f = open("MENACE_LOG.txt", "w")# For debugging    
game_board = ["-"]*9# New blank game board
boxes_used = []# (?)
#boxes = [[["-", "-", "-", "-", "-", "-", "-", "-", "-"], {"0":4, "1":4, "2":4, "3":4, "4":4, "5":4, "6":4, "7":4, "8":4}]]
boxes = [[["-", "-", "-", "-", "-", "-", "-", "-", "-"], [4, 4, 4, 4, 4, 4, 4, 4, 4]]]
f.close()

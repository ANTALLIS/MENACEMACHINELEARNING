import random
import tttAI

def playRandomMove(game_board):
	# Chooses a random position on the board and returns a number
	play_pos = []
	
	for i in range(9):
		if game_board[i] == "-":
			play_pos.append(i)
	
	random.shuffle(play_pos)
	
	return play_pos[0]

def printBoard(j):
	print(j[6] + "|" + j[7] + "|" + j[8])
	print("-" * 5)
	print(j[3] + "|" + j[4] + "|" + j[5])
	print("-" * 5)
	print(j[0] + "|" + j[1] + "|" + j[2])
		

game_board = ["-"]*9

for i in range(12):
	printBoard(game_board)
	print("\n")
	game_board[playRandomMove(game_board)] = "X"
	printBoard(game_board)
	print("\n")
	game_board[tttAI.getComputerMove(game_board)] = "O"

# NOT MINE
# Code from https://mblogscode.wordpress.com/2016/06/03/python-naughts-crossestic-tac-toe-coding-unbeatable-ai/

def checkWin(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or  # H top
            (b[3] == m and b[4] == m and b[5] == m) or  # H mid
            (b[6] == m and b[7] == m and b[8] == m) or  # H bot
            (b[0] == m and b[3] == m and b[6] == m) or  # V left
            (b[1] == m and b[4] == m and b[7] == m) or  # V centre
            (b[2] == m and b[5] == m and b[8] == m) or  # V right
            (b[0] == m and b[4] == m and b[8] == m) or  # LR diag
            (b[2] == m and b[4] == m and b[6] == m))  # RL diag

def checkDraw(b):
    return '-' not in b

def getBoardCopy(b):
    # Make a duplicate of the board. When testing moves we don't want to 
    # change the actual board
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

def testWinMove(b, mark, i):
    # b = the board
    # mark = 0 or X
    # i = the square to check if makes a win 
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return checkWin(bCopy, mark)

def testForkMove(b, mark, i):
    # Determines if a move opens up a fork
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if testWinMove(bCopy, mark, j) and bCopy[j] == ' ':
            winningMoves += 1
    return winningMoves >= 2

def getComputerMove(b):
    # Check computer win moves
    for i in range(0, 9):
        if b[i] == '-' and testWinMove(b, 'X', i):
            return i
    # Check player win moves
    for i in range(0, 9):
        if b[i] == '-' and testWinMove(b, 'O', i):
            return i
    # Check computer fork opportunities
    for i in range(0, 9):
        if b[i] == '-' and testForkMove(b, 'X', i):
            return i
    #  Check player fork opportunities
    for i in range(0, 9):
        if b[i] == '-' and testForkMove(b, 'O', i):
            return i
    # Play a corner
    for i in [0, 2, 6, 8]:
        if b[i] == '-':
            return i
    # Play center
    if b[4] == '-':
        return 4
    #Play a side
    for i in [1, 3, 5, 7]:
        if b[i] == '-':
            return i

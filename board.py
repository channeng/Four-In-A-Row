import copy
import time

colHeaders = [1,2,3,4,5,6,7]
r0 = ["-","-","-","-","-","-","-"]

r1 = [2,0,1,1,1,0,0]
r2 = [2,2,2,2,0,1,0]
r3 = [2,1,2,1,2,1,2]
r4 = [2,0,0,1,1,1,1]
r5 = [0,0,0,0,0,1,0]
r6 = [0,0,0,0,0,0,0]
board = [r1,r2,r3,r4,r5,r6]


#UI elements

def printboard(board):
	for i in range(50):
		print
	for r in board:
		print "|",
		for i in r:
			print i,
		print "|"
	print "-",
	for r in r0:
		print r,
	print "-"
	print " ",
	for r in colHeaders:
		print r,
	print " "
	print "---- COLUMN -----"
	print

def animateBoard(playerx,board,pcol):
	board2 = copy.deepcopy(board)
	for rowindex in range(len(board)):
		if board2[rowindex][pcol] == 0:
			if rowindex == 0:
				pass
			else: board2[rowindex-1][pcol] = 0
			board2[rowindex][pcol] = playerx
			printboard(board2)
			print
			print
			time.sleep(0.12)
		else: break

#INTERACTIVE elements

def checkcol(inputt,playerx,board):
	if inputt == "1" or inputt == "2" or inputt == "3" or inputt == "4" or inputt == "5" or inputt == "6" or inputt == "7":
		return int(inputt)
	else:
		printboard(board)
		print "Player "+str(playerx)+"'s turn"
		inputt2 = raw_input("Please enter only 1/2/3/4/5/6/7 \n > ")
		return checkcol(inputt2,playerx,board)

def fillBoard(playerx,board):
	pcol = checkcol(str(raw_input("Which column? (1/2/3/4/5/6/7)\n > ")),playerx,board)-1
	animateBoard(playerx,board,pcol)
	for r in reversed(board):
		if r[pcol] == 0:
			r[pcol] = playerx
			break
	else:
		printboard(board)
		print "Player "+str(playerx)+": "+"Column is filled! Please try another column!"
		fillBoard(playerx,board)

#WIN CRITERIA

def check_row_win(rowindex,board):
	for i in range(4):
		if board[rowindex][i]*board[rowindex][i+1]*board[rowindex][i+2]*board[rowindex][i+3] == 1 or board[rowindex][i]*board[rowindex][i+1]*board[rowindex][i+2]*board[rowindex][i+3] == 16:
			return True
	else: return False

def check_col_win(colindex,board):
	for i in range(3):
		if board[i][colindex]*board[i+1][colindex]*board[i+2][colindex]*board[i+3][colindex] == 1 or board[i][colindex]*board[i+1][colindex]*board[i+2][colindex]*board[i+3][colindex] == 16:
			return True
	else: return False

#GAME PROGRESSION

def Pturn(playerx, board):
	print "Player "+str(playerx)+"'s turn"
	fillBoard(playerx,board)
	printboard(board)

def start_game(board):
	printboard(board)
	i = 0
	while i<21:
		Pturn(1,board)
		Pturn(2,board)
		i += 1
	print "---- GAME OVER ----"
	print "    It's a draw!   "


print check_col_win(5,board)

import copy
import time

colHeaders = [1,2,3,4,5,6,7]
r0 = ["-","-","-","-","-","-","-"]

r1 = [0,0,0,0,0,0,0]
r2 = [0,0,0,0,0,0,0]
r3 = [0,0,0,0,0,0,0]
r4 = [0,0,0,0,0,0,0]
r5 = [0,0,0,0,0,0,0]
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

def row_win(board):
	for rowindex in range(len(board)):
		if check_row_win(rowindex,board):
			return True
		else: pass
	else: return False

def col_win(board):
	for colindex in range(len(board[0])):
		if check_col_win(colindex,board):
			return True
		else: pass
	else: return False

def diagmain_win(board,dirx):
	board2 = copy.deepcopy(board)
	i = 0
	if dirx == "left":
		pass
	else: 
		for r in board2:
			r.reverse()

	for colindex in range(3):
		if board2[i][colindex]*board2[i+1][colindex+1]*board2[i+2][colindex+2]*board2[i+3][colindex+3] == 1 or board2[i][colindex]*board2[i+1][colindex+1]*board2[i+2][colindex+2]*board2[i+3][colindex+3] == 16:
			return True
		else: 
			i+=1
	else:
		return False

def diagr2_win(board,dirx):
	board2 = copy.deepcopy(board)
	i = 1
	if dirx == "left":
		pass
	else: 
		for r in board2:
			r.reverse()

	for colindex in range(2):
		if board2[i][colindex]*board2[i+1][colindex+1]*board2[i+2][colindex+2]*board2[i+3][colindex+3] == 1 or board2[i][colindex]*board2[i+1][colindex+1]*board2[i+2][colindex+2]*board2[i+3][colindex+3] == 16:
			return True
		else: 
			i+=1
	else:
		return False

def diagr3_win(board,dirx):
	board2 = copy.deepcopy(board)
	i = 2
	if dirx == "left":
		pass
	else: 
		for r in board2:
			r.reverse()
	
	if board2[i][0]*board2[i+1][1]*board2[i+2][2]*board2[i+3][3] == 1 or board2[i][0]*board2[i+1][1]*board2[i+2][2]*board2[i+3][3] == 16:
		return True
	else: 
		return False

def diagc2_win(board,dirx):
	board2 = copy.deepcopy(board)
	i = 1
	if dirx == "left":
		pass
	else: 
		for r in board2:
			r.reverse()

	for rowindex in range(3):
		if board2[rowindex][i]*board2[rowindex+1][i+1]*board2[rowindex+2][i+2]*board2[rowindex+3][i+3] == 1 or board2[rowindex][i]*board2[rowindex+1][i+1]*board2[rowindex+2][i+2]*board2[rowindex+3][i+3] == 16:
			return True
		else: 
			i+=1
	else:
		return False

def diagc3_win(board,dirx):
	board2 = copy.deepcopy(board)
	i = 2
	if dirx == "left":
		pass
	else: 
		for r in board2:
			r.reverse()

	for rowindex in range(2):
		if board2[rowindex][i]*board2[rowindex+1][i+1]*board2[rowindex+2][i+2]*board2[rowindex+3][i+3] == 1 or board2[rowindex][i]*board2[rowindex+1][i+1]*board2[rowindex+2][i+2]*board2[rowindex+3][i+3] == 16:
			return True
		else: 
			i+=1
	else:
		return False

def diagc4_win(board,dirx):
	board2 = copy.deepcopy(board)
	i = 3
	if dirx == "left":
		pass
	else: 
		for r in board2:
			r.reverse()
	
	if board2[0][i]*board2[1][i+1]*board2[2][i+2]*board2[3][i+3] == 1 or board2[0][i]*board2[1][i+1]*board2[2][i+2]*board2[3][i+3] == 16:
		return True
	else: 
		return False

def diag_win_left(board):
	dirx = "left"
	if diagmain_win(board,dirx) or diagr2_win(board,dirx) or diagr3_win(board,dirx) or diagc2_win(board,dirx) or diagc3_win(board,dirx) or diagc4_win(board,dirx):
		return True
	else: 
		return False

def diag_win_right(board):
	dirx = "right"
	if diagmain_win(board,dirx) or diagr2_win(board,dirx) or diagr3_win(board,dirx) or diagc2_win(board,dirx) or diagc3_win(board,dirx) or diagc4_win(board,dirx):
		return True
	else: 
		return False

def diag_win(board):
	if diag_win_right(board) or diag_win_left(board):
		return True
	else:
		return False

def is_win(board):
	if row_win(board) or col_win(board) or diag_win(board):
		return True
	else:
		return False

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
		if is_win(board):
			print "Player 1 wins!"
			break
		else: pass
		Pturn(2,board)
		if is_win(board):
			print "Player 2 wins!"
			break
		else: pass
		i += 1
		if i == 20:
			print "    It's a draw!   "
			break
	print "---- GAME OVER ----"

start_game(board)

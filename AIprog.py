import scoresys
import copy

r1 = [0,0,0,0,0,0,0]
r2 = [0,0,0,0,1,0,0]
r3 = [1,1,0,0,0,2,0]
r4 = [1,2,1,1,2,1,2]
r5 = [2,2,1,1,1,2,2]
r6 = [2,1,2,1,1,1,2]

board = [r1,r2,r3,r4,r5,r6]

# BOARD-to-ARRAY transformation

def read_board(playerx,board):
	board2 = copy.deepcopy(board)
	for rowindex in range(len(board)):
		for i in range(len(board[rowindex])):
			if board[rowindex][i] == playerx:
				board2[rowindex][i] = 1
			elif board[rowindex][i] == 0:
				pass
			else:
				board2[rowindex][i] = "X"
	return board2

def get_row_result(playerx,board,rowindex):
	result =""
	for i in range(len(board[rowindex])):
		result = result + str(board[rowindex][i])
	return result

def get_array_result(array):
	result =""
	for i in range(len(array)):
		result = result + str(array[i])
	return result

def get_board_result(playerx,board):
	board2 = []
	for rowindex in range(len(board)):
		board2.append(get_row_result(playerx,board,rowindex))
	return board2

def rowboard(playerx,board):
	rowboard = read_board(playerx,board)
	for rowindex in range(4):
		for i in range(len(board[rowindex])):
			if board[rowindex][i] == 0 and board[rowindex+1][i] == 0:
				if board[rowindex][i] == 0 and board[rowindex+1][i] ==0 and board[rowindex+2][i] == 0:
					rowboard[rowindex][i] = "X"
				else: 
					rowboard[rowindex][i] = "P"
			else: pass
	for i in range(len(rowboard[4])):
		if board[4][i] == 0 and board[5][i] == 0:
			rowboard[4][i] = "P"
		else: pass

	return get_board_result(playerx,rowboard)

def colboard(playerx,board):
	colboard = read_board(playerx,board)
	column = []
	for colindex in range(len(board[0])):
		result = []
		for rowindex in range(len(board)):
			result.append(colboard[rowindex][colindex])
		column.append(get_array_result(result))
	return column

def get_diag(board,diag_type,row_col,diagindex):   # DIAG_TYPE: LEFT=0 , RIGHT=1 |  ROW_COL: ROW=0,COL=1
	diag = []
	board2 = copy.deepcopy(board)
	if diag_type == 0:
		if row_col == 0:
			for i in range(7-diagindex):
				diag.append(board2[diagindex-1+i][i])
			return diag
		elif row_col == 1:
			for i in range(7-diagindex):
				diag.append(board2[i][diagindex+i])
			return diag
	elif diag_type == 1:
		for i in range(len(board)):
			board2[i] = board[i][::-1]
		if row_col == 0:
			for i in range(7-diagindex):
				diag.append(board2[diagindex-1+i][i])
			return diag
		elif row_col == 1:
			for i in range(7-diagindex):
				diag.append(board2[i][diagindex+i])
			return diag

def get_diagboard(playerx,board,diag_type):
	board2 = read_board(playerx,board)
	leftdiagboard = []
	for i in range(3):
		leftdiagboard.append(get_diag(board2,diag_type,1,3-i))
	for i in range(6):
		leftdiagboard.append(get_diag(board2,diag_type,0,i+1))
	return leftdiagboard

def diagboard(playerx,board,diag_type):
	board2 = get_diagboard(playerx,board,diag_type)
	leftboard = get_diagboard(playerx,board,diag_type)

	for i in range(4):
		if board2[i+2][len(board2[i+2])-2] == 0 and board2[i+3][len(board2[i+3])-1] == 0:
			leftboard[i+2][len(leftboard[i+2])-2] = "P"
		else: pass
	if board2[1][4] == 0 and board2[2][5] == 0:
			leftboard[1][4] = "P" 
	else: pass

	for i in range(2):
		x = i+3
		for i in range(4):
			if board2[i+2][len(board2[i+2])-x] == 0 and board2[i+3][len(board2[i+3])-(x-1)] == 0:
				if board2[i+2][len(board2[i+2])-x] == 0 and board2[i+3][len(board2[i+3])-(x-1)] ==0 and board2[i+4][len(board2[i+4])-(x-2)] == 0:
					leftboard[i+2][len(leftboard[i+2])-x] = "X"
				else: 
					leftboard[i+2][len(leftboard[i+2])-x] = "P"
			else: pass
	
	for i in range(3):
		x = 5
		if board2[i+2][len(board2[i+2])-x] == 0 and board2[i+3][len(board2[i+3])-(x-1)] == 0:
			if board2[i+2][len(board2[i+2])-x] == 0 and board2[i+3][len(board2[i+3])-(x-1)] ==0 and board2[i+4][len(board2[i+4])-(x-2)] == 0:
				leftboard[i+2][len(leftboard[i+2])-x] = "X"
			else: 
				leftboard[i+2][len(leftboard[i+2])-x] = "P"
		else: pass
	
	for i in range(2):
		x = 6
		if board2[i+2][len(board2[i+2])-x] == 0 and board2[i+3][len(board2[i+3])-(x-1)] == 0:
			if board2[i+2][len(board2[i+2])-x] == 0 and board2[i+3][len(board2[i+3])-(x-1)] ==0 and board2[i+4][len(board2[i+4])-(x-2)] == 0:
				leftboard[i+2][len(leftboard[i+2])-x] = "X"
			else: 
				leftboard[i+2][len(leftboard[i+2])-x] = "P"
		else: pass

	for i in range(2):
		for x in range(4):
			if board2[i][x] == 0 and board2[i+1][x+1] == 0:
				if board2[i][x] == 0 and board2[i+1][x+1] ==0 and board2[i+2][x+2] == 0:
					leftboard[i][x] = "X"
				else: 
					leftboard[i][x] = "P"
			else: pass

	return get_board_result(playerx,leftboard)

def print_results(playerx,board):
	print "COLBOARD"
	for i in colboard(playerx,board):
		print i
	print
	print

	print "ROWBOARD"
	for i in rowboard(playerx,board):
		print i
	print
	print

	print "LEFT DIAGBOARD"
	for i in diagboard(playerx,board,0):
		print i
	print
	print

	print "RIGHT DIAGBOARD"
	for i in diagboard(playerx,board,1):
		print i
	print
	print

# SCORING

def easyscore(playerx,board,index,row_col):   # col : row_col = 1, row : row_col = 0
	board2 = []

	if row_col == 0:
		board2 = rowboard(playerx,board)
	elif row_col == 1:
		board2 = colboard(playerx,board)

	row_score = []

	base_score = [0]
	for i in scoresys.scoreboard[0]:
		if i[0] in board2[index]:
			base_score.append(i[1])
	row_score.append(max(base_score))

	extra_1_space_score = [0]
	for i in scoresys.scoreboard[1]:
		if i[0] in board2[index]:
			extra_1_space_score.append(i[1])
	row_score.append(max(extra_1_space_score))

	extra_2_space_score = [0]
	for i in scoresys.scoreboard[2]:
		if i[0] in board2[index]:
			extra_2_space_score.append(i[1])
	row_score.append(max(extra_2_space_score))

	return sum(row_score)

def countXs(x,result):    # Eg. Result  = rowboard(1,board)[i] or scoresys.score4char[i]
	before = len(result)
	result2 = []
	for i in range(before):
		if result[i] == str(x):
			pass
		else: 
			result2.append(result[i])
	after = len(result2)
	return before - after

def pscore(board_result,rowindex):
	pscore = []
	for scorechar in scoresys.scoreboard:
		charscore = []
		for i in range(len(scorechar)):
			score = 0
			if scorechar[i][0] in board_result[rowindex]:
				score = scorechar[i][1]
			else:
				replaced = board_result[rowindex].replace("P","0")
				countPs = countXs("P",board_result[rowindex])
				count0s = countXs("0",scorechar[i][0])
				if scorechar[i][0] in replaced and countPs <= count0s:
					score = scorechar[i][1]/(countPs+1.00)
				else: score =0
			charscore.append(score)
		pscore.append(max(charscore))
	return sum(pscore)

def colscore(playerx,board):
	colscore = 0
	for i in range(len(colboard(playerx,board))):
		colscore += easyscore(playerx,board,i,1)
	return colscore

def rowscore(playerx,board):
	board_result = rowboard(playerx,board)
	rowscore = easyscore(playerx,board,5,0)    # easy score for r6 of board
	for i in range(len(board_result)-1):    #pscore for rows 1 - 5
		rowscore += pscore(board_result,i)
	return rowscore

def leftdiagscore(playerx,board):
	board_result = diagboard(playerx,board,0)
	rowscore = 0    # easy score for r6 of board
	for i in range(len(board_result)):    #pscore for rows 1 - 5
		rowscore += pscore(board_result,i)
	return rowscore

def rightdiagscore(playerx,board):
	board_result = diagboard(playerx,board,1)
	rowscore = 0    # easy score for r6 of board
	for i in range(len(board_result)):    #pscore for rows 1 - 5
		rowscore += pscore(board_result,i)
	return rowscore

def allscore(playerx,board):
	allscore =[colscore(playerx,board),rowscore(playerx,board),leftdiagscore(playerx,board),rightdiagscore(playerx,board)]
	return sum(allscore)

# RUN THROUGH ALL SCENARIOS

def AIprog(playerx,board):
	table = []
	for colindex in range(len(board[0])):
		board2 = copy.deepcopy(board)
		for r in reversed(board2):
			if r[colindex] == 0:
				r[colindex] = playerx
				break
		else: pass
		table.append([colindex+1,allscore(playerx,board2)])
	
	scores = []
	for i in range(len(table)):
		scores.append(table[i][1])
	topscore = max(scores)

	best_col = 0
	for i in range(len(table)):
		if table[i][1]==topscore:
			best_col += int(table[i][0])
	return best_col




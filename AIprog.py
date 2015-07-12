import scoresys
import copy

r1 = [0,0,0,0,0,0,0]
r2 = [0,2,2,0,0,0,0]
r3 = [0,0,0,0,2,0,0]
r4 = [0,1,1,0,1,0,0]
r5 = [0,0,0,1,0,0,0]
r6 = [2,0,1,1,0,0,2]

board = [r1,r2,r3,r4,r5,r6]

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


def easyscore(playerx,board,rowindex):
	board2 = rowboard(playerx,board)
	row_score = []

	base_score = [0]
	for i in scoresys.scoreboard[0]:
		if i[0] in board2[rowindex]:
			base_score.append(i[1])
	row_score.append(max(base_score))

	extra_1_space_score = [0]
	for i in scoresys.scoreboard[1]:
		if i[0] in board2[rowindex]:
			extra_1_space_score.append(i[1])
	row_score.append(max(extra_1_space_score))

	extra_2_space_score = [0]
	for i in scoresys.scoreboard[2]:
		if i[0] in board2[rowindex]:
			extra_2_space_score.append(i[1])
	row_score.append(max(extra_2_space_score))

	return sum(row_score)

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

def leftdiagboard(playerx,board):
	leftdiagboard = []
	for i in range(3):
		leftdiagboard.append(get_diag(read_board(playerx,board),0,1,3-i))
	for i in range(3):
		leftdiagboard.append(get_diag(read_board(playerx,board),0,0,i+1))
	return leftdiagboard

def rightdiagboard(playerx,board):
	rightdiagboard = []
	for i in range(3):
		rightdiagboard.append(get_diag(read_board(playerx,board),1,1,3-i))
	for i in range(3):
		rightdiagboard.append(get_diag(read_board(playerx,board),1,0,i+1))
	return rightdiagboard
	

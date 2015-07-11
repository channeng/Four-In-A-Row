import scoresys

r1 = [0,0,0,0,0,0,0]
r2 = [0,0,0,0,0,0,0]
r3 = [0,0,0,2,1,1,0]
r4 = [0,0,0,1,2,1,0]
r5 = [1,0,1,2,1,2,0]
r6 = [2,0,1,1,1,0,2]

board = [r1,r2,r3,r4,r5,r6]

def getresult(playerx,board,rowindex):
	result =""
	for i in range(len(board[rowindex])):
		if board[rowindex][i] == playerx:
			board[rowindex][i] = 1
		elif board[rowindex][i] == 0:
			pass
		else:
			board[rowindex][i] = "X"
		result = result + str(board[rowindex][i])
	return result

def easyscore(playerx,board,rowindex):
	row_score = []
	base_score = [0]
	for i in scoresys.scoreboard[0]:
		if i[0] in getresult(playerx,board,rowindex):
			base_score.append(i[1])
	row_score.append(max(base_score))

	extra_1_space_score = [0]
	for i in scoresys.scoreboard[1]:
		if i[0] in getresult(playerx,board,rowindex):
			extra_1_space_score.append(i[1])
	row_score.append(max(extra_1_space_score))

	extra_2_space_score = [0]
	for i in scoresys.scoreboard[2]:
		if i[0] in getresult(playerx,board,rowindex):
			extra_2_space_score.append(i[1])
	row_score.append(max(extra_2_space_score))

	return sum(row_score)

def pscore(playerx,board,rowindex):
	row_score = []
	base_score = [0]
	for i in scoresys.scoreboard[0]:
		if i[0] in getresult(playerx,board,rowindex):
			base_score.append(i[1])
	row_score.append(max(base_score))

	extra_1_space_score = [0]
	for i in scoresys.scoreboard[1]:
		if i[0] in getresult(playerx,board,rowindex):
			extra_1_space_score.append(i[1])
	row_score.append(max(extra_1_space_score))

	extra_2_space_score = [0]
	for i in scoresys.scoreboard[2]:
		if i[0] in getresult(playerx,board,rowindex):
			extra_2_space_score.append(i[1])
	row_score.append(max(extra_2_space_score))

	return sum(row_score)





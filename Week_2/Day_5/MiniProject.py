def display_board(board):
	print("*****************")
	for row in board :
		print(f"*   {row[0]} | {row[1]} | {row[2]}   *")
		print("*  ---|---|---  *")
	print("*****************")

def player_input(player, board):
	allowed_input = ["1", "2", "3"]
	while True:
		row = input("Enter row(1-3): ")
		column  = input("Input column(1-3): ")
		if row in allowed_input and column in allowed_input:
			board[int(row)-1][int(column)-1] = player
			return 


def check_win(player, board):
	lines_to_check = []

	# get all rows and columns to check
	for index in range(3): 
		row = board[index]
		column = [board[0][index], board[1][index], board[2][index]]
		lines_to_check.extend([row, column])
	
	# get both diagonals to check
	diagonal1 = [board[0][0], board[1][1], board[2][2]]
	diagonal2 = [board[0][2], board[1][1], board[2][0]]
	lines_to_check.extend([diagonal1, diagonal2])

	#check all rows, columns and diagonals for a winner
	for line in lines_to_check:
		if line[0] != " " and len(set(line)) == 1:
			return player
	
	#check if the game ends in a tie
	for row in board:
		for cell in row:
			if cell == " ":
				return ""
	return "tie"


def play():
	board = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "]
]
	current_player = 'X' # X or O
	winner_player = ''

	print("Welcome to TIC TAC TOE!")

	while not winner_player:
		display_board(board)
		print(f"Player {current_player}'s turn...")
		player_input(current_player, board)
		winner_player = check_win(current_player, board)
		current_player = "O" if current_player == "X" else "X"

	print('The game ends...')
	display_board(board)
	if winner_player == "tie":
		print("in a tie :(")
	else:
		print(f"And {winner_player} wins!!!")
		

play()
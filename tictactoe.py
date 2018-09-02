import random

def clear_screen():
	print("\n" * 100)

def display_board(board):
	'''
	Displays ASCII tic-tac-toe board.
	'''
	for slot in range(1,10):
		print(' {} '.format(board[slot]), end='')

		# if slot is a multiple of three, advance to the next line
		if slot % 3 == 0:
			# only display horizontal separators after the first two rows
			if slot <= 6:
				print("\n" + '-' * 11)
			else:    # otherwise advance to the next line
				print("")
		else:    # display vertical separator
			print('|', end='')

def place_marker(board, marker, position):
	'''
	Places a maker on the board at the specified position.
	'''
	board[position] = marker

def win_check(board, mark):
	'''
	Checks the board to see if the given marker has won the game.
	'''
	wins = [(1,2,3), (4,5,6),(7,8,9),
			(1,4,7), (2,5,8),(3,6,9),
			(1,5,9),(3,5,7)]
	
	for x, y, z in wins:
		if board[x] == board[y] == board[z] == mark:
			return True

	return False

def choose_first():
	'''
	Determine which player goes first.
	'''
	if random.randint(0, 1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

def space_check(board, position):
	'''
	Determines if the position on the board is empty.
	'''
	return board[position] == ' '

def full_board_check(board):
	'''
	Determines if all available moves have been taken on the board.
	'''
	return ' ' not in board

def player_input():
	'''
	Prompts first player for their input. (X or O)
	'''
	marker = ''
	
	while marker not in ('X', 'O'):
		marker = input("Please pick a marker 'X' or 'O': ")
		marker = marker.upper().strip()

	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O', 'X')

def player_choice(board):
	'''
	Prompt the current player for their selection.
	'''
	position = int(input('Please enter a number (1-9): '))

	while not space_check(board, position):
		position = int(input('That position has been taken. Please enter a number: '))

	return position

def replay():
	'''
	Ask the player if they want to play again.
	'''
	selection = input("Play again? [y/n] ")
	selection = selection.lower().strip()
	return selection == 'y'

print('Welcome to Tic Tac Toe!')

while True:
	# assign markers to players
	player1_marker, player2_marker = player_input()

	# create a new board
	board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

	# determine who will go first
	turn = choose_first()
	print('{} will go first.\n'.format(turn))

	while True:

		if turn == 'Player 1':
			# get the player's move
			position = player_choice(board)

			# update the board
			place_marker(board, player1_marker, position)
			display_board(board)

			# check for a winner
			if win_check(board, player1_marker):
				print('Player 1 wins!')
				break
			elif full_board_check(board):
				print('The game is a draw!')
				break
			else:
				turn = 'Player 2'
		else:
			# get the player's move
			position = player_choice(board)

			# update the board
			place_marker(board, player2_marker, position)
			display_board(board)

			# check for a winner
			if win_check(board, player2_marker):
				print('Player 2 wins!')
				break
			elif full_board_check(board):
				print('The game is a draw!')
				break
			else:
				turn = 'Player 1'
		
	if not replay():
		break

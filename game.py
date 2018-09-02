import random
import tictactoe

def choose_first():
	'''
	Determine which player goes first.
	'''
	if random.randint(0, 1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'

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

	while not board.space_check(position):
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
	board = tictactoe.Board()

	# determine who will go first
	currentPlayer = choose_first()
	print('{} will go first.\n'.format(currentPlayer))
	print(board)
	
	while True:
		# determine which player's marker to place on the board
		if currentPlayer == 'Player 1':
			marker = player1_marker
		else:
			marker = player2_marker

		# get the player's move
		position = player_choice(board)
		print('')

		# update the board
		board.place_marker(marker, position)
		print(board)

		# check for a winner
		if board.win_check(marker):
			print('{} wins!'.format(currentPlayer))
			break
		elif board.is_full():
			print('The game is a draw!')
			break
		else:
			if currentPlayer == 'Player 1':
				currentPlayer = 'Player 2'
			else:
				currentPlayer = 'Player 1'
		
	if not replay():
		break
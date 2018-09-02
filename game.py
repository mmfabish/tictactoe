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
	turn = choose_first()
	print('{} will go first.\n'.format(turn))

	while True:

		if turn == 'Player 1':
			# get the player's move
			position = player_choice(board)

			# update the board
			board.place_marker(player1_marker, position)
			print(board)

			# check for a winner
			if board.win_check(player1_marker):
				print('Player 1 wins!')
				break
			elif board.is_full():
				print('The game is a draw!')
				break
			else:
				turn = 'Player 2'
		else:
			# get the player's move
			position = player_choice(board)

			# update the board
			board.place_marker(player2_marker, position)
			print(board)

			# check for a winner
			if board.win_check(player2_marker):
				print('Player 2 wins!')
				break
			elif board.is_full():
				print('The game is a draw!')
				break
			else:
				turn = 'Player 1'
		
	if not replay():
		break
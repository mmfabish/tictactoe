import tictactoe

def replay():
	'''
	Ask the player if they want to play again.
	'''
	selection = input("Play again? [y/n] ")
	selection = selection.lower().strip()
	return selection == 'y'

print('Welcome to Tic Tac Toe!')

game = tictactoe.Game()

while True:
	# play a game of Tic Tac Toe
	game.play()

	# prompt the user to play again
	if not replay():
		break
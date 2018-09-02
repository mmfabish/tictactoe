import random

class Board(object):
    '''
    Abstraction of a Tic Tac Toe board
    '''
    def __init__(self):
        self.clear()

    def __str__(self):
        '''
        Displays ASCII tic-tac-toe board.
        '''
        output = """ {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}
        """.format(self._board[1], self._board[2], self._board[3], 
        self._board[4], self._board[5], self._board[6], 
        self._board[7], self._board[8], self._board[9])

        return output

    def clear(self):
        '''
        Clears the board.
        '''
        self._board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '] 

    def is_full(self):
        '''
        Determines if the board is full.
        '''
        return ' ' not in self._board
    
    def space_check(self, position):
        '''
        Determines if the position on the board is empty.
        '''
        return self._board[position] == ' '

    def place_marker(self, marker, position):
        '''
        Places a maker on the board at the specified position.
        '''
        self._board[position] = marker

    def win_check(self, marker):
        '''
        Checks the board to see if the given marker has won the game.
        '''
        wins = [(1,2,3), (4,5,6),(7,8,9),
			(1,4,7), (2,5,8),(3,6,9),
			(1,5,9),(3,5,7)]

        for x, y, z in wins:
            if self._board[x] == self._board[y] == self._board[z] == marker:
                return True
                
        return False

class Game(object):
    '''
    Plays a single game of Tic Tac Toe
    '''
    def __init__(self):
        self._board = Board()

    def __get_player_markers(self):
        '''
        Prompts first player for their marker (X or O)
        '''
        self.player1Marker = ''

        while self.player1Marker not in ('X', 'O'):
            self.player1Marker = input("Please pick a marker 'X' or 'O': ")
            self.player1Marker = self.player1Marker.upper().strip()

        # determine the second player's marker
        if self.player1Marker == 'X':
            self.player2Marker = 'O'
        else:
            self.player2Marker = 'X'

    def __choose_first_player(self):
        '''
        Randomly chooses a player to take the first turn.
        '''
        if random.randint(0, 1) == 0:
            self.currentPlayer = 'Player 1'
        else:
            self.currentPlayer = 'Player 2'

    def __get_move(self):
        '''
        Prompts current player for their next move.
        '''
        position = int(input('Please enter a number (1-9): '))

        while not self._board.space_check(position):
            position = int(input('That position has been taken. Please enter a number: '))

        return position

    def init_game(self):
        '''
        Sets up game parameters.
        '''
        self.__get_player_markers()
        self.__choose_first_player()
        self._board.clear()

    def play(self):
        '''
        Plays a single game of Tic Tac Toe.
        '''
        self.init_game()

        print("{} will go first.\n".format(self.currentPlayer))

        # display the empty board
        print(self._board)

        while True:
            # determine which player's marker to place on the board
            if self.currentPlayer == 'Player 1':
                marker = self.player1Marker
            else:
                marker = self.player2Marker

            # get the player's move
            position = self.__get_move()
            print('')

            # update the board
            self._board.place_marker(marker, position)
            print(self._board)

            # check for a winner
            if self._board.win_check(marker):
                print('{} wins!'.format(self.currentPlayer))
                break
            elif self._board.is_full():
                print('The game is a draw!')
                break
            else:
                if self.currentPlayer == 'Player 1':
                    self.currentPlayer = 'Player 2'
                else:
                    self.currentPlayer = 'Player 1'

class Board(object):
    '''
    Abstraction of a Tic Tac Toe board
    '''
    def __init__(self):
        self.board = [' '] * 10

    def __str__(self):
        '''
        Displays ASCII tic-tac-toe board.
        '''
        output = """ {} | {} | {}
-----------
 {} | {} | {}
-----------
 {} | {} | {}
        """.format(self.board[1], self.board[2], self.board[3], 
        self.board[4], self.board[5], self.board[6], 
        self.board[7], self.board[8], self.board[9])

        return output

    def is_full(self):
        '''
        Determines if the board is full.
        '''
        return ' ' not in self.board
    
    def space_check(self, position):
        '''
        Determines if the position on the board is empty.
        '''
        return self.board[position] == ' '

    def place_marker(self, marker, position):
        '''
        Places a maker on the board at the specified position.
        '''
        self.board[position] = marker

    def win_check(self, marker):
        '''
        Checks the board to see if the given marker has won the game.
        '''
        wins = [(1,2,3), (4,5,6),(7,8,9),
			(1,4,7), (2,5,8),(3,6,9),
			(1,5,9),(3,5,7)]

        for x, y, z in wins:
            if self.board[x] == self.board[y] == self.board[z] == marker:
                return True
                
        return False
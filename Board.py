# This is the class for the chess board. Creates an 8x8 matrix
# and becomes initialized in later iterations. Includes logic for
# black and white spaces, chess-standard piece locations, and
# information for piece move validation. The class will have
# methods to update the board after every valid move.

# Standard convention is white facing bottom and black on top here..

from Pieces import King, Queen, Rook, Bishop, Knight, Pawn


class Board:

    def __init__(self):
        self.board = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]

    def pretty_print_board(self):
        for z in self.board:
            print(z)
        pass

    def make_position_list(self):
        black_pieces_list = [
            bR1, bN1, bB1, bQ1, bK1, bB2, bN2, bR2,
            bP1, bP2, bP3, bP4, bP5, bP6, bP7, bP8]

        white_pieces_list = [
            wP1, wP2, wP3, wP4, wP5, wP6, wP7, wP8,
            wR1, wN1, wB1, wQ1, wK1, wB2, wN2, wR2]

        self.board = [
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]  # Creates an empty board every time instead of find and replace.

        # If the piece has been taken, upon updating the list, do not include.


        for x, y in enumerate(white_pieces_list):
            chess_board.board[y.position[0]][y.position[1]] = y.type

        for x, y in enumerate(black_pieces_list):
            chess_board.board[y.position[0]][y.position[1]] = y.type

        return chess_board


    pass


# These objects are created here and will be stored in lists later.
bR1 = Rook(0, 0, 'black')
bN1 = Knight(0, 1, 'black')
bB1 = Bishop(0, 2, 'black')
bQ1 = Queen(0, 3, 'black')
bK1 = King(0, 4, 'black')
bB2 = Bishop(0, 5, 'black')
bN2 = Knight(0, 6, 'black')
bR2 = Rook(0, 7, 'black')
bP1 = Pawn(1, 0, 'black')
bP2 = Pawn(1, 1, 'black')
bP3 = Pawn(1, 2, 'black')
bP4 = Pawn(1, 3, 'black')
bP5 = Pawn(1, 4, 'black')
bP6 = Pawn(1, 5, 'black')
bP7 = Pawn(1, 6, 'black')
bP8 = Pawn(1, 7, 'black')

wR1 = Rook(7, 0, 'white')
wN1 = Knight(7, 1, 'white')
wB1 = Bishop(7, 2, 'white')
wQ1 = Queen(7, 3, 'white')
wK1 = King(7, 4, 'white')
wB2 = Bishop(7, 5, 'white')
wN2 = Knight(7, 6, 'white')
wR2 = Rook(7, 7, 'white')
wP1 = Pawn(6, 0, 'white')
wP2 = Pawn(6, 1, 'white')
wP3 = Pawn(6, 2, 'white')
wP4 = Pawn(6, 3, 'white')
wP5 = Pawn(6, 4, 'white')
wP6 = Pawn(6, 5, 'white')
wP7 = Pawn(6, 6, 'white')
wP8 = Pawn(6, 7, 'white')
chess_board = Board()
chess_board.make_position_list()


# Game logic section
# Move validity
# Input: Piece, destination.
# Loops through the board
# Finds the piece's current location
# Analyzes the piece's target location
# Updates the board with the destination if the move is valid.
# if a capture is desired, analyzes the piece's capture set and updates
# the board by subtracting the piece.


wP3.piece_move_logic()
wP3.move_piece(4, 4)
chess_board.make_position_list()

# These are not removing previous locations of the pieces.
chess_board.pretty_print_board()
# wP3.piece_move_logic()
# wP3.pretty_print_scope()


class Piece:
    """ Creates a general class called Piece that further class methods can override.
    Each child class has its own unique move set.
    """

    alive = True
    scope = [
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
    ]

    def __init__(self, position_x, position_y, color):
        self.position_x, self.position_y = position_x, position_y
        self.position = [position_x, position_y]
        self.color = color
        pass

    def pretty_print_scope(self):
        for z in self.scope:
            print(z)
        pass

    def move_piece(self, new_position_x, new_position_y):
        self.position_x = new_position_x
        self.position_y = new_position_y
        self.position = [new_position_x, new_position_y]

    def death(self):
        self.alive = False

    pass


class Pawn(Piece):
    type = 'P'
    has_moved = False

    def piece_move_logic(self):
        self.scope = Piece.scope
        self.pretty_print_scope()

        self.scope[self.position_x][self.position_y] = "x"
        if self.color == "white":
            self.scope[self.position[0]-1][self.position[1]] = 1 # Row.
            if self.has_moved == False:
                self.scope[self.position[0]-2][self.position[1]] = 1

        if self.color == "black":
            self.scope[self.position[0]+1][self.position[1]] = 1 # Row.
            if self.has_moved == False:
                self.scope[self.position[0]+2][self.position[1]] = 1

        self.has_moved= True

    def move_piece(self, new_position_x, new_position_y):
        self.has_moved = False
        validity = piece_move_logic()
        print(validity)
        self.position_x = new_position_x
        self.position_y = new_position_y
        self.position = [new_position_x, new_position_y]

    pass

class Rook(Piece):
    type = 'R'
    has_moved = False
    pass

class King(Piece):
    type = 'K'
    check_status = False
    has_moved = False
    pass

class Queen(Piece):
    type = 'Q'
    pass

class Knight(Piece):
    type = 'N'
    pass

class Bishop(Piece):
    type = 'B'
    pass

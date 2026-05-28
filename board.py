from piece import Piece
class Square:
    __init__(self):
        self.row_coordinate = None
        self.column_coordinate = None
        self.color = None

class Board:
    __init__(self):
        self.board = create_board(self)

    
    def create_board(self):
        board = []
        for letter in range(ord('A'), ord('Z') + 1):
            row = []
            for number in range(0, 7):
                square = Square()
                square.row_coordinate = letter
                square.column_coordinate = number
                row.append(square)
            board.append(row)
        return board

    def populate_board(self)


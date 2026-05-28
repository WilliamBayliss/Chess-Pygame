from piece import Piece
class Square:
    __init__(self):
        self.row_coordinate = None
        self.column_coordinate = None
        self.colour = None

class Board:
    __init__(self):
        self.board = create_board(self)
    
    def paint_board(board):
        for row in board:
            if row[0].row_coordinate % 2 = 0:
                row[0:2:4:6].colour = 0
                row[1:3:5:7].colour = 1
            else:
                row[0:2:4:6].colour = 1
                row[1:3:5:7].colour = 0
            


    def create_board(self):
        board = []
        for letter in range(ord('A'), ord('Z') + 1):
            row = []
            for number in range(1, 8):
                square = Square()
                square.row_coordinate = number
                square.column_coordinate = letter
                row.append(square)
            board.append(row)
        paint_board(board)
        return board


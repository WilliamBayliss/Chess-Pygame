class Board:
    __init__(self):
        self.board = create_board(self)

    
    def create_board(self):
        board = []
        for letter in range(ord('A'), ord('Z') + 1):
            row = []
            for number in range(0, 7):
                row.append([letter, number])
            board.append(row)
        return board
            
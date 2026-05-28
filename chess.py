import pygame
import lib
pygame.init()
WIDTH, HEIGHT = 1200, 1200
class Player:
    def __init__(self):
        self.colour = None
        self.name = None

class Square:
    def __init__(self):
        self.x = None
        self.y = None
        self.colour = None
        self.size = None

class Board:
    def __init__(self):
        self.grid = self.create_board()

    def create_board(self):
        board = []
        for x in range(8):
            row = []
            for y in range(8):
                square = Square()
                square.x = x
                square.y = y
                if (x + y) % 2 == 0:
                    square.colour = (245, 245, 229) # Light 
                else:
                    square.colour = (139, 69, 19) # Dark
                square.size = WIDTH // 8
                row.append(square)
            board.append(row)
        return board

class Piece:
    def __init__(self):
        self.square = [None, None]
        self.color = None
        self.sprite = None
        self.moved = False
        self.available_moves = None








screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chessboard")

def draw_board():
    board = Board()
    for row in board.grid:
        row_index = board.grid.index(row)
        for square in row:
            col_index = row.index(square)
            pygame.draw.rect(screen, square.colour, (col_index * square.size, row_index * square.size, square.size, square.size))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_board()
    pygame.display.flip()

pygame.quit()
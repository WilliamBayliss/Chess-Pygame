import pygame
import lib
pygame.init()
WIDTH, HEIGHT = 400, 400
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

        return self

class Board:
    def __init__(self, WIDTH):
        self.board = create_board(WIDTH)
        def create_board(width, height):
        for x in range(8):
            for y in range(8):
                square = Square()
                square.x = x
                square.y = y
                if (x + y) %2 == 0:
                    square.colour = (245, 245, 229) # Light 
                else:
                    square.colour = (139, 69, 19) # Dark
                square.size = WIDTH // 8
        return board
        
class Piece:
    def __init__(self):
        self.square = [None, None]
        self.color = None
        self.sprite = None
        self.moved = False
        self.available_moves = None








screen = pygame.display.set_caption("Chessboard")

def draw_board(WIDTH):
    board = lib.board.Board(WIDTH)
    for row in board:
        for square in row:
            pygame.draw.rect(screen, square.colour, row *square.size, square * square.size, square.size, square.size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_board(WIDTH)
    pygame.display.flip()

pygame.quit()
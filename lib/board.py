import pygame
from piece import Piece

class Square:
    def __init__(self):
        self.x = None
        self.y = None
        self.colour = None
        self.size = None

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
                else 
                    square.colour = (139, 69, 19) # Dark
                square.size = WIDTH // 8
        return board


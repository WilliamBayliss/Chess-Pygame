import pygame
from lib.board import Board
from lib.piece import Piece
from lib.player import Player

pygame.init()
WIDTH, HEIGHT = 400, 400
SQUARE_SIZE = WIDTH // 8


board = Board()

screen = pygame.display.set_caption("Chessboard")

# Colours, light is offwhite, dark is brown
LIGHT = (245, 245, 229) 
DARK = (139, 69, 19)

def draw_board(board):
    


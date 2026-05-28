import pygame
from lib.board import Board
from lib.piece import Piece
from lib.player import Player

pygame.init()
WIDTH, HEIGHT = 400, 400



board = Board(WIDTH)

screen = pygame.display.set_caption("Chessboard")

def draw_board(board):
    


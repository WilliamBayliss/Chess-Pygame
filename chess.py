import pygame
from lib.board import Board
from lib.piece import Piece
from lib.player import Player

pygame.init()
WIDTH, HEIGHT = 400, 400





screen = pygame.display.set_caption("Chessboard")

def draw_board(WIDTH):
    board = Board(WIDTH)
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
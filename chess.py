import pygame
import os
import lib
#Initialize
WIDTH, HEIGHT = 1200, 1200
LIGHT = (245, 245, 229)
DARK = (139, 69, 19)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome to Chess!")
font = pygame.font.Font(None, 50)


#Classes --------------------------------------------------------------------------------------------------------------------

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

    # Create 2D array with 8 subarrays each having 8 instances of Square class; set Square properties
    # Sets Square colour using sum of coordinates modulo 2: if remainder 0 Squares are light coloured
    def create_board(self):
        board = []
        for x in range(8):
            row = []
            for y in range(8):
                square = Square()
                square.x = x
                square.y = y
                if (x + y) % 2 == 0:
                    square.colour = LIGHT 
                else:
                    square.colour = DARK
                square.size = WIDTH // 8
                row.append(square)
            board.append(row)
        return board

class Piece:
    def __init__(self):
        self.player = None
        self.value = None
        self.square = [None, None]
        self.colour = None
        self.sprite = None
        self.moved = False
        self.available_moves = None

#MAIN FUNCTIONS ----------------------------------------------------------------------------------------------------------

# Create instance of board class and draw board on screen
def draw_board():
    board = Board()
    for row in board.grid:
        row_index = board.grid.index(row)
        for square in row:
            col_index = row.index(square)
            pygame.draw.rect(screen, square.colour, (col_index * square.size, row_index * square.size, square.size, square.size)) 
    pygame.display.set_caption("Chessboard")

def get_player_name():
    name = ""
    getting_name = True

    while getting_name:
        screen.fill((40, 40, 40)) # Dark gray window for name selection
        prompt_surface = font.render("Enter your name:" + "|", True, (0, 255, 0))
        screen.blit(prompt_surface, (100, 200))

        #Event tracking loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # Handle user keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # Stop when user presses enter
                    getting_name = False
                elif event.key == pygame.K_BACKSPACE: # Remove last Character
                    name = name["-1"]
                else:
                      name += event.unicode 

    return name

def start_menu():
    player = Player()

    while True:
        screen.fill(LIGHT)
        mouse = pygame.mouse.get_pos()

        start_button = pygame.Rect(300, 300, 140, 50)
        exit_button = pygame.Rect(300, 380, 140, 50)

        pygame.draw.rect(screen, LIGHT if start_button.collidepoint(mouse) else DARK, start_button)
        pygame.draw.rect(screen, LIGHT if exit_button.collidepoint(mouse) else DARK, exit_button)

        start_text = font.render("Start", True, LIGHT)
        exit_text = font.render("Exit", True, LIGHT)

        screen.blit(start_text, (335, 305))
        screen.blit(exit_text, (335, 385))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(mouse):
                    game()
                if exit_button.collidepoint(mouse):
                    pygame.quit()
        pygame.display.update()

def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_board()
        pygame.display.update()

    pygame.quit()

start_menu()
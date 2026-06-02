import pygame
import os
import lib

# Global Vars
WIDTH, HEIGHT = 1200, 1200
LIGHT = (245, 245, 229)
DARK = (139, 69, 19)

GREY = (150, 150, 150)
ACTIVE_COLOUR = (0, 200, 0) # GREEN
WHITE = (255, 255, 255)

# Initialize pygame globals
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome to Chess!")
font = pygame.font.Font(None, 50)


#Classes --------------------------------------------------------------------------------------------------------------------

class Player:
    def __init__(self):
        self.colour = None
        self.style = None

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
    return board

def create_menu_buttons():
    start_button = pygame.Rect(350, 900, 140, 50)
    exit_button = pygame.Rect(650, 900, 140, 50)
    pygame.draw.rect(screen, LIGHT if start_button.collidepoint(pygame.mouse.get_pos()) else DARK, start_button)
    pygame.draw.rect(screen, LIGHT if exit_button.collidepoint(pygame.mouse.get_pos()) else DARK, exit_button)
    start_text = font.render("Start", True, LIGHT)
    exit_text = font.render("Exit", True, LIGHT)
    screen.blit(start_text, (385, 905))
    screen.blit(exit_text, (685, 905))

def start_menu_validator(name, colour, style):
    if len(name) > 0:
        if colour != None:
            if style != None:
                return True

def start_menu():
    player = Player()

    getting_player_info = True
    while getting_player_info == True:
        screen.fill(LIGHT)
        mouse = pygame.mouse.get_pos()

        # Colour Selection
        player_colour = None

        # Style Selection
        player_style = None

        # Menu Buttons
        create_menu_buttons()

        # Handle start menu user inputs
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                case pygame.K_ESCAPE:
                    pygame.quit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_BACKSPACE:
                            player_name = player_name[:-1]
                        case pygame.K_RETURN:
                            if start_menu_validator(player_name, player_colour, player_style):
                                game()
                        case _:
                            player_name += event.unicode

                case pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(mouse):
                        if start_menu_validator(player_name, player_colour, player_style):
                            game()
                    elif exit_button.collidepoint(mouse):
                        pygame.quit()
                    elif input_rect.collidepoint(mouse):
                        name_input_active = True

        pygame.display.update()

def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        board = draw_board()
        pygame.display.update()

    pygame.quit()

start_menu()
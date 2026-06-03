import pygame
import os
import fnmatch
from pathlib import Path

# Global Vars
WIDTH, HEIGHT = 1200, 1200
LIGHT = (245, 245, 229)
DARK = (139, 69, 19)

GRAY = (150, 150, 150)
ACTIVE_COLOUR = (0, 200, 0) # GREEN
CANCEL_COLOUR = (200, 0, 0) # RED
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
    def __init__(self, player, name):
        
        # Inherited player attributes
        self.player = player
        self.colour = player.colour
        self.style = player.style


        # Assign piece value based on name        
        self.name = name
        match name:
            case "Pawn":
                self.value = 1
            case "Knight":
                self.value = 3
            case "Bishop":
                self.value = 3
            case "Rook":
                self.value = 5
            case "Queen":
                self.value = 9
            case "King":
                self.value = 10
        

        pygame.sprite.Sprite.__init__(self)
        wb = self.colour.split()[0].lower()

        # Find correct sprite by interpolating piece data in fstring of file path. The piece's style, colour and name correspond
        # to the filepath of the correct sprite.
        # Filepath example: "./lib/Sprites/Pieces/{style}/{sprite file}"
        # Sprite files have this pattern: w-pawn, b-king, w-rook, etc.
        self.image = pygame.image.load(
            f"./lib/Sprites/Pieces/{self.style.lower()}/{"w" if self.colour == "Light" else "b"}-{self.name.lower()}.png"
            ).convert_alpha()
        


        # Piece info for gameplay        
        self.square = [None, None]
        self.moved = False
        self.legal_moves = []
        self.illegal_moves = []
        

            

        

# START MENU FUNCTIONS ----------------------------------------------------------------------------------------------------------


def create_colour_selection(colour):
    mouse = pygame.mouse.get_pos()
    prompt_surface = font.render("Choose your side:" + "", True, DARK)
    screen.blit(prompt_surface, (450, 200))
    white_selection_square = pygame.Rect(300, 300, 200, 200)
    black_selection_square = pygame.Rect(700, 300, 200, 200)

    # Squares
    pygame.draw.rect(screen, WHITE, white_selection_square)
    pygame.draw.rect(screen, BLACK, black_selection_square)

    # Borders for current selection highlight
    pygame.draw.rect(screen, ACTIVE_COLOUR if white_selection_square.collidepoint(mouse) else WHITE, white_selection_square, 2)
    pygame.draw.rect(screen, ACTIVE_COLOUR if black_selection_square.collidepoint(mouse) else BLACK, black_selection_square, 2)
    

    selection_surface = font.render("Selection: " + f"{colour}", True, DARK) if colour is not None else font.render("Selection: ", True, DARK)
    screen.blit(selection_surface, (450, 250))

    return [white_selection_square, black_selection_square]

def create_style_selection(style):
    mouse = pygame.mouse.get_pos()
    prompt_surface = font.render("Choose your piece style.", True, DARK)
    screen.blit(prompt_surface, (450, 600))
    classic_button = pygame.Rect(300, 690, 100, 100)

    # Draw buttons
    pygame.draw.rect(screen, WHITE, classic_button)

    # Draw borders for current highlight selection
    pygame.draw.rect(screen, ACTIVE_COLOUR if classic_button.collidepoint(mouse) else WHITE, classic_button, 2)

    # Selection choice display
    selection_surface = font.render("Selection: " + f"{style}", True, DARK) if style is not None else font.render("Selection: ", True, DARK)
    screen.blit(selection_surface, (450, 650))

    
    return [classic_button]

def create_menu_buttons():
    mouse = pygame.mouse.get_pos()
    start_button = pygame.Rect(350, 900, 150, 75)
    exit_button = pygame.Rect(650, 900, 150, 75)
    pygame.draw.rect(screen, ACTIVE_COLOUR if start_button.collidepoint(mouse) else DARK, start_button)
    pygame.draw.rect(screen, CANCEL_COLOUR if exit_button.collidepoint(mouse) else DARK, exit_button)
    start_text = font.render("Start", True, LIGHT)
    exit_text = font.render("Exit", True, LIGHT)
    screen.blit(start_text, start_button.center)
    screen.blit(exit_text, exit_button.center)

    return [start_button, exit_button] 

def start_menu_validator(colour, style):
    if colour is not None:
        if style is not None:
            return True
        else:
            return False
    else:
        return False

# Runs start menu where player can customize their pieces, the board, and the rules of the game
def start_menu():
    player = Player()
    
    start_menu = True
    while start_menu == True:
        screen.fill(LIGHT)
        mouse = pygame.mouse.get_pos()

        # Colour Selection
        
        colour_selection_buttons = create_colour_selection(player.colour)
        white_button = colour_selection_buttons[0]
        black_button = colour_selection_buttons[1]

        # Style Selection
        style_buttons = create_style_selection(player.style)
        classic_button = style_buttons[0]



        # Menu Buttons
        menu_buttons = create_menu_buttons()
        start_button = menu_buttons[0]
        exit_button = menu_buttons[1]
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
                            if start_menu_validator(player.colour, player.style):
                                start_menu == False
                        case _:
                            player_name += event.unicode

                case pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(mouse):
                        if start_menu_validator(player.colour, player.style):
                            start_menu = False
                    if exit_button.collidepoint(mouse):
                        pygame.quit()
                    if white_button.collidepoint(mouse):
                        player.colour = "Light"
                    if black_button.collidepoint(mouse):
                        player.colour = "Dark"
                    if classic_button.collidepoint(mouse):
                        player.style = "Classic"


        pygame.display.update()
    return player

# MAIN FUNCTIONS -----------------------------------------------------------------------------------------

def create_pieces(player):
    pieces = []
    for x in range(7):
        piece = Piece(player, "Pawn")
        pieces.append(piece)
    for x in range(2):
        piece = Piece(player, "Knight")
        pieces.append(piece)
    for x in range(2):
        piece = Piece(player, "Bishop")
        pieces.append(piece)
    for x in range(2):
        piece = Piece(player, "Rook")
        pieces.append(piece)
    queen = Piece(player, "Queen")
    king = Piece(player, "King")

    pieces.extend([queen, king])
    return pieces

    

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

def game():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.quit()

def main():
    player = start_menu()
    board = draw_board()
    player.pieces = create_pieces(player)
    game()

main()
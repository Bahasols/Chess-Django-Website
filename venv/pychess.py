#python chess game
import pygame

pygame.init()
WIDTH = 1200
HEIGTH = 1200
screen = pygame.display.set_mode([WIDTH, HEIGTH])
timer = pygame.time.Clock()
fps = 60
#game images and placement
w_pieces = ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
w_locations = [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7)]
b_pieces = ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']
b_locations = [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
w_taken = []
b_taken = []
#turn order is white starts at 0, white selects a piece is at 1, black starts at 2, and black selects a piece is at 3
turn_order = 0
selection = 100
valid_movement = []
#load images
b_queen = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackqueen.png')
b_queen = pygame.image.scale(b_queen, (90,90))
b_king = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackking.png')
b_king = pygame.image.scale(b_king, (90,90))
b_bishop = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackbishop.png')
b_bishop = pygame.image.scale(b_bishop, (90,90))
b_knight = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackknight.png')
b_knight = pygame.image.scale(b_knight, (90,90))
b_pawn = pygame.image.load('chess_project/chess_project/pieces/black pieces/black pawn.png')
b_pawn = pygame.image.scale(b_pawn, (90,90))
b_rook = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackrook.png')
b_rook = pygame.image.scale(b_rook, (90,90))
w_queen = pygame.image.load('chess_project/chess_project/pieces/white pieces/whitequeen.png')
w_queen = pygame.image.scale(w_queen, (90,90))
w_king = pygame.image.load('chess_project/chess_project/pieces/white pieces/whiteking.png')
w_king = pygame.image.scale(w_king, (90,90))
w_bishop = pygame.image.load('chess_project/chess_project/pieces/white pieces/whitebishop.png')
w_bishop = pygame.image.scale(w_bishop, (90,90))
w_knight = pygame.image.load('chess_project/chess_project/pieces/white pieces/whiteknight.png')
w_knight = pygame.image.scale(w_knight, (90,90))
w_pawn = pygame.image.load('chess_project/chess_project/pieces/white pieces/whitepawn.png')
w_pawn = pygame.image.scale(w_pawn, (90,90))
w_rook = pygame.image.load('chess_project/chess_project/pieces/white pieces/whiterook.png')
w_rook = pygame.image.scale(w_rook, (90,90))
#main
run = True
while run:
    timer.tick(fps)
    screen.fill('light gray')

    for event in pygame.event.get():
       if event.type == pygame.quit: 
        run = False
    pygame.display.flip()
pygame.quit()
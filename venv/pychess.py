#python chess game
import pygame

pygame.init()
WIDTH = 1000
HEIGTH = 950
screen = pygame.display.set_mode([WIDTH, HEIGTH])
timer = pygame.time.Clock()
fps = 60
large_font = pygame.font.Font('freesansbold.ttf', 48)
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
b_queen = pygame.transform.scale(b_queen, (90,90))
b_king = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackking.png')
b_king = pygame.transform.scale(b_king, (90,90))
b_bishop = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackbishop.png')
b_bishop = pygame.transform.scale(b_bishop, (90,90))
b_knight = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackknight.png')
b_knight = pygame.transform.scale(b_knight, (90,90))
b_pawn = pygame.image.load('chess_project/chess_project/pieces/black pieces/black pawn.png')
b_pawn = pygame.transform.scale(b_pawn, (70,70))
b_rook = pygame.image.load('chess_project/chess_project/pieces/black pieces/blackrook.png')
b_rook = pygame.transform.scale(b_rook, (90,90))
w_queen = pygame.image.load('chess_project/chess_project/pieces/white pieces/whitequeen.png')
w_queen = pygame.transform.scale(w_queen, (90,90))
w_king = pygame.image.load('chess_project/chess_project/pieces/white pieces/whiteking.png')
w_king = pygame.transform.scale(w_king, (90,90))
w_bishop = pygame.image.load('chess_project/chess_project/pieces/white pieces/whitebishop.png')
w_bishop = pygame.transform.scale(w_bishop, (90,90))
w_knight = pygame.image.load('chess_project/chess_project/pieces/white pieces/whiteknight.png')
w_knight = pygame.transform.scale(w_knight, (90,90))
w_pawn = pygame.image.load('chess_project/chess_project/pieces/white pieces/whitepawn.png')
w_pawn = pygame.transform.scale(w_pawn, (70,70))
w_rook = pygame.image.load('chess_project/chess_project/pieces/white pieces/whiterook.png')
w_rook = pygame.transform.scale(w_rook, (90,90))
w_images = [w_bishop,w_king,w_knight,w_queen,w_pawn,w_rook]
b_images = [b_bishop,b_king,b_knight,b_queen,b_pawn,b_rook]
piece_list = ['pawn','knight','bishop','rook','queen','king']

#drawing up chess board
def draw_board():
   for i in range(32):
      column =i % 4
      row = i // 4
      if row % 2 == 0:
         pygame.draw.rect(screen, 'dark blue', [600 - (column*200), row*100, 100, 100])
      else:
         pygame.draw.rect(screen, 'dark blue', [700 - (column*200), row*100, 100, 100])
      pygame.draw.rect(screen, 'light blue', [0, 800, WIDTH, 150])
      pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 150], 10)
      pygame.draw.rect(screen, 'gold', [800, 0, 200, 810], 10)
      status_text = ['White: Select a Piece to move', 'White: Select its destination', 'Black: Select a Piece to move', 'Black: Select its destination']
      screen.blit(large_font.render(status_text[turn_order], True, 'black'), (20, 850))
#main
run = True
while run:
    timer.tick(fps)
    screen.fill('tan')
    draw_board()

    for event in pygame.event.get():
       if event.type == pygame.QUIT: 
        run = False
    pygame.display.flip()
pygame.QUIT()
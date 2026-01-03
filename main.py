import pygame
from board import *
from square import *

pygame.init()

# Font
font = pygame.font.SysFont("arial", 50)

clock = pygame.time.Clock()
FPS = 60
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

game_board = Board()
player = "X"
game_over = False  # Add a flag to track if the game is over

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # Only allow moves if the game is not over
            # Check which button was pressed
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for row in game_board.board:
                    for square in row:
                        if square.is_clicked(mouse_pos) and square.value == "":
                            square.value = player
                            if player == "X":
                                player = "O"
                            else:
                                player = "X"
    game_board.draw_board(screen)
    winner = game_board.get_winner()
    if winner != "":
        game_over = True  # Set the game_over flag to True when a winner is found
        text_surf = font.render(f'The winner is {winner}', True, 'purple')
        screen.blit(text_surf, (180, 300))
     
    clock.tick(FPS)
    pygame.display.flip()
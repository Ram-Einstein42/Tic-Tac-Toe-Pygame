import pygame
from board import *
from square import *

pygame.init()
clock = pygame.time.Clock()
FPS = 60

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

test_board = Board()



run = True
while run:
     

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    test_board.board[0][0].draw_square(screen)
    clock.tick(FPS)
    pygame.display.flip()

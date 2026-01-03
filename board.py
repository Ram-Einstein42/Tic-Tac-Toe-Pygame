import pygame
from square import *

class Board:
    def __init__(self):
        self.board = [[Square((0,0)), Square((200,0)),Square((400,0))],
                      [Square((0,200)),Square((200,200)), Square((400,200))],
                      [Square((0,400)),Square((200,400)), Square((400,400))]]
    
    def draw_board(self, screen):
        for row in self.board:
            for square in row:
                square.draw_square(screen)
        pygame.draw.line(screen, 'black', (200,0), (200,600), 5)
        pygame.draw.line(screen, 'black', (400,0), (400,600), 5)
        pygame.draw.line(screen, 'black', (0,200), (600,200), 5)
        pygame.draw.line(screen, 'black', (0,400), (600,400), 5)
    
    def place_marker(self, row, col, marker):
        if self.board[row][col].value == '':
            self.board[row][col].value = marker
            return True
        return False
    
    def get_winner(self):
        # rows
        for r in range(3):
            if self.board[r][0].value == self.board[r][1].value == self.board[r][2].value and self.board[r][0].value != "":
                return self.board[r][0].value

        # columns
        for c in range(3):
            if self.board[0][c].value == self.board[1][c].value == self.board[2][c].value and self.board[0][c].value != "":
                return self.board[0][c].value
        
        # diagonals
        if self.board[0][0].value == self.board[1][1].value == self.board[2][2].value and self.board[0][0].value != "":
            return self.board[0][0].value

        if self.board[0][2].value == self.board[1][1].value == self.board[2][0].value and self.board[2][0].value != "":
            return self.board[0][2].value

        return ""
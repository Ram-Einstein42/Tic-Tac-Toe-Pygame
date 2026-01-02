import pygame
class Square:
    size = (200,200)

    def __init__(self, position):
        self.position = position
        self.rect = pygame.rect.Rect(position, Square.size)
        self.value = 'O'
        self.center_pos = (position[0] + 100, position[1] + 100)
    
    def draw_square(self, screen):
        pygame.draw.rect(screen,'white',self.rect)

        if self.value == 'O':
            pygame.draw.circle(screen, 'black', self.center_pos, 100, 5)

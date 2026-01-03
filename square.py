import pygame
class Square:
    size = (200,200)

    def __init__(self, position):
        self.position = position
        self.rect = pygame.rect.Rect(position, Square.size)
        self.value = ''
        self.center_pos = (position[0] + 100, position[1] + 100)
    
    def draw_square(self, screen):
        pygame.draw.rect(screen,'white',self.rect)

        if self.value == 'O':
            pygame.draw.circle(screen, 'red', self.center_pos, 100, 5)
        elif self.value == 'X':
            pygame.draw.line(screen, 'blue', self.rect.topleft, self.rect.bottomright, 5) 
            pygame.draw.line(screen, 'blue', self.rect.topright, self.rect.bottomleft, 5)  

    def is_clicked(self, position):
        return self.rect.collidepoint(position)
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' An attempt to represent an alien. '''

    def __init__(self, ss):
        ''' Initialize main attributes. '''

        super().__init__()

        self.screen = ss.screen

        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        ''' Blits the alien. '''
    
        self.screen.blit(self.image, self.rect)
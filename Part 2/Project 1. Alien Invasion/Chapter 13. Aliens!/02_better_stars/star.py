import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    ''' An attempt to represent a star. '''

    def __init__(self, bs):
        ''' Initialize main attributes. '''

        super().__init__()
        
        self.screen = bs.screen

        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

    def blitme(self):
        ''' Makes the star visible. '''
          
        self.screen.blit(self.image, self.rect)

        
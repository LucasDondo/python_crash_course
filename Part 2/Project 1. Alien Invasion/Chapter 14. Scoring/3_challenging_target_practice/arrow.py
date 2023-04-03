import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):
    ''' An attempt to represent an arrow. '''

    def __init__(self, tp):
        ''' Initialize main attributes. '''

        super().__init__()
        self.bow = tp.bow
        self.settings = tp.settings
        self.speed = self.settings.arrow_speed
        self.screen = tp.screen

        self.img = pygame.image.load('images/arrow1.png')
        self.rect = self.img.get_rect()

        self.x = float(self.rect.x)
        self.rect.midright = self.bow.rect.midright

    def update(self):
        ''' Moves the arrow to the right. '''

        self.x += self.speed
    
    def blit(self):
        ''' Blit me. '''
    
        self.rect.x = self.x
        self.screen.blit(self.img, self.rect)
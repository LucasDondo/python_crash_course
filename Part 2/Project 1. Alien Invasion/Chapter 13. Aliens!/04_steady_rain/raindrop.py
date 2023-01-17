import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    ''' An attempt to represent a raindrop. '''

    def __init__(self, r):
        ''' Initialize main attributes. '''

        super().__init__()

        self.screen = r.screen
        self.screen_rect = r.screen_rect
        self.settings = r.settings

        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new raindrop at the top of the screen, not visible.
        self.rect.bottom = self.screen_rect.top

    def fell(self):
        ''' Returns if the raindrop is falling or if it already fell. '''
    
        while self.rect.top >= self.screen_rect.bottom:
            return True

    def update(self):
        ''' Updates the raindrop position. '''
        
        self.y = float(self.rect.y)    
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

    def blitme(self):
        ''' Blits the raindrop. '''
    
        self.screen.blit(self.image, self.rect)
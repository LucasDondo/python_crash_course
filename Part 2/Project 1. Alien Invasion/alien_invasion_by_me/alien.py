import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' A class to represent a single alien in the fleet. '''

    def __init__(self, ai):
        ''' Initialize the alien and set its starting position. '''

        super().__init__()
        self.screen = ai.screen
        self.screen_rect = ai.screen_rect
        self.settings = ai.settings

        # Load the alien img and set its rect attribute.
        self.img = pygame.image.load('images/alien_30%.bmp')
        self.rect = self.img.get_rect()

    def check_edges(self):
        ''' Return True if alien is at edge of screen. '''
    
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        ''' Move the alien right or left. '''

        self.rect.x += (self.settings.alien_speed * self.settings.fleet_direction)
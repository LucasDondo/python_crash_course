import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    ''' A class to represent a single alien in the fleet. '''

    def __init__(self, ai):
        ''' Initialize the alien and set its starting position. '''

        super().__init__()
        self.ai = ai

        self.IMAGE = pygame.image.load('images/alien_30%.bmp')
        self.rect  = self.IMAGE.get_rect()

    def check_edges(self):
        ''' Return True if alien is at edge of screen. '''

        if self.rect.right >= self.ai.SCREEN_RECT.right or self.rect.left <= 0:
            return True

    def update(self):
        ''' Move the alien right or left. '''

        self.rect.x += self.ai.alien_speed * self.ai.fleet_direction

    def show(self):
        ''' Draw the alien to the screen. '''

        self.ai.SCREEN.blit(self.IMAGE, self.rect)
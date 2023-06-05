import pygame
from pygame.sprite import Sprite

class Rocket(Sprite):
    ''' A class to manage the rocket. '''

    def __init__(self, ai):
        ''' Initialize the rocket and set its starting position. '''

        super().__init__()
        self.ai          = ai
        self.SCREEN_RECT = self.ai.SCREEN_RECT

        self.IMAGE        = pygame.image.load('images/rocket_25%.bmp')
        self.rect         = self.IMAGE.get_rect()
        self.rect.centerx = self.SCREEN_RECT.centerx
        self.x            = float(self.rect.x)
        self.moving_right = False
        self.moving_left  = False

    def update(self):
        ''' Update the rocket's position based on the movement flag. '''

        # Update the rocket's x attribute, not the rect.
        if self.moving_right and self.rect.right < self.SCREEN_RECT.right:
            self.x += self.ai.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def show(self):
        ''' Draw the rocket at its current location. '''

        self.ai.SCREEN.blit(self.IMAGE, self.rect)

    def center_rocket(self):
        ''' Center the rocket on the screen. '''
    
        self.rect.centerx = self.SCREEN_RECT.centerx
        self.x            = float(self.rect.x)

class ScoreBarRocket(Rocket):
    ''' An attempt to represent an horizontal rocket for the scorebar. '''

    def __init__(self, ai, BOTTOM):
        ''' Initialize main attributes. '''

        super().__init__(ai)

        self.IMAGE = pygame.image.load('images/horizontal_rocket_15%.bmp')
        self.rect  = self.IMAGE.get_rect()

        self.rect.bottom = BOTTOM
        self.rect.right  = 0
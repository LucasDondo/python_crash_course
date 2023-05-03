import pygame
from pygame.sprite import Sprite

class Rocket(Sprite):
    ''' A class to manage the rocket. '''

    def __init__(self, ai):
        ''' Initialize the rocket and set its starting position. '''

        super().__init__()
        self.screen      = ai.screen
        self.screen_rect = ai.screen_rect
        self.settings    = ai.settings

        # Load the rocket img and get its rect.
        self.image  = pygame.image.load('images/rocket_25%.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.height - self.settings.sb_height

        # Store a decimal value for the rocket's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags.
        self.moving_right = False
        self.moving_left  = False

    def update(self):
        ''' Update the rocket's position based on the movement flag. '''

        # Update the rocket's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        ''' Draw the rocket at its current location. '''

        self.screen.blit(self.image, self.rect)

    def center_rocket(self):
        ''' Center the rocket on the screen. '''
    
        self.rect.centerx = self.screen_rect.centerx
        self.x            = float(self.rect.x)
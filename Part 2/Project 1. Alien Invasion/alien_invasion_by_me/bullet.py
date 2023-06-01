import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' A class to manage bullets fired from the rocket. '''

    def __init__(self, ai):
        ''' Create a bullet object at the rocket's current position. '''

        super().__init__()
        self.SCREEN   = ai.SCREEN
        self.settings = ai.settings

        self.IMAGE       = pygame.image.load('images/bullet_15%.bmp')
        self.rect        = self.IMAGE.get_rect()
        self.rect.midtop = ai.rocket.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        ''' Move the bullet up the screen. '''

        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed

        # Update the rect position.
        self.rect.y = self.y

    def show(self):
        ''' Draw the bullet to the screen. '''
    
        self.SCREEN.blit(self.IMAGE, self.rect)
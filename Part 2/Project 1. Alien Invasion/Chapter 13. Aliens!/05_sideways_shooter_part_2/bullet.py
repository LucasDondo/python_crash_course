import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' An attempt to represent a bullet. '''

    def __init__(self, ss):
        ''' Initialize main attributes. '''

        super().__init__()
        self.settings = ss.settings
        self.screen = ss.screen
        self.ship = ss.ship
        self.screen_rect = ss.screen_rect
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midright = self.ship.rect.midright

        self.x = float (self.rect.x)

    def update(self):
        ''' Starts main class actions. '''

        # Moves and draws bullet.
        self.rect.x += self.settings.bullet_speed
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
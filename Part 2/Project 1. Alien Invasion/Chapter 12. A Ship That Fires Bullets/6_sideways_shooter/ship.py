import pygame

class Ship():
    ''' An attempt to represent a ship. '''

    def __init__(self, ss):
        ''' Initialize main attributes. '''
        
        # Settings and screen.
        self.settings = ss.settings
        self.screen = ss.screen
        self.screen_rect = ss.screen_rect

        # The ship itself.
        self.image = pygame.image.load('images\ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        ''' Update the ship's position based on movement flags. '''
    
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.y = self.y
        self.screen.blit(self.image, self.rect)
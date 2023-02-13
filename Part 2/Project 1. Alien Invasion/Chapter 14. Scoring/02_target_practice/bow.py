import pygame

class Bow:
    ''' An attempt to represent a bow. '''

    def __init__(self, tp):
        ''' Initialize main attributes. '''

        self.screen = tp.screen
        self.screen_rect = tp.screen_rect
        self.settings = tp.settings
        self.speed = self.settings.bow_speed

        self.img = pygame.image.load('images/bow1.png')
        self.rect = self.img.get_rect()

        self._center()
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False
    
    def _center(self):
        ''' Centers the bow. '''
    
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def update(self):
        ''' Updates the bow position. '''
    
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

    def blit(self):
        ''' Starts main class actions. '''

        self.rect.y = self.y
        self.screen.blit(self.img, self.rect)
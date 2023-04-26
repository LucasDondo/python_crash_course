import pygame
from pygame.sprite import Sprite


class Arrow(Sprite):
    ''' An attempt to represent an arrow. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        super().__init__()
        self.tbm             = tbm
        self.screen          = self.tbm.screen
        self.screen_rect     = self.tbm.screen_rect
        self.bow             = self.tbm.bow
        self.target          = self.tbm.target
        self.stopped         = self.target.stopped
        self.settings        = self.tbm.settings
        self.speed           = self.settings.arrow_speed
        self.animation_speed = self.settings.arrow_animation_speed

        self.img  = pygame.image.load('images/arrow_horizontal.png')
        self.rect = self.img.get_rect()

        self.rect.midright = self.bow.rect.midright
        self.x             = float(self.rect.x)
        self.y             = float(self.rect.y)

    def update(self):
        ''' Moves the arrow to the right. '''

        self.x += self.speed
    
    def move_as_target(self, movement_direction):
        ''' Desired movement for nailed arrows. '''
    
        if not self.tbm.target.stopped:
            self.y += self.target.speed * movement_direction
        self.rect.y = self.y
    
    def fall(self):
        ''' Makes the arrow fall. '''
    
        while self.rect.top < self.screen_rect.bottom:
            self.y += self.animation_speed
            self.tbm._update_screen()

    def blit(self):
        ''' Blit me. '''
    
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen.blit(self.img, self.rect)
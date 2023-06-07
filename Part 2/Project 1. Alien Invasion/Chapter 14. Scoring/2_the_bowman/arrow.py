import pygame
from pygame.sprite import Sprite


class Arrow(Sprite):
    ''' An attempt to represent an arrow. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        super().__init__()
        self.tbm             = tbm
        self.SCREEN          = self.tbm.SCREEN
        self.SCREEN_RECT     = self.tbm.SCREEN_RECT
        self.bow             = self.tbm.bow
        self.target          = self.tbm.target
        self.SPEED           = 6.0
        self.ANIMATION_SPEED = 5.0

        self.IMG  = pygame.image.load('images/arrow_horizontal.png')
        self.rect = self.IMG.get_rect()

        self.rect.midright = self.bow.rect.midright
        self.x             = float(self.rect.x)
        self.y             = float(self.rect.y)

    def update(self):
        ''' Moves the arrow to the right. '''

        self.x += self.SPEED
    
    def move_as_target(self, movement_direction):
        ''' Desired movement for nailed arrows. '''
    
        if not self.tbm.target.stopped:
            self.y += self.target.speed * movement_direction
        self.rect.y = self.y
    
    def fall(self):
        ''' Makes the arrow fall. '''
    
        while self.rect.top < self.SCREEN_RECT.bottom:
            self.y += self.ANIMATION_SPEED
            self.tbm.update_screen()

    def show(self):
        ''' Blit me. '''
    
        self.rect.x = self.x
        self.rect.y = self.y
        self.SCREEN.blit(self.IMG, self.rect)
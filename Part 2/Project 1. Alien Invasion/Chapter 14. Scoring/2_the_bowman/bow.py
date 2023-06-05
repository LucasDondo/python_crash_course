import pygame

class Bow:
    ''' An attempt to represent a bow. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        self.tbm             = tbm
        self.SCREEN          = self.tbm.SCREEN
        self.SCREEN_RECT     = self.tbm.SCREEN_RECT
        self.GAME_TOP        = self.tbm.GAME_TOP
        self.CENTER_UNDER_SB = self.GAME_TOP + (self.SCREEN_RECT.height - \
                                                        self.GAME_TOP) / 2
        self.SPEED           = 1.0
        self.ANIMATION_SPEED = self.tbm.ANIMATION_SPEED

        self.IMG  = pygame.image.load('images/bow1.png')
        self.rect = self.IMG.get_rect()

        self.rect.left    = self.SCREEN_RECT.left
        self.rect.centery = self.CENTER_UNDER_SB
        self.y            = float(self.rect.y)

        # Movement flags.
        self.moving_up   = False
        self.moving_down = False
    
    def center(self):
        ''' Centers the bow. '''

        if self.rect.centery < self.CENTER_UNDER_SB:
            self.moving_down = True
            while self.rect.centery < self.CENTER_UNDER_SB:
                self.y += self.ANIMATION_SPEED
                self.tbm.update_screen()
            self.moving_down = False
        elif self.rect.centery > self.CENTER_UNDER_SB:
            self.moving_down = True
            while self.rect.centery > self.CENTER_UNDER_SB:
                self.y -= self.ANIMATION_SPEED
                self.tbm.update_screen()
            self.moving_down = False
        elif self.rect.centery == self.CENTER_UNDER_SB:
            pass

    def update(self):
        ''' Updates the bow position. '''
    
        if self.moving_up and self.rect.top > (self.GAME_TOP \
                                                                  + self.SPEED):
            self.y -= self.SPEED
        if self.moving_down and self.rect.bottom < (self.SCREEN_RECT.bottom \
                                                                  - self.SPEED):
            self.y += self.SPEED

    def show(self):
        ''' Starts main class actions. '''

        self.rect.y = self.y
        self.SCREEN.blit(self.IMG, self.rect)
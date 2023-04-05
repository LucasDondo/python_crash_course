import pygame

class Bow:
    ''' An attempt to represent a bow. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        self.tbm = tbm
        self.settings = tbm.settings
        self.screen = tbm.screen
        self.screen_rect = tbm.screen_rect
        self.sb_line_y = self.settings.sb_line_y
        self.center_under_sb = self.sb_line_y + (self.screen_rect.height - self.sb_line_y) / 2
        self.speed = self.settings.bow_speed
        self.animation_speed = self.settings.animation_speed

        self.img = pygame.image.load('images/bow1.png')
        self.rect = self.img.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.centery = self.center_under_sb
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False
    
    def center(self):
        ''' Centers the bow. '''

        if self.rect.centery < self.center_under_sb:
            self.moving_down = True
            while self.rect.centery < self.center_under_sb:
                self.y += self.animation_speed
                self.tbm._update_screen()
            self.moving_down = False
        elif self.rect.centery > self.center_under_sb:
            self.moving_down = True
            while self.rect.centery > self.center_under_sb:
                self.y -= self.animation_speed
                self.tbm._update_screen()
            self.moving_down = False
        elif self.rect.centery == self.center_under_sb:
            pass

    def update(self):
        ''' Updates the bow position. '''
    
        if self.moving_up and self.rect.top > self.sb_line_y + self.speed:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

    def blit(self):
        ''' Starts main class actions. '''

        self.rect.y = self.y
        self.screen.blit(self.img, self.rect)
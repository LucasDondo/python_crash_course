import pygame
from rocket import ScoreBarRocket

class ScoreBar:
    ''' An attempt to represent a scorebar. '''

    def __init__(self, ai):
        ''' Initialize main attributes. '''

        self.ai              = ai
        self.screen_rect     = self.ai.screen_rect
        self.settings        = self.ai.settings
        self.bottom_distance = self.settings.sb_height
        self.stats           = self.ai.stats

        self.rect         = pygame.Rect(0, 0, 0, 1)
        self.rect.centery = self.screen_rect.height - self.bottom_distance

        self.rocket = ScoreBarRocket(ai)

    def reset(self):
        ''' Resets the bar w/ an animation. '''
    
        while self.rect.width > 0:
            self.rect.width        -= self.settings.sb_reset_animation_speed
            self.rocket.rect.right -= self.settings.sb_reset_animation_speed
            self.ai._update_screen()

    def update(self):
        ''' Updates the sb's length. '''

        try:
            pct_score = self.stats.score * 100 / self.stats.hs
        except ZeroDivisionError:
            pct_score = 0
        pct_screen = pct_score * self.screen_rect.width / 100

        if self.rect.width < pct_screen:
            self.rect.width        += self.settings.sb_animation_speed
            self.rocket.rect.right += self.settings.sb_animation_speed

    def draw(self):
        ''' Draws the sb to screen. '''
    
        pygame.draw.rect(self.ai.screen, self.settings.sb_color, self.rect)
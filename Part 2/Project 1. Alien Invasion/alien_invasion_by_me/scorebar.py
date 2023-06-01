import pygame
from rocket import ScoreBarRocket

class ScoreBar:
    ''' An attempt to represent a scorebar. '''

    def __init__(self, ai):
        ''' Initialize main attributes. '''

        self.ai          = ai
        self.SCREEN      = self.ai.SCREEN
        self.SCREEN_RECT = self.ai.SCREEN_RECT
        self.stats       = self.ai.stats
        self.settings    = self.ai.settings

        self.rect   = pygame.Rect(0, 0, 0, 1)
        self.rocket = ScoreBarRocket(ai)

        self.rect.centery = self.rocket.rect.centery

        # Create the cleaning rect.
        self.cleaning_rect         = pygame.Rect(0, 0, 0,
                                                        self.rocket.rect.height)
        self.cleaning_rect.right   = self.SCREEN_RECT.right
        self.cleaning_rect.centery = self.rect.centery

    def reset(self):
        ''' Resets the bar w/ an animation using dirty blitting. '''

        self.cleaning_rect.width  = 0
        self.cleaning_rect.right  = self.SCREEN_RECT.right
    
        while self.rect.width > 0:
            self.rect.width          -= self.settings.SB_RESET_ANIMATION_SPEED
            self.rocket.rect.right   -= self.settings.SB_RESET_ANIMATION_SPEED
            self.cleaning_rect.width += self.settings.SB_RESET_ANIMATION_SPEED
            self.cleaning_rect.left  -= self.settings.SB_RESET_ANIMATION_SPEED

            pygame.draw.rect(self.SCREEN, self.ai.BG_COLOR, self.cleaning_rect)
            self.show()
            pygame.display.flip()

    def update(self):
        ''' Updates the sb's length. '''

        try:
            pct_score = self.stats.score * 100 / self.stats.hs
        except ZeroDivisionError:
            pct_score = 0
        pct_screen = pct_score * self.SCREEN_RECT.width / 100

        if self.rect.width < pct_screen:
            self.rect.width        += self.settings.SB_ANIMATION_SPEED
            self.rocket.rect.right += self.settings.SB_ANIMATION_SPEED

    def show(self):
        ''' Draws the sb to screen. '''
    
        pygame.draw.rect(self.SCREEN, self.settings.SB_COLOR, self.rect)
        self.rocket.show()
import pygame

class PlayButton:
    ''' The magic button to start playing. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        self.SCREEN          = tbm.SCREEN
        self.SCREEN_RECT     = tbm.SCREEN_RECT
        self.GAME_TOP        = tbm.GAME_TOP
        self.CENTER_UNDER_SB = self.GAME_TOP + (self.SCREEN_RECT.height \
                                                         - self.GAME_TOP) / 2
        self.FONT            = tbm.FONT

        # Button (rect).
        self.WIDTH, self.HEIGHT = 200, 50
        self.COLOR              = (0, 0, 0)
        self.BORDER_RADIUS      = 25
        #
        self.rect         = pygame.Rect(0, 0, self.WIDTH, self.HEIGHT)
        self.rect.centerx = self.SCREEN_RECT.centerx
        self.rect.centery = self.CENTER_UNDER_SB

        # Msg (img).
        self.MSG       = "Let's go!"
        self.TXT_COLOR = tbm.BG_COLOR
        #
        self.MSG_IMG              = self.FONT.render(self.MSG, True,
                                                                 self.TXT_COLOR,
                                                                     self.COLOR)
        self.MSG_IMG_RECT         = self.MSG_IMG.get_rect()
        self.MSG_IMG_RECT.centerx = self.SCREEN_RECT.centerx
        self.MSG_IMG_RECT.centery = self.CENTER_UNDER_SB

    def show(self):
        ''' Shows the rect and the img. '''

        pygame.draw.rect(self.SCREEN, self.COLOR, self.rect,
                                               border_radius=self.BORDER_RADIUS)
        self.SCREEN.blit(self.MSG_IMG, self.MSG_IMG_RECT)        
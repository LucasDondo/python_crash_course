import pygame
import json

class Stats:
    ''' All game stats can be found here. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        # Recover highest score.
        try:
            with open(tbm.HS_FILE) as f:
                self.hs = json.load(f)
        except FileNotFoundError:
            self.hs = 0

        # Statsboard.
        self.tbm         = tbm
        self.SCREEN      = tbm.SCREEN
        self.SCREEN_RECT = tbm.SCREEN_RECT
        self.FONT        = tbm.FONT
        self.BG_COLOR    = tbm.BG_COLOR
        self.SPACING     = 10

        # Initialize stats.
        self.reset()
        self.sb_line     = Line(tbm, self.arrows_rect.bottom + self.SPACING)
        self.game_active = False

    def reset(self):
        ''' Reset all stats. '''

        self.arrows_left = 3
        self.score       = 0
        self._update_arrows()
        self.update_score()
        self.update_hs()

    def _update_arrows(self):
        ''' Updates the arrows left. '''

        if self.arrows_left == 3:
            img = 'images/3_arrows.png'
        elif self.arrows_left == 2:
            img = 'images/2_arrows.png'
        elif self.arrows_left == 1:
            img = 'images/vertical_arrow.png'

        self.arrows_img  = pygame.image.load(img)
        self.arrows_rect = self.arrows_img.get_rect()

        self.arrows_rect.centerx = self.SCREEN_RECT.centerx
        self.arrows_rect.top     = self.SPACING
        self.SB_CENTER           = self.arrows_rect.centery

    def one_arrow_less(self):
        ''' The user lost one arrow. '''

        self.arrows_left -= 1
        if self.arrows_left > 0:
            self._update_arrows()

    def update_score(self):
        ''' Updates main score components and data. '''

        txt_color = self.tbm.theme_color
        txt = "{:,}".format(self.score)
        self.score_img          = self.FONT.render(txt, True, txt_color,
                                                                  self.BG_COLOR)
        self.score_rect         = self.score_img.get_rect()
        self.score_rect.centery = self.SB_CENTER
        self.score_rect.left    = self.score_rect.top

    def update_hs(self):
        ''' Updates main highest score components and data. '''

        txt_color = self.tbm.theme_color
        txt = "{:,}".format(self.hs)
        self.hs_img          = self.FONT.render(txt, True, txt_color,
                                                                  self.BG_COLOR)
        self.hs_rect         = self.hs_img.get_rect()
        self.hs_rect.centery = self.SB_CENTER
        self.hs_rect.right   = self.SCREEN_RECT.right - self.hs_rect.top

    def update_color(self):
        ''' Updates the object's color. '''
    
        self.sb_line.update_color()
        self.update_score()
        self.update_hs()

    def show(self):
        ''' Shows the statsboard onscreen. '''

        # Statsboard background.
        self.sb_line.show()

        # Stats.
        self.SCREEN.blit(self.score_img, self.score_rect)
        self.SCREEN.blit(self.hs_img, self.hs_rect)
        if self.arrows_left > 0:
            self.SCREEN.blit(self.arrows_img, self.arrows_rect)

class Line:
    ''' An attempt to represent a line. '''

    def __init__(self, tbm, top):
        ''' Initialize main attributes. '''

        self.tbm      = tbm
        self.SCREEN   = tbm.SCREEN
        self.rect     = pygame.Rect(0, 0, tbm.SCREEN_RECT.width, 1)
        self.rect.top = top
        self.color    = tbm.INITIAL_COLOR

    def update_color(self):
        ''' Updates the object's color. '''
    
        self.color = self.tbm.theme_color

    def show(self):
        ''' Shows the line. '''
    
        pygame.draw.rect(self.SCREEN, self.color, self.rect)
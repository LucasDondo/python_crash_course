import pygame
import json
from arrow import Arrow

class Stats:
    ''' All game stats can be found here. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        # Recover highest score.
        try:
            with open(tbm.settings.hs_file) as f:
                self.hs = json.load(f)
        except FileNotFoundError:
            self.hs = 0

        # Statsboard.
        self.screen      = tbm.screen
        self.screen_rect = tbm.screen_rect
        self.font        = tbm.settings.font
        self.txt_color   = tbm.settings.stats_txt_color
        self.bg_color    = tbm.settings.bg_color
        self.spacing     = tbm.settings.sb_spacing
        # Line.
        self.sb_line         = pygame.Rect(0, 0, self.screen_rect.width, 1)
        self.sb_line_y       = tbm.settings.sb_line_y
        self.sb_line.y = self.sb_line_y
        self.sb_line_color   = tbm.settings.sb_line_color

        # Initialize stats.
        self.game_active = False
        self._reset()
    
    def _update_score(self):
        ''' Updates main score components and data. '''
    
        txt = "{:,}".format(self.score)
        self.score_img          = self.font.render(txt, True, self.txt_color
                                                            , self.bg_color)

        self.score_rect         = self.score_img.get_rect()
        self.score_rect.centery = self.sb_line_y / 2
        self.score_rect.left    = self.score_rect.top
    
    def _update_hs(self):
        ''' Updates main highest score components and data. '''
            
        txt = "{:,}".format(self.hs)
        self.hs_img          = self.font.render(txt, True, self.txt_color
                                                         , self.bg_color)
        
        self.hs_rect         = self.hs_img.get_rect()
        self.hs_rect.centery = self.sb_line_y / 2
        self.hs_rect.right   = self.screen_rect.right - self.hs_rect.top

    def one_arrow_less(self):
        ''' The user lost one arrow. '''
    
        self.arrows_left -= 1
        if self.arrows_left > 0:
            self._update_arrows()

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

        self.arrows_rect.centerx = self.screen_rect.centerx
        self.arrows_rect.top     = self.spacing

    def show_sb(self):
        ''' Shows the statsboard onscreen. '''
    
        # Statsboard background.
        pygame.draw.rect(self.screen, self.sb_line_color, self.sb_line)

        # Stats.
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hs_img, self.hs_rect)
        if self.arrows_left > 0:
            self.screen.blit(self.arrows_img, self.arrows_rect)

    def _reset(self):
        ''' Reset all stats. '''
    
        self.arrows_left = 3
        self.score       = 0
        self._update_score()
        self._update_hs()
        self._update_arrows()
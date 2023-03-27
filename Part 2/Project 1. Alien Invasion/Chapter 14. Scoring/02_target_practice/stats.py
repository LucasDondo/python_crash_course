import pygame
import json
class Stats:
    ''' All game stats can be found here. '''

    def __init__(self, tp):
        ''' Initialize main attributes. '''

        # Recover highest score.
        try:
            with open(tp.settings.hs_file) as f:
                self.hs = json.load(f)
        except FileNotFoundError:
            self.hs = 0

        # Scoreboard.
        self.screen = tp.screen
        self.screen_rect = tp.screen_rect
        self.font = tp.settings.font
        self.txt_color = tp.settings.stats_txt_color
        self.bg_color = tp.settings.bg_color

        # Initialize stats.
        self._reset()
        self.game_active = False
    
    def _update_score(self):
        ''' Updates main score components and data. '''
    
        txt = "{:,}".format(self.score)
        self.score_img = self.font.render(txt, True, self.txt_color,
                                          self.bg_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = 20
        self.score_rect.top = 20
    
    def _update_hs(self):
        ''' Updates main highest score components and data. '''
            
        txt = "{:,}".format(self.hs)
        self.hs_img = self.font.render(txt, True, self.txt_color, self.bg_color)

        self.hs_rect = self.hs_img.get_rect()
        self.hs_rect.right = self.screen_rect.right - 20
        self.hs_rect.top = 20

    def _update_arrows(self):
        ''' Updates the arrows left. '''
    
        if self.arrows_left == 3:
            img = 'images/3_arrows.png'
        elif self.arrows_left == 2:
            img = 'images/2_arrows.png'
        elif self.arrows_left == 1:
            img = 'images/vertical_arrow.png'
            
        self.arrows_img = pygame.image.load(img)
        self.arrows_rect = self.arrows_img.get_rect()

        self.arrows_rect.centerx = self.screen_rect.centerx
        self.arrows_rect.top = 20

    def one_arrow_less(self):
        ''' The user lost one arrow. '''
    
        self.arrows_left -= 1
        if self.arrows_left > 0:
            self._update_arrows()

    def show_sb(self):
        ''' Shows the score onscreen. '''
    
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hs_img, self.hs_rect)
        if self.arrows_left > 0:
            self.screen.blit(self.arrows_img, self.arrows_rect)

    def _reset(self):
        ''' Reset all stats. '''
    
        self.arrows_left = 3
        self.score = 0
        self._update_score()
        self._update_hs()
        self._update_arrows()
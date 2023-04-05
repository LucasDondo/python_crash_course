import pygame

class PlayButton:
    ''' The magic button to start playing. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        self.settings = tbm.settings
        self.screen_rect = tbm.screen_rect
        self.screen = tbm.screen
        self.sb_line_y = self.settings.sb_line_y
        self.center_under_sb = self.sb_line_y + (self.screen_rect.height - self.sb_line_y) / 2
        self.font = tbm.settings.font

        # Button (rect).
        self.width = self.settings.play_button_width
        self.height = self.settings.play_button_height
        self.color = self.settings.play_button_color
        #
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.center_under_sb
        
        # Msg (img).
        self.msg = self.settings.play_button_msg
        self.text_color = self.settings.play_button_text_color
        #
        self.msg_img = self.font.render(self.msg, True, self.text_color,
                                            self.color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.centerx = self.screen_rect.centerx
        self.msg_img_rect.centery = self.center_under_sb
    
    def show(self):
        ''' Shows the rect and the img. '''
    
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
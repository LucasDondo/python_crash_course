import pygame

class PlayButton:
    ''' The magic button to start playing. '''

    def __init__(self, tp):
        ''' Initialize main attributes. '''

        self.settings = tp.settings
        self.screen_rect = tp.screen_rect
        self.screen = tp.screen
        self.font = tp.settings.font

        # Button (rect).
        self.width = self.settings.play_button_width
        self.height = self.settings.play_button_height
        self.color = self.settings.play_button_color
        #
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # Msg (img).
        self.msg = self.settings.play_button_msg
        self.text_color = self.settings.play_button_text_color
        #
        self.msg_img = self.font.render(self.msg, True, self.text_color,
                                            self.color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.screen_rect.center
    
    def show(self):
        ''' Shows the rect and the img. '''
    
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
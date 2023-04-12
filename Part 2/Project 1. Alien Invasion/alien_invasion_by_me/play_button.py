import pygame.font

class PlayButton:

    def __init__(self, ai, msg):
        ''' Initialize play button attributes. '''

        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the play button.
        self.width, self.height = 200, 50
        self.play_button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the play button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The play button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        ''' Turn msg into a rendered image and center text on the button. '''

        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.play_button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_play_button(self):
        ''' Draw blank play button and then draw message. '''
    
        self.screen.fill(self.play_button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
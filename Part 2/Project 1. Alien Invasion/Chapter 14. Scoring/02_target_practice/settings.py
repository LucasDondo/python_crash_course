import pygame

class Settings:
    ''' All game settings can be found here. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        # General.
        self.animation_speed = 1.0
        self.arrow_animation_speed = 5.0
        self.font = pygame.font.SysFont(None, 50)

        # Target.
        self.target_width, self.target_height = 10, 100
        self.target_color = (0, 0, 0)
        self.target_speed = 1.0
        self.speedup_scale = 1.05
        self.target_border_radius = 4

        # Screen.
        self.bg_color = (255, 255, 255)

        # Bow.
        self.bow_speed = 1.0

        # Arrow.
        self.arrow_speed = 3.0

        # Play button.
        self.play_button_msg = "Let's go!"
        self.play_button_width, self.play_button_height = 200, 50
        self.play_button_text_color = (255, 255, 255)
        self.play_button_color = (0, 0, 0)

        # Stats.
        self.stats_txt_color = (0, 0, 0)
        self.hs_file = 'highest_score.json'
        self.sb_spacing = 10
        self.sb_line_color = (0, 0, 0)
        # How many vertical pixels does the scoreboard use?
        # First I need an auxiliary vertical arrow to use it's height, since I
        # cannot use the one from stats.py since that file is run later in
        # target_practice.py
        img = pygame.image.load('images/vertical_arrow.png')
        arrow_rect = img.get_rect()
        #
        self.sb_line_y = arrow_rect.height + 2 * self.sb_spacing
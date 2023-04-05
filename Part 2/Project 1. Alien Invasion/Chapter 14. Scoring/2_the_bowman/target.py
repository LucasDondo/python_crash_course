import pygame

class Target:
    ''' An attempt to represent the target. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        # Made things more accesible.
        self.tbm = tbm
        self.settings = tbm.settings
        self.screen = tbm.screen
        self.screen_rect = tbm.screen_rect
        self.sb_line_y = self.settings.sb_line_y
        self.center_under_sb = self.sb_line_y + (self.screen_rect.height - self.sb_line_y) / 2
        #
        self.width = self.settings.target_width
        self.height = self.settings.target_height
        self.border_radius = self.settings.target_border_radius
        self.color = self.settings.target_color
        self.speed = self.settings.target_speed
        self.animation_speed = self.settings.animation_speed

        # Create and position target.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.center_under_sb
        self.y = float(self.rect.y)
        # 1 = move down; -1 = move up.
        self.movement_direction = 1

        # To move, or not to move, that is the question.
        self.stopped = False

    def center(self):
        ''' Centers in screen. '''
    
        if self.rect.centery < self.center_under_sb:
            self.movement_direction = 1
            while self.rect.centery < self.center_under_sb:
                self.y += self.animation_speed * self.movement_direction
                self.tbm._update_screen()
        elif self.rect.centery > self.center_under_sb:
            self.movement_direction = -1
            while self.rect.centery > self.center_under_sb:
                self.y += self.animation_speed * self.movement_direction
                self.tbm._update_screen()

    def update(self):
        ''' Updates the position. '''
    
        self._check_edges()
        if not self.stopped:
            self.y += self.movement_direction * self.speed

    def _check_edges(self):
        ''' Checks if an edge has been reached. '''
    
        if self.rect.top <= self.sb_line_y or \
        self.rect.bottom >= self.screen_rect.bottom:
            self.movement_direction *= -1

    def draw(self):
        ''' Please draw me. '''

        self.rect.y = self.y
        pygame.draw.rect(self.screen, self.color, self.rect,
                         border_radius=self.border_radius)
import pygame

class Target:
    ''' An attempt to represent the target. '''

    def __init__(self, tbm):
        ''' Initialize main attributes. '''

        # Made things more accesible.
        self.tbm             = tbm
        self.SCREEN          = tbm.SCREEN
        self.SCREEN_RECT     = tbm.SCREEN_RECT
        self.GAME_TOP        = self.tbm.GAME_TOP
        self.CENTER_UNDER_SB = self.GAME_TOP + (self.SCREEN_RECT.height - \
                                                              self.GAME_TOP) / 2
        #
        self.WIDTH, self.height = 10, 200
        self.BORDER_RADIUS      = 4
        self.color              = self.tbm.INITIAL_COLOR
        self.ANIMATION_SPEED    = self.tbm.ANIMATION_SPEED
        self.reset_speed()

        # Create and position target.
        self.rect         = pygame.Rect(0, 0, self.WIDTH, self.height)
        self.rect.right   = self.SCREEN_RECT.right
        self.rect.centery = self.CENTER_UNDER_SB
        self.y            = float(self.rect.y)

        # 1 = move down; -1 = move up.
        self.movement_direction = 1
        # To move, or not to move, that is the question.
        self.stopped = False

    def reset_speed(self):
        self.speed = 1.0

    def update(self):
        ''' Updates the position. '''

        self._check_edges()
        self.y += self.movement_direction * self.speed

    def _check_edges(self):
        ''' Checks if an edge has been reached. '''

        if self.rect.top <= self.GAME_TOP or \
                                    self.rect.bottom >= self.SCREEN_RECT.bottom:
            self.movement_direction *= -1

    def center(self):
        ''' Centers in screen. '''

        if self.rect.centery < self.CENTER_UNDER_SB:
            self.movement_direction = 1
            while self.rect.centery < self.CENTER_UNDER_SB:
                self.y += self.ANIMATION_SPEED * self.movement_direction
                self.tbm.update_screen()
        elif self.rect.centery > self.CENTER_UNDER_SB:
            self.movement_direction = -1
            while self.rect.centery > self.CENTER_UNDER_SB:
                self.y += self.ANIMATION_SPEED * self.movement_direction
                self.tbm.update_screen()

    def update_color(self):
        ''' Updates the object's color. '''
    
        self.color = self.tbm.theme_color

    def show(self):
        ''' Please draw me. '''

        self.rect.y = self.y
        pygame.draw.rect(self.SCREEN, self.color, self.rect,
                                               border_radius=self.BORDER_RADIUS)
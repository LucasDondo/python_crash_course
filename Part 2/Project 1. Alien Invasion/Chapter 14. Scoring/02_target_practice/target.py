import pygame

class Target:
    ''' An attempt to represent the target. '''

    def __init__(self, tp):
        ''' Initialize main attributes. '''

        # Made things more accesible.
        self.tp = tp
        self.screen = tp.screen
        self.screen_rect = tp.screen_rect
        self.settings = tp.settings
        #
        self.width = self.settings.target_width
        self.height = self.settings.target_height
        self.color = self.settings.target_color
        self.speed = self.settings.target_speed
        self.animation_speed = self.settings.animation_speed

        # Create and position target.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)
        # 1 = move down; -1 = move up.
        self.movement_direction = 1

    def center(self):
        ''' Centers in screen. '''
    
        if self.rect.centery < self.screen_rect.centery:
            self.movement_direction = 1
            while self.rect.centery < self.screen_rect.centery:
                self.y += self.animation_speed * self.movement_direction
                self.tp._update_screen()
        elif self.rect.centery > self.screen_rect.centery:
            self.movement_direction = -1
            while self.rect.centery > self.screen_rect.centery:
                self.y += self.animation_speed * self.movement_direction
                self.tp._update_screen()

    def update(self):
        ''' Updates the position. '''
    
        self._check_edges()
        self.y += self.movement_direction * self.speed

    def _check_edges(self):
        ''' Checks if an edge has been reached. '''
    
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_rect.bottom:
            self.movement_direction *= -1

    def draw(self):
        ''' Please draw me. '''

        self.rect.y = self.y
        pygame.draw.rect(self.screen, self.color, self.rect)
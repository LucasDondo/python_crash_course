import sys
import time
import pygame
from settings import Settings
from target import Target
from bow import Bow
from arrow import Arrow
from stats import Stats
from play_button import PlayButton

class TargetPractice:
    ''' Main class for the Target Practice game. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.settings = Settings()
        self.bg_color = self.settings.bg_color
        self.stats = Stats()
        self.game_active = self.stats.game_active

        # Audiovisual elements.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Target Practice')
        #
        pygame.mixer.music.load('sounds/arrow_by_jim_yosef.mp3')

        self.play_button = PlayButton(self)
        self.target = Target(self)
        self.bow = Bow(self)
        self.arrows = pygame.sprite.Group()
        self.nailed_arrows = pygame.sprite.Group()

        self.reset_stopped_time()

    def reset_stopped_time(self):
        ''' Sets stopped_time to 0. '''
        
        self.stopped_time = 0 # Used to stop the target for a second.

    def start(self):
        ''' Starts main class actions. '''

        while True:
            self._check_events()
            self._update_screen()

            if self.game_active:
                pygame.mixer.music.set_volume(1)
                pygame.mouse.set_visible(False)
                if time.time() - self.stopped_time > 1:
                    self.target.stopped = False
                    self.reset_stopped_time()
                self.target.update()
                self.bow.update()
                self._update_arrows()
            
            elif not self.game_active:
                pygame.mixer.music.set_volume(.5)
                pygame.mixer.music.play(fade_ms=2000, start=2.1)
                started_time = time.time()
                self._check_events()
                while time.time() - started_time < 2:
                    self._check_events()
                    continue
                if time.time() - started_time > 2:
                    pygame.mixer.music.fadeout(2000)
                    finished_time = time.time()
                while time.time() - finished_time < 1.7:
                    self._check_events()
                    continue

    def _check_events(self):
        ''' Checks and reacts to kb and mouse events. '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    self.bow.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.bow.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._create_arrow()
                    self._k_space_play_button()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.bow.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.bow.moving_down = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._click_play_button(mouse_pos)

    def _new_game(self):
        ''' Sets everything up to start a new game. '''
    
        # Housekeeping.
        pygame.mouse.set_visible(False)
        self.arrows.empty()
        self.stats._reset()

        # Let's go!
        pygame.mixer.music.play(fade_ms=1000)
        self.game_active = True
        # Animations.
        for arrow in self.nailed_arrows.sprites():
            arrow.fall()
            self._check_events() # To make sure the game doesn't freeze.
                                 # And yes, it's true that this is not as
                                 # instant as it could be, but it creates a
                                 # nice effect.
        self.nailed_arrows.empty()
        self.target.center()
        self.bow.center()

        # I must use this because when this method is called from the
        # _check_events method and that one has been called by the loop from
        # the part of the start method where game_active is False and the music
        # gets repeated again and again, I need to get out of that loop to let
        # the gameplay loop start.
        self.start()

    def _click_play_button(self, mouse_pos):
        ''' Checks if the play button has been clicked. '''
    
        clicked = self.play_button.rect.collidepoint(mouse_pos)
        if clicked and not self.game_active:
            self._new_game()

    def _k_space_play_button(self):
        ''' Creates a new game when space is pressed (and if...). '''
    
        if not self.game_active:
            self._new_game()

    def _create_arrow(self):
        ''' Creates an arrow. '''
    
        # Game must be active and target not stopped.
        if self.game_active and not self.target.stopped:
            new_arrow = Arrow(self)
            self.arrows.add(new_arrow)
    
    def _update_arrows(self):
        ''' Updates everything arrow-related. '''
        
        # Arrows.
        self.arrows.update()
        self._check_collision()
        self._del_old_arrows()

        # Nailed arrows.
        for arrow in self.nailed_arrows.sprites():
            arrow.move_as_target(self.target.movement_direction)

    def _check_collision(self):
        ''' Checks and reacts to collisions between arrows and the target. '''
    
        arrow_shot = pygame.sprite.spritecollideany(self.target, self.arrows)
        if arrow_shot:
            self.target.stopped = True
            self.stopped_time = time.time()
            self.arrows.remove(arrow_shot)
            self.nailed_arrows.add(arrow_shot)

    def _del_old_arrows(self):
        ''' Deletes arrows that are out of the screen. '''
    
        for arrow in self.arrows.sprites():
            if arrow.rect.left > self.screen_rect.right:
                self.arrows.remove(arrow)

                # The user lost the shot.
                self.stats.one_arrow_less()

                # Check if the game goes on.
                if self.stats.arrows_left <= 0:
                    pygame.mixer.music.fadeout(500)
                    pygame.mouse.set_visible(True)
                    self.game_active = False

    def _update_screen(self):
        ''' Display main game elements. '''
    
        self.screen.fill(self.bg_color)
        self.target.draw()
        self.bow.blit()
        for arrow in self.arrows.sprites():
            arrow.blit()
        for arrow in self.nailed_arrows.sprites():
            arrow.blit()
        if not self.game_active:
            self.play_button.show()
        pygame.display.flip()

if __name__ == '__main__':
    # Creates an instance and runs it.
    tp = TargetPractice()
    tp.start()
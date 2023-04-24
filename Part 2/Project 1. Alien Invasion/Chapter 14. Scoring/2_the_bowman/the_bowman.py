import sys
import time
import pygame
import json

from settings import Settings
from target import Target
from bow import Bow
from arrow import Arrow
from stats import Stats
from play_button import PlayButton

class TheBowman:
    ''' Main class for the The Bowman game. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.settings = Settings()
        self.bg_color = self.settings.bg_color

        # Audiovisual elements.
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('🏹 The Bowman 🏹')
        #
        pygame.mixer.music.load('sounds/arrow_by_jim_yosef.mp3')

        self.target = Target(self)
        self.bow = Bow(self)
        self.stats = Stats(self)
        self.game_active = self.stats.game_active
        self.play_button = PlayButton(self)
        self.speedup_scale = self.settings.speedup_scale
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
                self._exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    self._exit_game()
                elif event.key == pygame.K_UP:
                    self.bow.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.bow.moving_down = True
                elif event.key == pygame.K_SPACE:
                    if self.game_active and not self.target.stopped:
                        self._create_arrow()
                    elif not self.game_active:
                        self._new_game()
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
        self.target.speed = self.settings.target_speed

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

    def _create_arrow(self):
        ''' Creates an arrow. '''
    
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
        if arrow_shot and arrow_shot.rect.right < self.screen_rect.right and \
        self.target.rect.top < arrow_shot.rect.centery < self.target.rect.bottom:
            self.target.stopped = True
            self.stopped_time = time.time()
            self.arrows.remove(arrow_shot)
            self.nailed_arrows.add(arrow_shot)
            self.target.speed *= self.speedup_scale
            self.stats.score += len(self.nailed_arrows) # Nailed arrows = level.
            self.stats._update_score()
            if self.stats.score > self.stats.hs:
                self.stats.hs = self.stats.score
                self.stats._update_hs()

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
        self.stats.show_sb()
        pygame.display.flip()

    def _exit_game(self):
        ''' Housekeeping and exiting. '''

        with open(self.settings.hs_file, 'w') as f:
            json.dump(self.stats.hs, f)
        sys.exit()

if __name__ == '__main__':
    # Creates an instance and runs it.
    tbm = TheBowman()
    tbm.start()
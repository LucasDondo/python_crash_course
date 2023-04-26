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

        # 📺 Screen.
        self.bg_color    = self.settings.bg_color
        self.screen      = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('🏹 The Bowman 🏹')

        # 🎵 Music.
        pygame.mixer.music.load('sounds/arrow_by_jim_yosef.mp3')

        self.stats         = Stats(self)
        self.target        = Target(self)
        self.bow           = Bow(self)
        self.game_active   = self.stats.game_active
        self.play_button   = PlayButton(self)
        self.speedup_scale = self.settings.speedup_scale
        self.arrows        = pygame.sprite.Group()
        self.nailed_arrows = pygame.sprite.Group()

        self.stopped_time = 0 # Initialize var.

    def start(self):
        ''' Starts main class actions. '''

        while True:
            self._check_events()
            self._update_screen()

            if self.game_active:
                # 🎯 Target.
                if time.time() - self.stopped_time > 1:
                    self.target.stopped = False
                    self.target.update()
                # 🏹 Bow & arrows.
                self.bow.update()
                self._update_arrows()
            
            else:
                # 🎵 Lobby music loop.
                finished_time = 0 # Initialize var.

                # 📈 Incrementing.
                pygame.mixer.music.set_volume(.5)
                pygame.mixer.music.play(fade_ms=2000, start=2.1)
                started_time = time.time()
                # ⌚ Wait.
                while (time.time() - started_time) < 2:
                    self._check_events()
                    if self.game_active:
                        break # ... from while loop.

                # All the breaks and this if are to avoid unnecessary steps when
                # _check_events() recorded a K_SPACE that starts the game.
                if not self.game_active:
                    # 📉 Decrementing.
                    pygame.mixer.music.fadeout(2000)
                    finished_time = time.time()
                    # ⌚ Wait.
                    while (time.time() - finished_time) < 1.7:
                        self._check_events()
                        if self.game_active:
                            break # ... from while loop.

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
    
        # 🏠 Housekeeping.
        pygame.mouse.set_visible(False)
        pygame.mixer.music.set_volume(1)
        self.arrows.empty()
        self.stats._reset()
        self.target.speed = self.settings.target_speed

        self.game_active = True

        # 💨 Animations.
        for arrow in self.nailed_arrows.sprites():
            arrow.fall()
        self.nailed_arrows.empty()
        self.target.center()
        self.bow.center()

        # 🎵 Music, please!
        pygame.mixer.music.play(fade_ms=1000)

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
                    pygame.mouse.set_visible(True)
                    pygame.mixer.music.fadeout(500)
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
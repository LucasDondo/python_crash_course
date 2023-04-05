''''
Note #1: It's important to note that when you delete a key from a dictionary,
         you're only deleting the reference to the list object, not the list
         object itself. If the list object is not referenced by any other
         variables or objects, then it will eventually be garbage collected by
         Python. However, if the list object is still referenced elsewhere in
         your code, then it will not be garbage collected and will continue to
         exist even after you delete the reference to it in the dictionary.

         If the elements in the list are objects that are also in a PyGame
         sprite group, then the `del` operation on the dictionary will not
         remove those objects from the sprite group. The objects will remain in
         the sprite group until they are explicitly removed from it using the
         remove method or until the group is cleared.

Note #2: `messy_rain`? `messi_rain`? `messi`? `Messi`? `Messi ⭐⭐⭐`?
         `🇦🇷 Messi ⭐⭐⭐`?
'''

import sys
import pygame
import random
from settings import Settings
from raindrop import Raindrop

class MessyRain():
    ''' An attempt to represent rain. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('🌧️ Messy Rain ☔')

        self.settings = Settings()

        self.rds = pygame.sprite.Group()
        self.row_id = 0
        self.rows = {} # Id : Row's list
        self.deleted_rows = 0 # Synced w/ row's ids.

    def _create_row(self):
        ''' Creates a row of raindrops. '''

        self.row_id += 1
        row = []
    
        rd = Raindrop(self)
        rd_width = rd.rect.width
        spacing = rd_width // 2
        available_space_side = self.screen_rect.width // 2 - rd_width // 2 - \
                               spacing
        available_rds_side = available_space_side // (spacing + rd_width)
        mid_screen = self.screen_rect.width // 2

        # Middle rd.
        show_md_rd = random.choice([True, False])
        if show_md_rd:
            rd.rect.centerx = self.screen_rect.centerx
            self.rds.add(rd)
            row.append(rd)

        # Right rds.
        for rd in range(available_rds_side):
            count = rd
            show = random.choice([True, False])
            if show:
                rd = Raindrop(self)
                rd.rect.left = (mid_screen + rd_width // 2 + spacing) + \
                               count * (rd_width + spacing)
                self.rds.add(rd)
                row.append(rd)

        # Left rds.
        for rd in range(available_rds_side):
            count = rd
            show = random.choice([True, False])
            if show:
                rd = Raindrop(self)
                rd.rect.right = (mid_screen - rd_width // 2 - spacing) - \
                                count * (rd_width + spacing)
                self.rds.add(rd)
                row.append(rd)

        # Position on the top of the screen.
        for rd in row:
            rd.rect.bottom = 0

        self.rows[self.row_id] = row

    def _check_events(self):
        ''' Checks for and reacts to keyboard and mouse inputs. '''
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _renew_rds(self):
        ''' Deletes raindrops that got to the floor and creates new rows. '''

        try:
            # Remove old rds.
            oldest_row = list(self.rows.values())[0]
            old_rd = oldest_row[0] # I just need one, it doesn't matter which one.
            #
            if old_rd.fell():
                for rd in oldest_row: # See Note #1.
                    self.rds.remove(rd)
                self.deleted_rows += 1
                del self.rows[self.deleted_rows]
            
            # Create new row.
            newest_row = list(self.rows.values())[-1]
            new_rd = newest_row[-1]
            spacing = new_rd.rect.height * 1.5
            #
            if new_rd.rect.top >= spacing:
                self._create_row()
        except IndexError:
            pass

    def _update_screen(self):
        ''' Updates the main screen components. '''
    
        self.screen.fill((19, 63, 91))
        for rd in self.rds.sprites():
            rd.blitme()
        pygame.display.flip()

    def start(self):
        ''' Starts the main loop. '''
    
        self._create_row()
        while True:
            self._check_events()
            self._renew_rds()
            self.rds.update()
            self._update_screen()

if __name__ == '__main__':
    # Creates an instance and runs it.
    sr = MessyRain()
    sr.start()
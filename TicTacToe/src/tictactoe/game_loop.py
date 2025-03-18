'''game_loop.py'''

import sys

import pygame
import pygame.locals

class GameLoop:
    '''
    This class is responsible for running the game loop.
    '''

    def __init__(self, screen):
        self.screen = screen

    def run(self):
        while True:
            self._refresh_screen()

            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    pygame.quit()
                    sys.exit()

    def _refresh_screen(self):
        self.screen.fill((0,0,0))
        pygame.display.update()

"""
Turn based battle game template
For learning to grab images from a sprite sheet
And ideally for use in later projects
"""

import sys
import pygame as pg
from settings import *
from game_objects.units import BattleGroup


class Battle:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create resources"""
        pg.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Battle")

        self.battle_group = BattleGroup(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        # Draw the sample unit in its current position
        self.battle_group.units[0].blitme()
        pg.display.flip()


if __name__ == "__main__":
    battle_game = Battle()
    battle_game.run_game()


"""Module to represent the set of combatants in a battle"""

import os
import pygame as pg
from settings import *
from game_objects.spritesheet import SpriteSheet


class BattleGroup:
    """Represents the order of battle for a group of combatants
    Each combatant is a member of the Unit class"""

    def __init__(self, battle_game):
        """Initialize attributes to represent the set of combatants in the battle"""

        self.battle_game = battle_game
        self.units = []
        self._load_units()

    def _load_units(self):
        """Builds the overall set:
        - Loads images from the sprite sheet
        - Creates a Unit object, and sets appropriate attributes for that unit
        - Adds each unit to the group self.units
        """

        filepath = FE8_MAP_SPRITE_PATH
        unit_sprite_sheet = SpriteSheet(filepath)

        # create a unit
        # x_pos = 16 + 1
        # y_pos = 6 + 32 + 1 + 1
        ephraim_rect = (16, 39, 32, 32)
        ephraim_img = unit_sprite_sheet.image_at(ephraim_rect)

        ephraim = Unit(self.battle_game)
        ephraim.image = ephraim_img
        ephraim.name = "Ephraim"
        ephraim.color = "blue"
        self.units.append(ephraim)


class Unit:
    """Represents a combatant"""
    def __init__(self, battle_game):
        """Initialize attributes to represent the combatant"""
        self.image = None
        self.name = ""
        self.color = ""

        self.screen = battle_game.screen

        # Place each unit initially in the top left corner
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        """Draw the piece at its current location"""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)


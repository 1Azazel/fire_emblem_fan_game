import pygame as pg


class Tile:
    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y
        self.tile_type = tile_type
        self.tile_mods = self.check_tile_mods()

    def check_tile_mods(self):
        return self.tile_type

    def set_pos(self, new_pos):
        if new_pos is type(pg.Vector2):
            self.x = new_pos.x
            self.y = new_pos.y
        else:
            self.x, self.y = new_pos[0], new_pos[1]

    def get_pos(self):
        return pg.Vector2(self.x, self.y)

    def get_tile_image(self):
        if self.tile_type is "fort":
            return "fort.png"

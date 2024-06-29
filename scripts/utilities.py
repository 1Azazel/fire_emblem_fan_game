import pygame as pg
from settings import *


def init():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    font = pg.font.Font(None, FONT_SIZE)
    running = True
    return screen, clock, font, running


def load_sprite(path):
    sprite_sheet = pg.image.load(path)
    return sprite_sheet


def get_sprite(x, y, width, height, sheet):
    sprite = pg.Surface([width, height])
    sprite.blit(sheet, (0, 0), (x, y, width, height))
    sprite.set_colorkey((0, 0, 0))  # Assuming black is your transparent colour
    return sprite



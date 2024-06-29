# settings.py
import pygame.color

# Screen Dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
ORIGIN = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Font Size
FONT_SIZE = 20

# Frame Rate
TICK = 120

# File Path for map sprites
FE6_MAP_SPRITE_PATH = r"assets/map sprites/Game Boy Advance - Fire Emblem The Binding Blade JPN - Map Sprites.png"
FE7_MAP_SPRITE_PATH = r"assets/map sprites/Game Boy Advance - Fire Emblem The Blazing Blade - Map Sprites.png"
FE8_MAP_SPRITE_PATH = r"C:\Users\xxpun\Documents\GitHub\fire_emblem_fan_game\assets\map sprites\Game Boy Advance - Fire Emblem The Sacred Stones - Map Sprites.png"

# Size of FE Sprite:
SPRITE_WIDTH = 32
SPRITE_HEIGHT = 32

# Some values for the FE8 Sprite Sheet in particular
SPRITE_SHEET_X_OFFSET = 16
SPRITE_SHEET_Y_OFFSET = 6

# Sprite Sheet Color:
sprite_color = pygame.color.Color("#80A080")
SPRITE_BG_COLOR = (sprite_color.r, sprite_color.g, sprite_color.b, sprite_color.a)

# Default Background
DEFAULT_BACKGROUND_PATH = r"assets/battle maps/Game Boy Advance - Fire Emblem The Sacred Stones - Tower of Valni I.png"


class Settings:
    def __init__(self):
        self.screen_width, self.screen_height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.bg_color = SPRITE_BG_COLOR

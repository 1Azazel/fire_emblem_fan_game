import pygame
import csv
from settings import *
from scripts.utilities import load_sprite, get_sprite

fe6_sheet = load_sprite(FE6_MAP_SPRITE_PATH)
fe7_sheet = load_sprite(FE7_MAP_SPRITE_PATH)
fe8_sheet = load_sprite(FE8_MAP_SPRITE_PATH)

win_width, win_height = 800, 600  # Adjust to desired window dimensions
half_width = win_width // 2
win = pygame.display.set_mode((win_width + half_width, win_height))
bg = pygame.image.load(FE8_MAP_SPRITE_PATH)  # add your spritesheet path
bg_rect = bg.get_rect()  # Get the dimensions of your sprite sheet

drag = False
running = True
sx, sy = 0, 0
sprite_positions = []
sprite_bin = []

scroll_y = 0  # Initialize scroll_y variable
zoom = 1.0

while running:
    dy = dz = 0
    ex, ey = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:  # detect dragging start
            if event.button == 1:
                drag = True
                sx, sy = pygame.mouse.get_pos()
                sy += scroll_y  # Adjust for scroll position
            if half_width < ex < half_width * 2:  # deletion zone
                px, py, = pygame.mouse.get_pos()
                # check and remove sprite_positions
                for pos in sprite_positions[::-1]:
                    if pos['top_left'][0] < px - half_width < pos['bottom_right'][0] and pos['top_left'][1] < py < \
                            pos['bottom_right'][1]:
                        sprite_positions.remove(pos)
                        break

        if event.type == pygame.MOUSEBUTTONUP:  # detect dragging stop
            if event.button == 1:
                drag = False
                ex, ey = pygame.mouse.get_pos()
                ey += scroll_y  # Adjust for scroll position
                sprite_positions.append({'top_left': (sx, sy), 'bottom_right': (ex, ey)})

        elif event.type == pygame.MOUSEWHEEL:
            dy = event.y  # Get mouse wheel scroll amount
            dz = -event.y  # Invert y-axis for zoom

        scroll_y += dy * 10  # Update scroll position
        zoom += dz * 0.1
        zoom = max(0.1, zoom)  # prevent inverted view

        scroll_y = min(0, scroll_y)  # Restrict scrolling above spritesheet
        scroll_y = max(-(bg_rect.height * zoom - win_height), scroll_y)  # Restrict scrolling below spritesheet

        win.fill((0, 0, 0))  # Fill screen with black to prevent sprite drawing overlap

        surf = pygame.transform.scale(bg, (int(bg_rect.width * zoom), int(bg_rect.height * zoom)))  # scale the images
        win.blit(surf, (0, scroll_y))  # Draw the background sprite sheet on the screen

        sprite_bin = [pygame.transform.scale(pygame.Surface((abs(pos['bottom_right'][0] - pos['top_left'][0]),
                                                             abs(pos['bottom_right'][1] - pos['top_left'][1]))),
                                             (int(abs(pos['bottom_right'][0] - pos['top_left'][0]) * zoom),
                                              int(abs(pos['bottom_right'][1] - pos['top_left'][1]) * zoom)))
                      for pos in sprite_positions]

    if drag:
        pygame.draw.rect(win, (0, 255, 0), pygame.Rect(sx, sy - scroll_y, ex - sx, ey + scroll_y - sy), 2)

    bin_y = 10
    for sprite in sprite_bin:
        win.blit(sprite, (win_width + 10, bin_y))
        bin_y += sprite.get_height() + 10  # place new sprite below the old one

    pygame.display.flip()

# Save the sprite_positions to a csv file
with open('sprite_positions.csv', 'w', newline='') as csvfile:
    fieldnames = ['top_left', 'bottom_right']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for pos in sprite_positions:
        writer.writerow(pos)

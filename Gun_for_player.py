import pygame
start_x, start_y = 0, 0
def call_test(surface, end_x, end_y):
    global start_x, start_y
    pygame.draw.rect(surface, (139, 69, 19), (start_x, start_y, 50, 50))
    dx, dy = (end_x - start_x, end_y - start_y)
    stepx, stepy = (dx * .05, dy * .05)
    start_x += stepx
    start_y += stepy


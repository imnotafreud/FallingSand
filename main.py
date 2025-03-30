import pygame
import sys
from const import *
from grid import Grid
pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("FALLING SAND")

clock = pygame.time.Clock()
grid = Grid(WINDOW_WIDTH,WINDOW_WIDTH, CELL_SIZE)

#simulation loop

while True:

#       EVENT HANDLERS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


#           DRAWING
    window.fill(GREY)
    grid.draw(window)
    pygame.display.flip()
    clock.tick(FPS)
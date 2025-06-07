import pygame
from const import *
from simulation import Simulation

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("FALLING SAND")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

#simulation loop
while True:
#       EVENT HANDLERS
    simulation.handleControls()

#           UPDATE
    simulation.update()

#           DRAWING
    window.fill(GREY)
    simulation.draw(window)

    pygame.display.flip()
    clock.tick(FPS)
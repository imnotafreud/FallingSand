from grid import Grid
from particle import SandParticle
import pygame, sys

class Simulation():
    def __init__(self, width, height, cellsize):
        self.grid = Grid(width, height, cellsize)
        self.cellSize = cellsize

    def draw(self, window):
        self.grid.draw(window)

    def addParticle(self, row, column):
        self.grid.addParticle(row, column, SandParticle)

    def removeParticle(self, row, column):
        self.grid.removeParticle(row, column)

    def update(self):
        for row in range(self.grid.rows -2, -1, -1):
            for column in range(self.grid.columns):
                particle = self.grid.getCell(row, column)
                if particle is not None:
                    new_pos = particle.update(self.grid, row, column)
                    if new_pos != (row, column):
                        self.grid.setCell(new_pos[0], new_pos[1], particle)
                        self.grid.removeParticle(row, column)

    def restart(self):
        self.grid.clear()

    def handleControls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handleKey(event)
        self.handleMouse()


    def handleKey(self, event):
        if event.key == pygame.K_SPACE:
            self.restart()
        elif event.key == pygame.K_s:
            print("Sand Mode")
        elif event.key == pygame.K_r:
            print("Rock Mode")
        elif event.key == pygame.K_e:
            print("Eraser Mode")

    def handleMouse(self):
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            pos = pygame.mouse.get_pos()
            row = pos[1] // self.cellSize
            column = pos[0] // self.cellSize
            self.addParticle(row, column)
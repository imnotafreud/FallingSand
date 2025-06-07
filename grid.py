from const import *
import pygame
from particle import *

class Grid:
    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        #print("rows ", self.rows)
        self.columns = width // cell_size
        #print("columns ", self.columns)
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]
        self.color = (0,0,0)

    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                particle = self.cells[row][column]
                if particle is not  None:
                    color = particle.color
                    pygame.draw.rect(window, color,(column * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size ))

    def isCellValid(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            return True
        return False

    def addParticle(self, row, column, particleType):
        if self.isCellValid(row, column):
            self.cells[row][column] = particleType()

    def removeParticle(self, row, column):
        if self.isCellValid(row, column):
            self.cells[row][column] = None

    def isCellEmpty(self, row, column):
        if self.isCellValid(row, column):
            if self.cells[row][column] == None:
                return True
        return False

    def setCell(self, row, column, particle):
        if not(0 <= row < self.rows and 0 <= column < self.columns):
            return
        self.cells[row][column] = particle

    def getCell(self, row, column):
        if self.isCellValid(row, column):
            return self.cells[row][column]
        return None

    def clear(self):
        self.cells = [[None for _ in range(self.columns)] for _ in range(self.rows)]

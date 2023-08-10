from Variables import *
import pygame
class pixel:   

    height = 2
    width = 10

    def __init__(self, x, y):
        self.x  = x
        self.y = y

    def drawPixel(self, surface):
        surface.set_at(((int)(self.x), (int)(self.y)), BLACK)  

    def drawRect(self, surface):
        rectangle = Rect((int)(self.x), (int)(self.y), self.width, self.height)
        pygame.draw.rect(surface, BLACK, rectangle)

    def updateCoord(self, x):
        self.x = x

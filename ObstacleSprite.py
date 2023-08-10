import pygame
from RandomGeneration import *
from pygame.locals import *

class Obstacle:
    def __init__(self, screenheight, screenwidth, imagefile):

        self.shape = pygame.image.load(imagefile)
        self.height = GenRandomYOb(50, 150)
        self.length = GenRandomXOb(40, 110)
        self.shape = pygame.transform.scale(self.shape, (self.length, self.height))
        self.top = screenheight
        self.left = screenwidth


    def Show(self, surface): 
        surface.blit(self.shape, (self.left, self.top))

    #the first parameter is always the instance the method is called on (self)
    def UpdateCoords(self, y):
        self.left = y

    def UpdateY(self, x):
        self.top = x
    

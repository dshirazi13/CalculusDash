import pygame
import random

#if you only import the module itself without the from keyword, you have to call its methods with the class name in front of it
from random import *
#if you import all the methods from a module, you can call them without the class keyword
from pygame.locals import *
from Variables import *

#Base character will be a 3 pixel radius circle
#Easter eggs can be coded in later
class Character:

    accel_x = 0
    accel_y = 0
    x_change = 0
    y_change = 0

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def drawCircle(self, surface):
        pygame.draw.circle(surface, RED, (self.X, self.Y), 9) 

    def drawCircl(self, surface, X, Y):
        pygame.draw.circle(surface, RED, (X, Y), 9)

    def Show(self, surface):
        surface.blit(self.shape, (self.top, self.left))

    def UpdateCoords(self, x):
        self.left = x-self.shape.get_width()/2


   
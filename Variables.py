from ObstacleSprite import *
from pygame.locals import *

ObstacleXFloor = 1
ObstacleXCeiling = 15
HeroX = 100
HeroY = 500
Speed = 100
TimeBetweenDrop = 6
Beginning = True
Gaming = False
Dead = False
bg_speed = 10
deviousbg_speedY = 10
totalArcLength = 0
totalVolume = 0

NumOb = 12

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
ObstacleImg = "./backgrounds/EVIL.png"
Obstacles = [] #you don't need to define the type of list, because you were providing an iterable when you weren't supposed to
#you are supposed to put iterables in the brackets, and Obstacles aren't an iterable
Pixels = [] # would this work for pixels in the line as well? 
DeviousObstacles = []

y_change = 0
accel_y = 0
max_speed_V = 30

x_change = 0
accel_x = 0
max_speed_H = 30

DeathMessage = "You have fallen"

s = 'sound'
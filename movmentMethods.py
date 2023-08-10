import pygame
import Variables
from RandomGeneration import *
from ObstacleSprite import *
from pygame.locals import *
from CharacterSprite import *
from FunctionLine import* 


class ScrollingBackground:

    def __init__(self, screenheight, imagefile):

        self.img = pygame.image.load(imagefile)
        self.coord = [0, 0]
        self.coord2 = [0, -screenheight]
        self.y_original = self.coord[1]
        self.y2_original = self.coord2[1]

    def MakeNewOb():
        pos = GenRandomXOb(-8, 780)
        if (len(Obstacles) < Variables.NumOb):
            ob = Obstacle(pos, 1400, ObstacleImg)
            Obstacles.append(ob) 
        else:
            for obstacle in Obstacles:
                if (obstacle.left <= -100):
                    Obstacles.remove(obstacle)

    def MakeNewPixel(character): 
        pix = pixel(character.X - 9, character.Y)
        Pixels.append(pix)
        for pix in Pixels: #condition that the pixel is going out of the screen
            if(pix.x <=0):
                Pixels.remove(pix)
      
        
    def DropOb(surface):
        for ob in Obstacles:
            ob.Show(surface)

        for obstacle in Obstacles:
            left = obstacle.left
            #top -= 40
            obstacle.UpdateCoords(left-bg_speed)
            #the screen is generated with the top left corner being 0, 0, so you need to add to the y coordinate to make the
            #object go downward

        for pix in Pixels:
            #pix.drawPixel(surface)
            pix.drawRect(surface)

        for pix in Pixels:
            initXPixelValue = pix.x
            #top -= 40
            pix.updateCoord(initXPixelValue-10)
            #the screen is generated with the top left corner being 0, 0, so you need to add to the y coordinate to make the
            #object go downward
            
        for pix in Pixels: #condition that the pixel is going out of the screen
            if(pix.x <=0):
                Pixels.remove(pix)

    def UpdateObPos(Character):
        Character.X -= 5
        if(Character.X <= 109):
            Character.X = 109
    

    def CheckCollisions(Character, Obstacles, DeviousObstacles):
        #if (len(Obstacles) > 0):
            for obstacle in Obstacles:
                if (Character.Y - 9 > obstacle.top and Character.Y + 9 < obstacle.top + obstacle.height):
                    if (Character.X + 9 < obstacle.left + obstacle.length and Character.X - 9 > obstacle.left):
                        return True
            
            for obstacle in DeviousObstacles:
                if (Character.Y - 9 > obstacle.top and Character.Y + 9 < obstacle.top + obstacle.height):
                    if (Character.X + 9 < obstacle.left + obstacle.length and Character.X - 9 > obstacle.left):
                        return True

    def CreateDeviousObject():
        pos = GenRandomXOb(-8, 780)
        if (len(DeviousObstacles) < (Variables.NumOb/2)):
            ob = Obstacle(pos, 1400, ObstacleImg)
            DeviousObstacles.append(ob) 
        else:
            for obstacle in DeviousObstacles:
                if (obstacle.left <= -100):
                    DeviousObstacles.remove(obstacle)
        
    def MoveDeviousObject(surface):
        for ob in DeviousObstacles:
            ob.Show(surface)

        for obstacle in DeviousObstacles:
            left = obstacle.left - bg_speed
            top = obstacle.top - Variables.deviousbg_speedY
            #top -= 40
            obstacle.UpdateCoords(left)
            obstacle.UpdateY(top)

            if(top < 0 or top > 770):
                Variables.deviousbg_speedY *= -1
            
            #the screen is generated with the top left corner being 0, 0, so you need to add to the y coordinate to make the
            #object go downward
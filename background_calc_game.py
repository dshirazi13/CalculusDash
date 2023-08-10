import math
from pygame.locals import * 
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
#from main import *
import Variables





scalefactor = 1000 #thousands of pixels


class calc: 
  def refreshScoreVolume(Character): 
        Variables.totalVolume += ((780 - Character.Y)/scalefactor)
  
  def f(dydx): 
    return math.sqrt(1+(dydx ** 2))

  def arcLengthRefresh(Character): 
      initYCoorPlayer = Character.Y # initial y value
      finalYCoorPlayer = Character.Y # final y value
      changeX = Variables.bg_speed #change in x over the time interval
      changeY = finalYCoorPlayer - initYCoorPlayer # change in y over the time interval
      dydx = changeY/changeX
      x = sy.Symbol("x")
      Variables.totalArcLength += (sy.integrate(calc.f(dydx), (x, 0, changeX)))

  def DisplayPolarFunction(screen, Character, font):
    Magnitude = math.sqrt( ((Character.X - 0)**2) + ((Character.Y - 780)**2))
    Rad = np.arctan((780 - Character.Y)/(Character.X - 0))
    Angle = np.rad2deg(np.arctan((780 - Character.Y)/(Character.X - 0)))
    MEquation = "R = " + str(round(Magnitude, 2))
    Timer = font.render(MEquation, True, (0, 0, 0))
    AExpression = "Θ = " + str(round(Angle, 2))+"°"
    RExpression = "Radians = " + str(round(Rad, 2))
    Ang = font.render(AExpression, True, (0, 0, 0))
    Radians = font.render(RExpression, True, (0, 0, 0))
    screen.blit(Timer, (1050, 45))
    screen.blit(Ang, (1050, 65))
    screen.blit(Radians, (1050, 85))

  def DisplayVectorFunction(screen, Character, font):
    PositionFunction = "▲X = " + str((int)(Character.X)) +"i + " + str((int)(780 - Character.Y)) +"j"
    VelocityFunction = "V = " +str((int)(Character.x_change)) + " dx/dt + " + str( -1 * (int)(Character.y_change)) + " dy/dt"
    AccelerationFunction = "a = " + str((Character.accel_x)) + " d^2x/dt^2 + "+ str( -1 *(Character.accel_y)) + " d^2y/dt^2"
    Pos = font.render(PositionFunction, True, (0, 0, 0))
    Vel = font.render(VelocityFunction, True, (0, 0, 0))
    Acel = font.render(AccelerationFunction, True, (0, 0, 0))
    screen.blit(Pos, (1050, 125))
    screen.blit(Vel, (1050, 145))
    screen.blit(Acel, (1050, 165))

  def DisplayScore(screen, font):
      Inte = "Integral = " + str((int)(Variables.totalVolume)) + " in thousands of pixels"
      Arc = "Arc Length = " + str((int)(Variables.totalArcLength)) + " in pixels"
      Integ = font.render(Inte, True, (0, 0, 0))
      ArcL = font.render(Arc, True, (0, 0, 0))
      screen.blit(Integ, (950, 190))
      screen.blit(ArcL, (950, 210))


  def DeathMessage(screen, font):
    DM = font.render(Variables.DeathMessage, True, (255, 0, 0))
    screen.blit(DM, (600, 350))
    Inte = "Integral = " + str((int)(Variables.totalVolume)) + " in thousands of pixels"
    Arc = "Arc Length = " + str((int)(Variables.totalArcLength)) + " in pixels"
    Integ = font.render(Inte, True, Variables.RED)
    ArcL = font.render(Arc, True, Variables.RED)
    screen.blit(Integ, (600, 370))
    screen.blit(ArcL, (600, 390))

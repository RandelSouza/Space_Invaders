import pygame, sys, os
from pygame.locals import *

class Ship(object):
def __init__(self, x, y, width, height, speed, screen):
self.screen = screen
self.images = []
self.speed = speed
self.setWidthAndHeight( width, height )
self.setXandY(x, y)

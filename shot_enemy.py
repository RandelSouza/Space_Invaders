import pygame, sys, os, random
from pygame.locals import *
from setup import *

class ShotEnemy(object):
def __init__(self):
self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("image/shot_red.png").convert_alpha(), (25,25)), 180)
self.image2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("image/shot_yellow.png").convert_alpha(), (25,25)), 180)

from setup import *
import pygame, sys, os
from pygame.locals import *

class Screen(object):
def __init__(self):
self.init = pygame.init()
self.screen = pygame.display.set_mode([LARGURA, ALTURA])
self.background =  pygame.image.load("scenarios/back_3.png").convert()

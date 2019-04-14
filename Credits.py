from setup import *
import pygame, sys, os
from pygame.locals import *

class Credits(Object):
    def __init__( self ):
        self.init = pygame.init()
        self.font =  pygame.font.Font(None, 80)

from setup import *
import pygame, sys, os
from pygame.locals import *

class Menu( object ):
def __init__( self ):
self.init = pygame.init()
self.font =  pygame.font.Font(None, 80)
self.screen = pygame.display.set_mode( [ LARGURA, ALTURA ] )
self.background =  pygame.image.load( "image/menu1.png" ).convert()
self.fps = pygame.time.Clock().tick( 60 )
pygame.font.init()
self.collors = { "white": (255, 255, 255), "green": (0, 255, 0) }
self.options = []
self.menuOptionsFonts()

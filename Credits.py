from setup import *
import pygame, sys, os
from pygame.locals import *

class Credits( object ):
    def __init__( self ):
        self.init = pygame.init()
        self.font =  pygame.font.Font(None, 80)
        self.screen = pygame.display.set_mode( [ LARGURA, ALTURA ] )
        pygame.font.init()

    def drawAndUpdateCredits( self ):
        #self.screen.blit( self.background, ( 0, 0 ) )
        self.screen.fill( (0, 0, 0) )
        pygame.display.update()

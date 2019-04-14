from setup import *
import pygame, sys, os
from pygame.locals import *

class Credits( object ):
    def __init__( self ):
        self.init = pygame.init()
        self.font =  pygame.font.Font(None, 80)
        self.screen = pygame.display.set_mode( [ LARGURA, ALTURA ] )
        pygame.font.init()

    def eventQuitCredits(self, event):
        if event.type == QUIT:
            exit()

    def eventHandlerCredits( self ):
        for event in pygame.event.get():
            eventQuitCredits(event)

    def drawAndUpdateCredits( self ):
        eventHandlerCredits()
        self.screen.fill( (0, 0, 0) )
        pygame.display.update()

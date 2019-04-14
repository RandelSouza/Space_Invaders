from setup import *
import pygame, sys, os
from pygame.locals import *

class Credits( object ):
    def __init__( self ):
        self.init = pygame.init()
        self.font =  pygame.font.Font(None, 80)
        self.screen = pygame.display.set_mode( [ LARGURA, ALTURA ] )
        self.text = []
        self.setText()
        pygame.font.init()

    def setText( self ):
        self.text = ["Game Programming - Randel Souza ALmeida",
                     "Game Design - Randel Souza Almeida",
                     "Picture Art - GameArt site (www.gameArt.com)"]

    def drawUpdateText( self ):
        pass
    def eventQuitCredits( self, event ):
        if event.type == QUIT:
            return 3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return 3

    def eventHandlerCredits( self ):
        for event in pygame.event.get():
            return self.eventQuitCredits( event )

    def drawAndUpdateCredits( self ):
        main_game = self.eventHandlerCredits()
        self.screen.fill( ( 0, 0, 0 ) )
        pygame.display.update()
        return main_game

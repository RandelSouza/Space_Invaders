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
        self.collors = { "white": (255, 255, 255), "green": (0, 255, 0) }
        pygame.font.init()

    def renderText( self, nameText, collor ):
        return self.font.render( nameText, True, collor )

    def setText( self ):
        text = [ "Game Programming - Randel Souza ALmeida",
                     "Game Design - Randel Souza Almeida",
                     "Picture Art - GameArt site (www.gameArt.com)" ]
        posX = 320
        posY = ALTURA

        for nameText in text:
            self.text.append( { "text" : nameText, "pos" : ( posX, posY ), "collor" : self.collors[ "white" ] } )
            posY -= 100

    def updateScreenText( self ):
        limit = LARGURA
        while limit > 0:
            for text in self.text:
                posy = text[ "pos" ][1]
                self.screen.blit( self.renderText( text[ "text" ], text[ "collor" ] ), (text[ "pos" ][ 0 ], posy ) )
                posy += 1
                limit += posy

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
        self.updateScreenText()        
        pygame.display.update()
        return main_game

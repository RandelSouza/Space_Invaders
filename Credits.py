from setup import *
import pygame, sys, os
from pygame.locals import *

class Credits( object ):
    def __init__( self ):
        self.init = pygame.init()
        self.font =  pygame.font.Font( None, 40 )
        self.screen = pygame.display.set_mode( [ LARGURA, ALTURA ] )
        self.text = []
        self.collors = { "white" : ( 255, 255, 255 ) }
        self.setText()
        pygame.font.init()
        self.limit = ALTURA

    def renderText( self, nameText, collor ):
        return self.font.render( nameText, True, collor )

    def setText( self ):
        text = [
                 "Game Programming - Randel Souza ALmeida",
                 "Game Design - Randel Souza Almeida",
                 "Site (https://opengameart.org/)",
                 "Picture Art - OpenGameArt: ",
                 "                                   CREDITS" ]

        posX = 20
        posY = ALTURA + 300

        for nameText in text:
            self.text.append( { "text" : nameText, "pos" : ( posX, posY ), "collor" : self.collors[ "white" ] } )
            posY -= 50

    def updateScreenText( self ):
        for text in self.text:
            self.screen.blit( self.renderText( text[ "text" ], text[ "collor" ] ), ( text[ "pos" ][ 0 ], text[ "pos" ][ 1 ] ) )
            text[ "pos" ] = ( text[ "pos" ][ 0 ], text[ "pos" ][ 1 ] - 0.3 )
            if text[ "pos" ][1] <= -50:
                text[ "pos" ] = ( text[ "pos" ][0], ALTURA + 300)

    def resetText( self ):
        self.text = []
        self.setText()

    def eventQuitCredits( self, event ):
        if event.type == QUIT:
            self.resetText()
            return 3

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.resetText()
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

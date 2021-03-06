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

    def renderFont( self, nameFont, collor ):
        return self.font.render(nameFont, True, collor)

    def menuOptionsFonts( self ):
        fonts = ["Play", "Settings", "Credits", "Exit"]
        posX = 320
        posY = 150
        selected = 0
        collor = "green"

        for nameFont in fonts:
            self.options.append( { "font" : ( nameFont, self.collors[ collor ] ),
                                    "pos" : ( posX, posY ), "selected": selected } )
            posY += 100

    # mudar a cor das opcoes
    def changeOption( self, index, selected):
        if index < len(self.options) and  index >= 0:
            print self.options[index]["font"], self.options[index]["selected"]
            self.options[index]["selected"] = selected
            print self.options[index]["font"], self.options[index]["selected"]

    def updateScreenOptionsFonts( self ):
        for font in self.options:
            if font["selected"] == 1:
                self.screen.blit( self.renderFont( font[ "font" ][ 0 ], self.collors["white"] ), font[ "pos" ] )
            else:
                self.screen.blit( self.renderFont( font[ "font" ][ 0 ], font[ "font" ] [ 1 ] ), font[ "pos" ] )

    def executeOptions(self, index):
        nameFont = self.options[index]["font"][0]

        if nameFont == "Play":
            return 1

        if nameFont == "Settings":
            pass

        if nameFont == "Credits":
            return 2

        if nameFont == "Exit":
            exit()

    def drawAndUpdateMenu( self ):
        self.screen.blit( self.background, ( 0, 0 ) )
        self.updateScreenOptionsFonts()
        pygame.display.update()

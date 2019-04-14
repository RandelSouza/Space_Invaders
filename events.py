import pygame, sys, os
from setup import *
from pygame.locals import *

class Events(object):
    def __init__(self):
        self.first = -1
        self.font =  pygame.font.Font('./score_board/scoreboard.ttf', 30)
        self.count = 0
        self.score = self.font.render("score: " + str(self.count), True, (0, 255, 0))

    def shootSound(self, shoot):
        shoot.sound.play()

    def removeBulletShip(self, shoot, X, Y, max):
        if len(BULLETS) < max:
            BULLETS.append(pygame.Rect(X+36, Y, 25, 50))
            self.shootSound(shoot)

    def eventKeyPressK_Space(self, event, shoot, X, Y, max):
        if event.key == pygame.K_SPACE :
            self.removeBulletShip(shoot, X, Y, max)

    def eventKeyDown(self, event, shoot, X, Y, max):
        if event.type == pygame.KEYDOWN :
            self.eventKeyPressK_Space( event, shoot, X, Y, max)

    def eventQuit(self, event):
        if event.type == QUIT:
            return 0

    def eventQuitMenu(self, event):
        if event.type == QUIT:
            exit()

    def insertBulletShip(self, shoot, X, Y, max):
        if len(BULLETS) < max:
            BULLETS.append(pygame.Rect(X+36, Y, 25, 50))
            self.shootSound(shoot)

    def eventButtonMouseLeft(self, event, shoot, X, Y, max):
        if event.button == 1:
            print event
            self.insertBulletShip(shoot, X, Y, max)

    def eventButtonMouseRight(self, event, main_game):
        if event.button == 3:
            main_game = 1
            return main_game

    def eventMouseButtonDown(self, event, shoot, X, Y, max):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.eventButtonMouseLeft(event, shoot, X, Y, max)

    def eventMouseButtonDownMenu(self, event, main_game):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return self.eventButtonMouseRight(event, main_game)

    def eventHandler(self, X, Y, shoot, max, main_game):
        for event in pygame.event.get():
            main_game = self.eventQuit( event )
            self.eventKeyDown( event, shoot, X, Y, max)
            self.eventMouseButtonDown(event, shoot, X, Y, max)
            return main_game

    # mudar index e mudar cor da opcao do menu
    def eventKeyPressK_UP_menu( self , event, menu ):
        if event.key == pygame.K_UP:
            menu.changeOption( self.first, 0 )
            if self.first <= 4:
                self.first -= 1
            if self.first < 0:
                self.first = 4
            menu.changeOption( self.first,  1)

    # mudar index e mudar cor da opcao do menu
    def eventKeyPressK_DOWN_menu( self, event, menu):
        if event.key == pygame.K_DOWN:
            menu.changeOption( self.first, 0 )
            if self.first <= 4:
                self.first += 1
            if self.first > 4:
                self.first = 0
            menu.changeOption( self.first, 1)

    def eventKeyPressK_ENTER( self, event, menu, main_game):
        if event.key == pygame.K_RETURN:
            if self.first >= 0 and self.first <= 3:
                main_game =  menu.executeOptions(self.first)
                print main_game
                return main_game

    def eventKeyDownMenu(self, event, menu, main_game):
        if event.type == pygame.KEYDOWN :
            self.eventKeyPressK_UP_menu( event, menu )
            self.eventKeyPressK_DOWN_menu( event, menu )
            return self.eventKeyPressK_ENTER( event, menu, main_game)

    def eventHandlerMenu( self, main_game, menu ):
        for event in pygame.event.get():
            main_game = self.eventKeyDownMenu( event, menu, main_game)
            self.eventQuitMenu( event )
            main_game = self.eventMouseButtonDownMenu( event, main_game )
            return main_game

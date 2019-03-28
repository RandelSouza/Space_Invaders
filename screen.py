from setup import *
import pygame, sys, os
from pygame.locals import *

class Screen(object):
    def __init__(self):
        self.init = pygame.init()
        self.screen = pygame.display.set_mode([LARGURA, ALTURA])
        self.background =  pygame.image.load("scenarios/back_3.png").convert()
        self.fps = pygame.time.Clock().tick(60)
        pygame.mixer.init()
        pygame.mixer.music.load("music/sound2.ogg")
        pygame.font.init()

    def limites_tela(self, X, Y):
if X <= -10: X = 702
if X >= 704.99: X = 0
if Y <= 422: Y = 422
if Y > 499:   Y = 499
return X, Y

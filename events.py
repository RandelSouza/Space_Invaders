import pygame, sys, os
from setup import *
from pygame.locals import *

class Events(object):
def __init__(self):
self.font =  pygame.font.Font('./score_board/scoreboard.ttf', 30)
self.count = 0
self.score = self.font.render("score: " + str(self.count), True, (0, 255, 0))

def shootSound(self, shoot):
shoot.sound.play()

import pygame, sys, os
from pygame.locals import *
from setup import *

class Shot(object):
def __init__(self):
#self.image = pygame.transform.scale(pygame.image.load("image/shot_red.png").convert_alpha(), (25,25))
#self.image = pygame.transform.scale(pygame.image.load("image/enemy_shoot_purple.png").convert_alpha(), (25,25))
self.image = []
self.speed = 1
self.sound = pygame.mixer.Sound("music/Shoot_00.wav")
self.sound2 = pygame.mixer.Sound("music/Explosion_01.wav")
self.sound2.set_volume(0.1)
self.sound.set_volume(0.1)
self.setImage()

def setImage( self ):
for pathImage in LIST_STRINGS:
self.image.append( pygame.transform.scale( pygame.image.load( pathImage ).convert_alpha(), ( 25, 25 ) ) )


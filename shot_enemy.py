import pygame, sys, os, random
from pygame.locals import *
from setup import *

class ShotEnemy(object):
def __init__(self):
self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("image/shot_red.png").convert_alpha(), (25,25)), 180)
self.image2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("image/shot_yellow.png").convert_alpha(), (25,25)), 180)
self.speed = 1.9
self.sound = pygame.mixer.Sound("music/Shoot_00.wav")
self.sound2 = pygame.mixer.Sound("music/Explosion_01.wav")
self.sound2.set_volume(0.1)

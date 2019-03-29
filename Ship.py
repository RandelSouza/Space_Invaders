import pygame, sys, os
from pygame.locals import *

class Ship(object):
def __init__(self, x, y, width, height, speed, screen):
self.screen = screen
self.images = []
self.speed = speed
self.setWidthAndHeight( width, height )
self.setXandY(x, y)
self.sprit_number = 1
self.get_images_array()
self.setSounds()
self.setHeart()
self.rect = self.get_rect()
pygame.mixer.music.set_volume(0.2)

def setHeart(self):
self.heart = pygame.image.load("image/heart.png")
self.heart_count = 10


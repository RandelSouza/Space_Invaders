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

def setSounds(self):
self.sound = pygame.mixer.Sound("music/wind1.wav")
self.sound2 = pygame.mixer.Sound("music/Explosion_01.wav")

def setWidth(self, width):
self.width = width

def setHeight(self, height):
self.height = height

def setWidthAndHeight(self, width, height):
self.setWidth(width)
self.setHeight(height)

def setX(self, x):
self.x = x

def setY(self, y):
self.y = y

def setXandY(self, x, y):
self.setX(x)
self.setY(y)

def get_rect(self):
return pygame.Rect(self.x, self.y, self.width, self.height)

def draw_centered(self, surface1, surface2, position):
rect = surface1.get_rect()
rect = rect.move( position[0], position[1] )
surface2.blit( surface1, rect )

def update_position(self):
self.draw_centered(self.images[self.sprit_number], self.screen, [self.x, self.y])


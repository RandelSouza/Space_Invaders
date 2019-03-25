import pygame, sys, os, random
from setup import *
from pygame.locals import *
from threading import Thread
import time

class Enemy(object):
def __init__(self, x , y, width, height, speed):
self.x = x
self.y = y
self.width = width
self.height = height
self.speed = speed
self.image =  pygame.transform.scale(pygame.image.load("image/aliensprite1.png").convert_alpha(), (40,40))
self.image2 = pygame.transform.scale(pygame.image.load("image/ufo2.png").convert_alpha(), (50,50))
self.image3 = pygame.transform.scale(pygame.image.load("image/alien.png").convert_alpha(), (50,50))
self.image4 = pygame.transform.scale(pygame.image.load("image/alien2.png").convert_alpha(), (50,50))
self.rect = self.get_rect()

def get_rect(self):
return pygame.Rect(self.x, self.y, self.width, self.height)

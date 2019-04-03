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

def update_heart(self):
for life in range(self.heart_count):
self.draw_centered(self.heart, self.screen, [-10 + 30 * life, -10])

def loadImage(self, pathImage):
return pygame.image.load(pathImage)

def transformScaleImage(self, image):
return pygame.transform.scale(image, (self.width, self.height) )

def appendImageInArray(self, pathImage):
self.images.append( self.transformScaleImage( self.loadImage(pathImage) ) )

def get_images_array(self):
for indexImage in range(1, 4):
self.appendImageInArray( "image/redfighter000%i.png" %( indexImage + 3 ) )

for indexImage in range(1, 4):
self.appendImageInArray( "image/ship%i.png" %( indexImage + 1) )

def moveRight(self):
self.x  += self.speed

def moveLeft(self):
self.x  -= self.speed

def setSpritNumber(self, sprit_number):
self.sprit_number = sprit_number

def setSoundMaxTime(self, maxTimeSound):
self.sound.play(0, maxTimeSound)

def setSpritSound(self, sprit_number, maxTimeSound):
self.setSpritNumber(sprit_number)
self.setSoundMaxTime(maxTimeSound)

def moveUp(self):
self.y  -= self.speed

def moveDown(self):
self.y  += self.speed

def moveRightLeft(self, right, sprit_number, maxTimeSound):
if right:
self.moveRight()
else:
self.moveLeft()
self.setSpritSound(sprit_number, maxTimeSound)

def moveUpDown(self, up, sprit_number, maxTimeSound):
if up:
self.moveUp()
else:
self.moveDown()
self.setSpritSound(sprit_number, maxTimeSound)

def eventMoveRight(self):
if pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]:
self.moveRightLeft(True, 2, 200)

def eventMoveLeft(self):
if pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]:
self.moveRightLeft(False, 0, 200)

def eventMoveUp(self):
if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]:
self.moveUpDown(True, 1, 200)

def eventMoveDown(self):
if pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]:
self.moveUpDown(False, 1, 200)

def movimentacao_nave(self):
self.eventMoveRight()
self.eventMoveLeft()
self.eventMoveUp()
self.eventMoveDown()

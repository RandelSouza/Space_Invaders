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

def create_enemies(self, number):
start_t = time.time()

global count, y2
y2 = 0

for _ in range(number):
if count == 5:
count = 0
y2 += 35

enemyObject = Enemy(LARGURA/2 - 250 + (count * 50), y2, 50, 50, 0.8)
enemies.append(enemyObject)
count += 1

print time.time() - start_t

def enemy_create_shot(self, shot_enemy, X, Y):
if len(BULLETS_ENEMY) < random.randint(1, 2):
BULLETS_ENEMY.append(pygame.Rect(X+16, Y-5, 25, 50))
shot_enemy.sound.play()

def enemy_collide(self, ship):
collide = ship.get_rect().collidelist(BULLETS_ENEMY)

if collide != -1:
BULLETS_ENEMY.remove(BULLETS_ENEMY[collide])
if ship.heart_count >= 1:
#ship.sound2.play()
ship.heart_count -= 1

def update_coordinate_enemy(self, enemy):
enemy.x += enemy.speed

if enemy.x > LARGURA:
enemy.y += 100
enemy.x = 0

if enemy.y >= 400:
enemy.y = 0


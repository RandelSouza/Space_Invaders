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
        self.sound.set_volume(0.1)

def update_bullets(self, screen, ship):
if len(BULLETS_ENEMY) != 0:
for bullet_enemy in BULLETS_ENEMY:
bullet_enemy[1] += self.speed

if bullet_enemy[1] > ALTURA:
BULLETS_ENEMY.remove(bullet_enemy)

# decidir de coloco ou nao
#if random.randint(1, 2) % 2 == 0:
#    bullet_enemy[0] += self.speed
#else:
#    bullet_enemy[0] -= self.speed
#screen.blit(self.image2, bullet_enemy)
screen.blit(self.image, bullet_enemy)

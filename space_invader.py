# -*- coding: utf-8 -*-
import pygame, sys, os
from pygame.locals import *
from shot import *
from setup import *
from screen import *
from events import *
from Enemy import *
from Ship import *
from menu import *
from shot_enemy import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

menu = Menu()
tela = Screen()
ship = Ship(LARGURA/2, ALTURA/2, 100, 100, 1.8, tela.screen)
shot = Shot()
enemy = Enemy(0,0,0,0,0)
events = Events()
shotEnemy = ShotEnemy()
number = 20
spriteEnemy = 1
max_shot = 3
main_game = 0
enemies_quantity = 0

while True:
    main_game = events.eventHandlerMenu(main_game, menu)
menu.drawAndUpdateMenu()

if main_game == 1:
while True:
if main_game == 0:
break

main_game = events.eventHandler(ship.x, ship.y, shot, max_shot, main_game)

tela.screen.blit(tela.background, (0,0))
shot.update_bullets(tela.screen)
shotEnemy.update_bullets(tela.screen, ship)

if enemies_quantity == 0:
enemy.create_enemies(number)
if spriteEnemy == 1:
spriteEnemy = 2
elif spriteEnemy == 2:
spriteEnemy = 3
elif spriteEnemy == 3:
spriteEnemy = 4
else:
spriteEnemy = 1

enemies_quantity = enemy.update_enemies(tela.screen, spriteEnemy, shot, events, ship, shotEnemy)

ship.movimentacao_nave()
ship.x, ship.y = tela.limites_tela(ship.x, ship.y)
ship.update_position()
ship.update_heart()

tela.screen.blit(events.score,  (600, 0))
pygame.display.update()

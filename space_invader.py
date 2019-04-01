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

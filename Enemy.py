import pygame, sys, os, random
from setup import *
from pygame.locals import *
from threading import Thread
import time

class Enemy(object):
def __init__(self, x , y, width, height, speed):

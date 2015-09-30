import pygame, sys
from pygame.locals import *

pygame.init()

class Player:
    def __init__(self):
        self.name = "PLACEHOLDER"
        self.inventory = {}

        self.level = 1
        self.stats = {"str": 1, "def": 5, "atk": 4}

        self.current_hp = 10
        self.equipped = {}

        

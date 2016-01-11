import pygame
from pygame.locals import *

class Event_Handler(object):
    def __init__(self):
        pass

    def quit_game(self, event):
        '''quits the game if 'x' is pressed'''
        if event.type == QUIT:
            return True

    def can_move(self, x, y, grid):
        '''checks if the player can move to a (x, y) position'''
        for j in grid:
            for i in j:
                if i.__class__.__name__ != "Player":
                    if i.xpos == x and i.ypos == y:
                        return i.is_free()

    def player_moves(self, event, plr_x, plr_y, size_x, size_y, grid, xmov, ymov):
        '''handles player moves'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ymov = -size_y
            if event.key == pygame.K_s:
                ymov = size_y
            if event.key == pygame.K_a:
                xmov = -size_x
            if event.key == pygame.K_d:
                xmov = size_x

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                if ymov < 0:
                    ymov = 0
            if event.key == pygame.K_s:
                if ymov > 0:
                    ymov = 0
            if event.key == pygame.K_a:
                if xmov < 0:
                    xmov = 0
            if event.key == pygame.K_d:
                if xmov > 0:
                    xmov = 0
        return xmov, ymov

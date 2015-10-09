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
        self.x = x
        self.y = y
        for j in grid:
            for i in j:
                if i.__class__.__name__ != "Player":
                    if i.xpos == x and i.ypos == y:
                        if i.is_free():
                            return True

    def player_moves(self, event, plr_x, plr_y, size_x, size_y, grid, xmov, ymov):
        '''handles player moves'''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if self.can_move(plr_x, plr_y - size_y, grid):
                    ymov = -size_y
            if event.key == pygame.K_s:
                if self.can_move(plr_x, plr_y + size_y, grid):
                    ymov = size_y
            if event.key == pygame.K_a:
                if self.can_move(plr_x - size_x, plr_y, grid):
                    xmov = -size_x
            if event.key == pygame.K_d:
                if self.can_move(plr_x + size_x, plr_y, grid):
                    xmov = size_x
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                if self.can_move(plr_x, plr_y - size_y, grid):
                    if ymov < 0:
                        ymov = 0
            if event.key == pygame.K_s:
                if self.can_move(plr_x, plr_y + size_y, grid):
                    if ymov > 0:
                        ymov = 0
            if event.key == pygame.K_a:
                if self.can_move(plr_x - size_x, plr_y, grid):
                    if xmov < 0:
                        xmov = 0
            if event.key == pygame.K_d:
                if self.can_move(plr_x + size_x, plr_y, grid):
                    if xmov > 0:
                        xmov = 0

        return xmov, ymov

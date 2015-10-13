import pygame
from pygame.locals import *

class Text(object):
    def __init__(self):
        self.small_font = pygame.font.Font(r"res/rudelsberg/Rudelsberg.ttf", 25)
        self.big_font = pygame.font.Font(r"res/rudelsberg/Rudelsberg.ttf", 75)

    def text_object(self, text, color, kinda_font):
        '''returns the surface of a given text and font rendered'''
        self.text_surf = kinda_font.render(text, False, color)
        return self.text_surf, self.text_surf.get_rect()

    def text_by_top_left(self, msg, coords, color, kinda_font):
        '''locates the text by receiving its top left corner coordinates (default)'''
        self.text_surf, self.text_rect = self.text_object(msg, color, kinda_font)
        return self.text_surf, self.text_rect

    def text_by_center(self, msg, coords, color, kinda_font):
        '''locates the text by receiving its center coordinates, returns surface and rect'''
        self.text_surf, self.text_rect = self.text_object(msg, color, kinda_font)
        self.text_rect.center = coords
        return self.text_surf, self.text_rect

    def text_by_top_right(self, msg, coords, color, kinda_font):
        '''locates the text by receiving its top right corner coordinates'''
        self.text_surface, self.text_rect = self.text_object(msg, color, kinda_font)
        self.text_rect_width = self.text_surface.get_width()
        self.text_rect_height = self.text_surface.get_height()
        self.text_rect.center = int(coords[0] - self.text_rect_width/2), int(coords[1] + self.text_rect_height/2)
        return self.text_surf, self.text_rect

    def text_by_bot_left(self, msg, coords, color, kinda_font):
        '''locates the text by receiving its top right corner coordinates'''
        self.text_surface, self.text_rect = self.text_object(msg, color, kinda_font)
        self.text_rect_width = self.text_surface.get_width()
        self.text_rect_height = self.text_surface.get_height()
        self.text_rect.center = int(coords[0] + self.text_rect_width/2), int(coords[1] - self.text_rect_height/2)
        return self.text_surf, self.text_rect

    def text_by_bot_right(self, msg, coords, color, kinda_font):
        '''locates the text by receiving its top right corner coordinates'''
        self.text_surface, self.text_rect = self.text_object(msg, color, kinda_font)
        self.text_rect_width = self.text_surface.get_width()
        self.text_rect_height = self.text_surface.get_height()
        self.text_rect.center = int(coords[0] - self.text_rect_width/2), int(coords[1] - self.text_rect_height/2)
        return self.text_surf, self.text_rect

class Life_bar(object):
    def __init__(self, life, scr_width, scr_height):

        self.width = scr_width
        self.height = scr_height
        if life <= 0:
            self.life = 0
        else:
            self.life = life
        self.percent = (100 * self.life) / 10
        self.totallength = (self.width / 10) * 8
        self.length = self.totallength * (self.percent/100)

    def get_color(self):
        '''calculates the color based on life percentage'''
        if self.percent >= 50:
            self.red = -(self.percent * 5.1) + 510
            self.green = 255
            return (self.red, self.green, 0)
        elif self.percent <50:
            self.red = 255
            self.green = self.percent * 5.1
            return (self.red, self.green, 0)


    def get_rect(self):
        '''defines the rect that is going to be drawn'''
        self.coords = (self.width/10, self.height/10)
        self.color = self.get_color()

        return("SURFACE", self.color, (self.coords[0], self.coords[1], self.length, 20), 2)

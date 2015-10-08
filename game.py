import pygame
from pygame.locals import *
from grid import Grid
from fields import Player

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
OFF_RED = (230, 20, 20)


player = Player(1, 1, 1, 1, 1)

'''
###----TEXT_CLASS----###################################################################################################
class Text(Game):
    def __init__(self):
        pygame.init()
        self.small_font = pygame.font.SysFont("Arial", 25)
        self.big_font = pygame.font.SysFont("Arial", 75)

    def text_objects(self, text, color, font_type):

        text_surface = font_type.render(text, True, color)
        return text_surface, text_surface.get_rect()

    def message_to_screen(self, msg, coords, color, font_type):

        text_surface, text_rect = Text.text_objects(self, msg, color, font_type)
        #print(text_rect)
        text_rect.center = coords
        gameDisplay.blit(text_surface, text_rect)

    def message_to_screen_left_corner(self, msg, coords, color, font_type):

        screen_text = font_type.render(msg, True, color)
        gameDisplay.blit(screen_text, coords)

    def message_to_screen_right_corner(self, msg, coords, color, font_type):

        text_surface, text_rect = Text.text_objects(self, msg, color, font_type)
        text_rect_width = text_surface.get_width()
        text_rect_height = text_surface.get_height()
        text_rect.center = int(coords[0] - text_rect_width/2), int(coords[1] + text_rect_height/2)
        gameDisplay.blit(text_surface, text_rect)

    def display_stats(self, stats_dict):

        self.stats = stats_dict
        self.display.blit(self.small_font.render('strength:' + str(stats['strength']), True, (255,0,0)), (10, 10))

text_class = Text()

'''




class Game(object):
    """Where the game runs"""
    def __init__(self, height, width):
        pygame.init()
        self.height, self.width = height, width
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.convert()
        self.background.fill(BLACK)
        self.clock = pygame.time.Clock()


        self.small_font = pygame.font.SysFont("Arial", 25)
        self.big_font = pygame.font.SysFont("Arial", 75)
        pygame.display.set_caption('PyRogue')

        pygame.display.update()


    def get_stats(self):
        char_stats = player.stats()
        return char_stats

    def display_stats(self, stats_dict):
        self.stats = stats_dict
        self.screen.blit(self.small_font.render('strength:' + str(stats_dict['strength']), True, (OFF_RED)), (10, 10))

    def adjust_screen(self, bottom_right_field):
        """adjusts the screen if fields don't take up all display"""
        width = bottom_right_field.xpos + bottom_right_field.sizex
        height = bottom_right_field.ypos + bottom_right_field.sizey
        self.screen = pygame.display.set_mode((width, height))

    def main(self):
        # Blit everything to the screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        grid = Grid("level1.txt")
        fields_grid = grid.generate_grid(self.height, self.width)
        self.adjust_screen(fields_grid[-1][-1])
        for x in fields_grid:
            for f in x:
                pygame.draw.rect(self.screen, f.color, (f.xpos,f.ypos, f.sizex, f.sizey), 0)

        # Event loop
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            stats = self.get_stats()
            pygame.draw.rect(self.screen, (BLACK), (5, 10, 200, 100), 2)
            self.display_stats(stats)
            pygame.display.flip()
            self.clock.tick(30)
if __name__ == '__main__':
    Game(540, 960).main()

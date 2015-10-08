import pygame
from pygame.locals import *
from grid import Grid
from fields import Player

BLACK = (0,0,0)
WHITE = (255,255,255)


player = Player(1, 1, 1, 1, 1)

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

        self.font = pygame.font.SysFont('Arial', 25)
        pygame.display.set_caption('PyRogue')

        pygame.display.update()


    def display_stats(self):
        char_stats = player.stats()
        return char_stats


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
            stats = self.display_stats()
            pygame.draw.rect(self.screen, (BLACK), (5, 10, 200, 100), 2)
            self.screen.blit(self.font.render('strength:' + str(stats['strength']), True, (255,0,0)), (10, 10))
            pygame.display.flip()
            self.clock.tick(30)
if __name__ == '__main__':
    Game(540, 960).main()

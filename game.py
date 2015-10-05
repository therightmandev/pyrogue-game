import pygame
from pygame.locals import *
from grid import Grid

BLACK = (0,0,0)
WHITE = (255,255,255)


class Display(object):
    """handles pygame main loop, display etc."""
    def __init__(self, height, width):
        pygame.init()
        self.height, self.width = height, width
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.convert()
        self.background.fill(BLACK)
        self.clock = pygame.time.Clock()

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

            pygame.display.flip()
            self.clock.tick(30)

if __name__ == '__main__':
    Display(540, 960).main()

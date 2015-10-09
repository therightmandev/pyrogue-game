import pygame
from pygame.locals import *
from grid import Grid
from player import Player
from events import Event_Handler


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
OFF_RED = (230, 20, 20)


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
        self.gameExit = False


        self.small_font = pygame.font.SysFont("Arial", 25)
        self.big_font = pygame.font.SysFont("Arial", 75)
        pygame.display.set_caption('PyRogue')

        pygame.display.update()


    def get_stats(self, player):
        '''get player stats'''
        char_stats = player.stats()
        return char_stats

    def display_stats(self, stats_dict):
        '''render stats to the screen'''
        self.stats = stats_dict
        pygame.draw.rect(self.screen, (BLACK), (7, 10, 150, 120), 3)
        self.screen.blit(self.small_font.render('level: ' + str(stats_dict['level']), True, (OFF_RED)), (10, 10))
        self.screen.blit(self.small_font.render('HP: ' + str(stats_dict['current_hp']), True, (OFF_RED)), (10, 30))
        self.screen.blit(self.small_font.render('strength: ' + str(stats_dict['strength']), True, (OFF_RED)), (10, 50))
        self.screen.blit(self.small_font.render('attack : ' + str(stats_dict['attack']), True, (OFF_RED)), (10, 70))
        self.screen.blit(self.small_font.render('defence: ' + str(stats_dict['defence']), True, (OFF_RED)), (10,  90))


    def adjust_screen(self, bottom_right_field):
        '''adjusts the screen if fields don't take up all display'''
        width = bottom_right_field.xpos + bottom_right_field.sizex
        height = bottom_right_field.ypos + bottom_right_field.sizey
        self.screen = pygame.display.set_mode((width, height))

    def draw_grid(self, grid):
        '''draws the grid and returns the player object'''
        for x in grid:
            for f in x:
                if f.__class__.__name__ == "Wall" or f.__class__.__name__ == "Floor":
                    pygame.draw.rect(self.screen, f.color, (f.xpos,f.ypos, f.sizex, f.sizey), 0)
                if f.__class__.__name__ == "Player":
                    player = f
                    player_index = x.index(f)
                    player_row = grid.index(x)
        pygame.draw.rect(self.screen, player.color, (player.xpos, player.ypos, player.sizex, player.sizey), 0)
        return player, player_row, player_index


    def main(self):
        # Blit everything to the screen
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        grid = Grid("level1.txt")
        fields_grid = grid.generate_grid(self.height, self.width)
        self.adjust_screen(fields_grid[-1][-1])



        # Event loop
        while not self.gameExit:
            player, player_row, player_index = self.draw_grid(fields_grid)

            for event in pygame.event.get():
                events = Event_Handler()
                self.gameExit = events.quit_game(event)
                player.xpos, player.ypos = events.player_moves(event, player.xpos, player.ypos, player.sizex, player.sizey, fields_grid)
                fields_grid[player_row][player_index] = player

            stats = self.get_stats(player)
            self.display_stats(stats)
            pygame.display.flip()
            self.clock.tick(30)
if __name__ == '__main__':
    Game(540, 960).main()

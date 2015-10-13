import pygame
from pygame.locals import *
from grid import Grid
from player import Player
from events import Event_Handler
from screen_addons import Text, Life_bar


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
OFF_RED = (230, 20, 20)
DARK_GREY = (30, 30, 30)
A_BLUE = (5, 100, 240)



class Game(object):
    """Where the game runs"""
    def __init__(self, height, width):
        pygame.init()
        self.height, self.width = height, width
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.convert()
        self.background.fill(DARK_GREY)
        self.clock = pygame.time.Clock()
        self.gameExit = False

        self.text = Text()


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
        self.screen.blit(self.text.small_font.render('Level: ' + str(stats_dict['level']), False, (A_BLUE)), (10, 10))
        self.screen.blit(self.text.small_font.render('HP: ' + str(stats_dict['current_hp']), False, (A_BLUE)), (10, 30))
        self.screen.blit(self.text.small_font.render('Strength: ' + str(stats_dict['strength']), False, (A_BLUE)), (10, 50))
        self.screen.blit(self.text.small_font.render('Attack : ' + str(stats_dict['attack']), False, (A_BLUE)), (10, 70))
        self.screen.blit(self.text.small_font.render('Defence: ' + str(stats_dict['defense']), False, (A_BLUE)), (10,  90))

        self.render_list = []
        self.render_list.append(self.text.text_by_bot_left(str(stats_dict['level']), (self.width/10, self.height/10*9), A_BLUE, self.text.big_font))
        for f in self.render_list:
            self.screen.blit(f[0], f[1])

    def disp(self, life):
        self.life_bar = Life_bar(life, self.width, self.height)
        self.bar = self.life_bar.get_rect()
        pygame.draw.rect(self.screen, self.bar[1], (self.bar[2]), self.bar[3])


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
        #self.adjust_screen(fields_grid[-1][-1])



        # Event loop
        while not self.gameExit:
            self.screen.blit(self.background, (0, 0))
            player, player_row, player_index = self.draw_grid(fields_grid)

            for event in pygame.event.get():
                events = Event_Handler()
                self.gameExit = events.quit_game(event)
                player.xmov, player.ymov = events.player_moves(event, player.xpos, player.ypos, player.sizex, player.sizey, fields_grid, player.xmov, player.ymov)
                fields_grid[player_row][player_index] = player
            if events.can_move(player.xpos + player.xmov, player.ypos, fields_grid):
                player.xpos += player.xmov
                if player.xmov > 0:
                    player.current_hp = player.current_hp - 0.2
            if events.can_move(player.xpos, player.ypos + player.ymov, fields_grid):
                player.ypos += player.ymov

            stats = self.get_stats(player)
            self.display_stats(stats)
            self.disp(player.current_hp)
            pygame.display.flip()
            self.clock.tick(20)

if __name__ == '__main__':
    Game(640, 1060).main()

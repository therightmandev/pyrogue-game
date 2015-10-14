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
RED_ORANGE = (245, 34, 5)
D_BLUE = (0, 179, 255)




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

        self.render_list = []
        self.tile = pygame.Surface(self.screen.get_size())
        self.level_text = self.text.text_by_bot_left("Lvl " + str(stats_dict['level']), (self.width/10, self.height/20*19), A_BLUE, self.text.big_font)
        self.strength_text = self.text.text_by_bot_left("Strenght " + str(stats_dict['strength']), (self.level_text[1].x + self.level_text[1].width, self.height/20*19), A_BLUE, self.text.big_font)
        self.defense_text = self.text.text_by_top_left("Defense " + str(stats_dict['defense']), (self.width/10, self.height/20*3), D_BLUE, self.text.small_font)
        self.attack_text = self.text.text_by_top_left("Attack " + str(stats_dict['attack']), (self.width/10 + 1.2 * self.defense_text[1].width, self.height/20*3), RED_ORANGE, self.text.small_font)
        self.render_list.append(self.level_text)
        self.render_list.append(self.defense_text)
        self.render_list.append(self.attack_text)
        self.render_list.append(self.strength_text)
        for f in self.render_list:
            self.screen.blit(f[0], f[1])

    def display_hp(self, life):
        self.life_bar = Life_bar(life, self.width, self.height)
        self.bar = self.life_bar.get_bar()
        pygame.draw.rect(self.screen, self.bar[1], (self.bar[2]), self.bar[3])
        self.bar_x_center = self.bar[2][0] + self.bar[2][2]/2
        self.bar_y_center = self.bar[2][1] + self.bar[2][3]/2
        self.string = self.text.text_by_center(str(life), (self.bar_x_center, self.bar_y_center), self.bar[1], self.life_bar.life_font)
        self.screen.blit(self.string[0], self.string[1])


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
                if player.xmov > 0: #for testing purposes
                    player.current_hp = round(player.current_hp - 0.2, 1)
                if player.current_hp <= 0: #for testing purposes
                    player.current_hp = 0
            if events.can_move(player.xpos, player.ypos + player.ymov, fields_grid):
                player.ypos += player.ymov

            stats = self.get_stats(player)
            self.display_stats(stats)
            self.display_hp(player.current_hp)
            pygame.display.flip()
            self.clock.tick(20)

if __name__ == '__main__':
    Game(640, 1060).main()

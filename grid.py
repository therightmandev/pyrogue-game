from fields import *
from player import Player


class Grid(object):
    def __init__(self, level_file):
        """level_list is a list of rows of level"""
        self.level_list = self.open_level(level_file)

    def open_level(self, level_file):
        filepath = "res/"+level_file
        try:
            level = open(filepath)
        except:
            print "Cannot open " + filepath
        else:
            print "Level "+filepath+" loaded" \
                                    ""
        level_list = level.readlines()
        return level_list

    def get_longest_row(self):
        # needed for calculating size of Fields
        longest = 0
        for row in self.level_list:
            if len(row) > longest:
                longest = len(row)
        return longest

    def get_middle(self):
        self.longest_row = self.get_longest_row()
        self.middlex = self.longest_row / 2
        self.middley = len(self.level_list) / 2
        return self.middlex, self.middley

    def generate_grid(self, screen_height, screen_width):
        """returns a list of ready to draw Fields"""
        # calculating field size
        row_count = self.get_longest_row()
        field_xsize = 10
        field_ysize = 10
        if screen_height == screen_width: # if screen is square
            field_xsize = screen_height / row_count
            field_ysize = screen_height / row_count
        field_xsize = screen_width / row_count - 1 # field width is fitted to screen
        field_ysize = screen_width / row_count - 1 # field height is fitted to screen

        # coordinates of fields on screen
        middle_x, middle_y = self.get_middle()
        print middle_x, middle_y
        x_pos = screen_width/2 - middle_x * field_xsize #level is centered on x
        y_pos = (screen_height/4 + (screen_height/8 * 7))/2 - middle_y * field_ysize

        all_fields = []
        for row in self.level_list:
            fields_row = []
            for char in row:
                if char == '#':
                    new_field = Wall(x_pos, y_pos, field_xsize, field_ysize)
                    fields_row.append(new_field)
                if char == '.':
                    new_field = Floor(x_pos, y_pos, field_xsize, field_ysize)
                    fields_row.append(new_field)
                if char == '@':
                    player = Player(x_pos, y_pos, field_xsize * 20 / 60, "Caveman", 0, 0)
                    new_field1 = Floor(x_pos, y_pos, field_xsize, field_ysize)
                    print "appended player"
                    fields_row.append(new_field1)
                    fields_row.append(player)
                x_pos += field_xsize
            all_fields.append(fields_row)
            x_pos = screen_width/2 - middle_x * field_xsize
            y_pos += field_ysize
        return all_fields

    def print_fields(self, fields_grid):

        for x in fields_grid:
            for y in x:
                print y.sizex
                print y.sizey

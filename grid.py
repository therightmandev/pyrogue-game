from fields import *


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

    def generate_grid(self, screen_height, screen_width):
        """returns a list of ready to draw Fields"""
        # calculating field size
        row_count = self.get_longest_row()
        field_xsize = 0
        field_ysize = 0
        if screen_height == screen_width: # if screen is square
            field_xsize = screen_height / row_count
            field_ysize = screen_height / row_count
        field_xsize = screen_width / row_count # field width is fitted to screen
        field_ysize = screen_height / len(self.level_list) # field height is fitted to screen

        # coordinates of fields on screen
        x_pos = 0
        y_pos = 0

        all_fields = []
        for row in self.level_list:
            fields_row = []
            for char in row:
                if char == '#':
                    new_field = Wall(x_pos, y_pos, field_xsize, field_ysize)
                if char == '.':
                    new_field = Floor(x_pos, y_pos, field_xsize, field_ysize)
                fields_row.append(new_field)
                x_pos += field_xsize
            all_fields.append(fields_row)
            x_pos = 0
            y_pos += field_ysize
        return all_fields

    def print_fields(self, fields_grid):

        for x in fields_grid:
            for y in x:
                print y.sizex
                print y.sizey

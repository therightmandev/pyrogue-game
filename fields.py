RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GRAY = (160,160,160)
BROWN = (153,76,0)


class Field(object):
    """Field or 'square' on the grid"""
    def __init__(self, xpos, ypos, sizex, sizey):
        self.xpos = xpos
        self.ypos = ypos
        self.sizex = sizex
        self.sizey = sizey

    def is_free(self):
        return self.__class__.__name__ == 'Free'

    def details(self):
        print "Type: " + self.__class__.__name__

class Player(Field):
    """player class, inheriting from Field as it's still a field"""
    def __init__(self, xpos, ypos, sizex, sizey, name):
        Field.__init(self, xpos, ypos, sizex, sizey)
        self.color = GREEN
        self.name = name


class Wall(Field):
    def __init__(self, xpos, ypos, sizex, sizey):
        Field.__init__(self, xpos, ypos, sizex, sizey)
        self.color = BROWN


class Floor(Field):
    def __init__(self, xpos, ypos, sizex, sizey):
        Field.__init__(self, xpos, ypos, sizex, sizey)
        self.color = GRAY

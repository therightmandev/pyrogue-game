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
        print "free checking"
        if self.__class__.__name__ == "Wall":
            print "wall"
            return False
        elif self.__class__.__name__ == "Floor":
            return True

    def details(self):
        print "Type: " + self.__class__.__name__


class Wall(Field):
    def __init__(self, xpos, ypos, sizex, sizey):
        Field.__init__(self, xpos, ypos, sizex, sizey)
        self.color = BROWN
        self.free = False


class Floor(Field):
    def __init__(self, xpos, ypos, sizex, sizey):
        Field.__init__(self, xpos, ypos, sizex, sizey)
        self.color = GRAY
        self.free = True

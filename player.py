GREEN = (0,255,0)

class Player(object):
    """player class, inheriting from Field as it's still a field"""
    def __init__(self, xpos, ypos, sizex, sizey, name, xmov, ymov):
        self.xpos = xpos
        self.ypos = ypos
        self.xmov = xmov
        self.ymov = ymov
        self.sizex = sizex
        self.sizey = sizey
        self.color = GREEN
        self.name = name
        self.strength = 1
        self.attack = 5
        self.defense = 4
        self.level = 1
        self.current_hp = 10
    def stats(self):
        stats = {'strength': self.strength,
                     'attack': self.attack,
                     'defence': self.defense,
                     'level': self.level,
                     'current_hp': self.current_hp}
        return stats

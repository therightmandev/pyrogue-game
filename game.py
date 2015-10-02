import pygame, sys
from pygame.locals import *
from core.player import Player
from core.walls import Wall
from core.free import Free

###Some colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

###Pygame init and fonts
pygame.init()
fpsClock = pygame.time.Clock()

font_size = 16
font = pygame.font.SysFont('monospace', font_size)

###File opening and reading
level1 = open('level1.txt')
level1List = level1.readlines()
for i, j in enumerate(level1List): #This strips the lines's newline characters
	level1List[i] = j.strip("\n")
level1Locations = []
label_i = font.render(level1List[0], 1, green)

###Display settings
label_rect = pygame.Surface.get_rect(label_i)
display_width = label_rect[2]
display_height = len(level1List)*font_size
display = pygame.display.set_mode((display_width, display_height))

###levelLocations list appending
for i in range(0, len(level1List)):
	level1Locations.append([])
	for j in range(0,len(level1List[i])):

		letter = j

		if (level1List[i][j] == "@"):
			player = Player((i,j))
			level1Locations[i].append(player)
		if (level1List[i][j] == "."):
			free = Free((i,j))
			level1Locations[i].append(free)
		if (level1List[i][j] == "#"):
			wall = Wall((i,j))
			level1Locations[i].append(Wall)


###Main loop
while True:

    display.fill(black)

    for i, j in enumerate(level1List):

		label_i = font.render(j, 1, green)
		display.blit(label_i, (0,(i * font_size)))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    fpsClock.tick(30)

print len(level1Locations)
print level1Locations

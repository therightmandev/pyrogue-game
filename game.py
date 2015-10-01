import pygame, sys
from pygame.locals import *
from core.player import Player
from core.walls import Wall
from core.free import Free

pygame.init()
fpsClock = pygame.time.Clock()

display = pygame.display.set_mode((1280, 720))

font_size = 16
font = pygame.font.SysFont('monospace', font_size)

level1 = open('level1.txt')
level1List = level1.readlines()
level1Locations = []


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


while True:

    display.fill((255,255,255))

    for i, j in enumerate(level1List):
        label_i = font.render(j, 1, pygame.Color(0,0,0))
        display.blit(label_i, (0,(i * font_size)))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    fpsClock.tick(30)

print len(level1Locations)
print level1Locations

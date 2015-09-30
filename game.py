import pygame, sys
from pygame.locals import *
from core.player import Player
from core.walls import Wall
from core.free import Free

pygame.init()
fpsClock = pygame.time.Clock()

display = pygame.display.set_mode((1280, 720))

font = pygame.font.SysFont('monospace', 16)

level1 = open('level1.txt')
level1List = level1.readlines()
level1Locations = []

for i in range(0, len(level1List)):
	level1Locations.append([])
	for j in range(0,len(level1List[i])):
		
		letter = j
		print letter
		if (level1List[i][j] == "@"):
			player = Player((i,j))
			level1Locations[i].append(player)
		if (level1List[i][j] == "."):
			free = Free((i,j))
			level1Locations.append[i](free)
		if (level1List[i][j] == "#"):
			wall = Wall((i,j))
			level1Locations.append[i](Wall

print level1Locations
print level1List

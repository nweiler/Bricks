import random, pygame, sys, os
from pygame.locals import *

FPS = 120
WINDOWWIDTH = 1200
WINDOWHEIGHT = 860
CELLSIZE = 5
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a mutliple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
fpsClock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED =   (255,0,0)
BLUE =  (0,0,255)


WINDOW = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Lines')
WHITE = (255, 255, 255)
BLACK = (0,0,0)
WINDOW.fill(WHITE)

pygame.init()
lines = []


def main():
	WINDOW.fill(GREEN)
	pygame.event.get()
	
	pos = pygame.mouse.get_pos()
	
	for index, x in enumerate(lines):
		pygame.draw.line(lines[index][0], lines[index][1], (lines[index][2][0], lines[index][2][1]), (lines[index][3][0], lines[index][3][1]), 5)

	
	if pygame.mouse.get_pressed()[0] == True:
		lines.append((WINDOW, BLACK, (0, 0), (pos[0], pos[1]), 5))
	
	line1 = pygame.draw.line(WINDOW, BLUE, (0, 0), (pos[0], pos[1]), 5)
	
	pygame.display.update()
	fpsClock.tick(FPS)

while True:
	main()
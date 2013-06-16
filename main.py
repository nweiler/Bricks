import random, pygame, sys, os
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 1200
WINDOWHEIGHT = 860
CELLSIZE = 20
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
BROWN = (139,69,19)


WINDOW = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Bricks')
WHITE = (255, 255, 255)
BLACK = (0,0,0)
WINDOW.fill(BROWN)

pygame.init()
bricks = []
for x in range(0, 1200, 20):
	for y in range(0, 140, 20):
		bricks.append((WINDOW, BLACK, (x, y, x + 20, y + 20)))

bugs = []
bugs.append((WINDOW, RED, (0, 240, 20, 20)))


def main():
	WINDOW.fill(BROWN)
	pygame.event.get()
	
	pos = pygame.mouse.get_pos()


	for index, x in enumerate(bricks):
		pygame.draw.rect(bricks[index][0], bricks[index][1], (bricks[index][2][0], bricks[index][2][1], bricks[index][2][2], bricks[index][2][3]))

	bugs_temp = bugs.pop()
	bugs.append((bugs_temp[0], bugs_temp[1], bugs_temp[2][0] + 20, bugs_temp[2][1], bugs_temp[2][2], bugs_temp[2][3]))
	
	for index, x in enumerate(bugs):
		pygame.draw.rect(bugs[index][0], bugs[index][1], (bugs[index][2][0], bugs[index][2][1], bugs[index][2][2], bugs[index][2][3]))
	
	
	if pygame.mouse.get_pressed()[0] == True:
		bricks.append((WINDOW, BLACK, (pos[0] - pos[0] % 20, pos[1] - pos[1] % 20, 20, 20)))
	
	if pygame.mouse.get_pressed()[2] == True:
		bricks.append((WINDOW, BROWN, (pos[0] - pos[0] % 20, pos[1] - pos[1] % 20, 20, 20)))
	
	rect1 = pygame.draw.rect(WINDOW, GREEN, (pos[0] - pos[0] % 20, pos[1]- pos[1] % 20, 20, 20))
	
	
	
	pygame.display.update()
	fpsClock.tick(FPS)

while True:
	main()
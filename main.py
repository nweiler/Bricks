import random, pygame, sys, os
from pygame.locals import *

FPS = 60
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


WINDOW = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Bricks')
WHITE = (255, 255, 255)
BLACK = (0,0,0)
WINDOW.fill(WHITE)

pygame.init()
bricks = []
bricks.append((WINDOW, BLACK, (0, 0, 30, 20)))
bricks.append((WINDOW, BLACK, (90, 100, 30, 20)))

bugs = []


def main():
	WINDOW.fill(GREEN)
	pygame.event.get()
	
	pos = pygame.mouse.get_pos()


	circ1 = pygame.draw.circle(WINDOW, RED, (100, 100), 100)
	
	rect1 = pygame.draw.rect(WINDOW, BLACK, (pos[0] - pos[0] % 30, pos[1]- pos[1] % 20, 30, 20))


	for index, x in enumerate(bricks):
		pygame.draw.rect(bricks[index][0], bricks[index][1], (bricks[index][2][0], bricks[index][2][1], bricks[index][2][2], bricks[index][2][3]))

	
		
	if pygame.mouse.get_pressed()[0] == True:
		bricks.append((WINDOW, BLACK, (pos[0] - pos[0] % 30, pos[1] - pos[1] % 20, 30, 20)))
	
	
	pygame.display.update()
	fpsClock.tick(FPS)

while True:
	main()
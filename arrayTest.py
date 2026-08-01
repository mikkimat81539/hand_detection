# GOAL: convert array into surface

import pygame
import numpy as np

from numpy import *

# 3D Array
myArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

arraySurface = pygame.surfarray.make_surface(myArray) # convert into a surface


# SCREEN
screen = pygame.display.set_mode((500, 500))

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill("white")

	arraySurface.fill("green")
	screen.blit(arraySurface, (0, 0))

	pygame.display.update()

pygame.quit()

import pygame
import numpy as np
from numpy import *
from cameraObject import *
from playerObject import *

pygame.init()

# SCREEN
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Telekinesis")


# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	screen.fill("black")

	# CAMERA OBJECT
	Camera_Detection.Camera(screen)


	pygame.display.update()

pygame.quit()

import pygame
import numpy as np
from numpy import *
from cameraObject import *
from playerObject import *

pygame.init()

# TIME
clock = pygame.time.Clock()

# SCREEN
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Telekinesis")


# IMAGES
trash_bin = pygame.transform.scale(pygame.image.load("assets/trash_bin.png"), (256, 256)) # trash_bin image

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

#		if event.type == pygame.MOUSEBUTTONDOWN:
#			print(event.pos)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	screen.fill("black")

	# CAMERA OBJECT
	Camera_Detection.Camera(screen)

	# DRAW
	screen.blit(trash_bin, (550, 350))
	

	pygame.display.update()

	clock.tick(60)

pygame.quit()

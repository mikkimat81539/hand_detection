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
brain = pygame.transform.scale(pygame.image.load("assets/brain.png"), (128, 128))

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

	# DRAW
	screen.blit(brain, (350, screen.get_height()//2))

	pygame.display.update()

	clock.tick(60)

pygame.quit()

import pygame
import numpy as np
from numpy import *
from cameraObject import *
from playerObject import *
import cv2 as cv

pygame.init()

# TIME
clock = pygame.time.Clock()

# SCREEN
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("You Are Your Own Worst Enemy")

# IMAGES
heart = pygame.transform.scale(pygame.image.load("assets/heart.png"), (256, 256))

heart_rect = heart.get_rect(topleft=(550, 350))

PLAYER = Camera_Detection().player

# PLAYER HEART COLLISION
def player_heart(player, heart_rect):
	if player.rect.colliderect(heart_rect):
		print("HEART ATTACK")


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

	# COLLISION
	player_heart(PLAYER, heart_rect)

	# DRAW
	screen.blit(heart, (heart_rect))
		
	pygame.display.update()

	clock.tick(60)

pygame.quit()

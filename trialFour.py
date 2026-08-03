import pygame
import numpy as np
from numpy import *
from cameraObject import *
from playerObject import *
from addOns import *
import cv2 as cv
import time

pygame.init()

# TIME
clock = pygame.time.Clock()

# SCREEN
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("You Are Your Own Worst Enemy")

# CAMERA ACTIVATION
camera_activate = True

# FONT
deathText = setupFont(400, 20, "CIGERETTES KILL")

# IMAGES
heart = pygame.transform.scale(pygame.image.load("assets/heart.png"), (256, 256))

heart_rect = heart.get_rect(topleft=(550, 350))

# PLAYER
PLAYER = Camera_Detection().player

# AUDIO
normal_heart = pygame.mixer.music.load("audio/norm_heart_beat.mp3")
# fast_heart = pygame.mixer.music.load("audio/fast_heart_beat.mp3")

pygame.mixer.music.play(1000)

# PLAYER HEART COLLISION
def player_heart(player, heart_rect, surface):
	global camera_activate

	if player.rect.colliderect(heart_rect):
		# PLAY AUDIO
		deathText.displayFont(surface)

		pygame.mixer.music.stop()	

		flatline = pygame.mixer.music.load("audio/flatline.mp3")
		pygame.mixer.music.play(1)

		# pygame.time.delay(5000)
	
		camera_activate = False



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
	if camera_activate:
		Camera_Detection.Camera(screen)

	else:
		pygame.time.delay(500)
		Camera_Detection().cap.release()
		cv.destroyAllWindows()	
		running = False


	# COLLISION
	player_heart(PLAYER, heart_rect, screen)


	# DRAW
	screen.blit(heart, (heart_rect))
		
	pygame.display.update()

	clock.tick(60)

pygame.quit()

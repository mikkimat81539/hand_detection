import cv2 as cv
import pygame
import numpy as np

# initialize pygame
pygame.init()


# Window Title
caption = "Telekinesis"

# Screen
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((800, 600), flags)
pygame.display.set_caption(caption)

# DISPLAY CAMERA
cap = cv.VideoCapture(0)

# if camera is not detected exit
if not cap.isOpened():
	print("Cannot open camera")
	exit()


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

	# DRAW
	ret, frame = cap.read()

	# print(frame)

	frame = np.fliplr(frame) # flip camera
	frame = np.rot90(frame)	 # rotate camera

	frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) # apply color to camera

	frame = cv.resize(frame, (210, 320)) # resize camera display

	camArray = pygame.surfarray.make_surface(frame) # convert array into pygame surfaec

	# print(camArray.get_width(), camArray.get_height())

	screen.blit(camArray, (0, 0)) # blit camera onto screen

	if not ret:
		print("Can't receive frame")
		running = False

	pygame.display.update()

pygame.quit()

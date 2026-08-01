import pygame
from objects import Object
import pygame.camera
import cv2 as cv

pygame.init()
pygame.camera.init()


# CLOCK
clock = pygame.time.Clock()

# SCREEN

flags = pygame.FULLSCREEN

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Telekinesis")

# OBJECTS
block1 = Object(10, 10, 30, 30, "red")

# CAMERA
#cam = pygame.camera.Camera("FaceTime HD Camera", (640, 480))
#cam.start()

cap = cv.VideoCapture(0)
if not cap.isOpened():
	print("Cannot Open Camera")
	exit()

# MAIN LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	screen.fill("white")
	# LOAD CAMERA
	ret, frame = cap.read()

	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		break
	
		# Our operations on the frame come here
		gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	
		# Display the resulting frame
		cv.imshow('frame', gray)
	
	# DRAW
	block1.draw_object(screen)

	pygame.display.update()

	clock.tick(60)

pygame.quit()

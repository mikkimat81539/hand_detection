import cv2 as cv
import pygame

pygame.init()

caption = "Telekinesis"

cap = cv.VideoCapture(0)

if not cap.isOpened():
	print("Cannot open camera")
	exit()


# IMAGE
darkness = cv.imread(cv.samples.findFile("assets/black.jpg"))

if darkness is None:
	sys.exit("Cound not read image")

# GAME LOOP
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
	ret, frame = cap.read()
	# ret is a boolean variable that returns true if the frame is available.

	if not ret:
		print("Can't receive frame")
		running = False

	# SET COLOR
	camColor = cv.applyColorMap(frame, cv.COLORMAP_OCEAN)
	
	cv.imshow(caption, camColor)

cap.release()
cv.destroyAllWindows()

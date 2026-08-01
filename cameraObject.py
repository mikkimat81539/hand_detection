# THIS FILE INCLUDES CAMERA STUFF

import pygame
import cv2 as cv
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
import numpy as np
from numpy import *


class Camera_Detection:
	# TIME
	start_time = time.time()
	

	# DEFINE TASKS
	BaseOptions = mp.tasks.BaseOptions
	HandLandmarker = mp.tasks.vision.HandLandmarker
	HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
	VisionRunningMode = mp.tasks.vision.RunningMode

	# LOAD MODEL
	MODEL_PATH = "assets/hand_landmarker.task"

	# CREATE TASKS
	options = HandLandmarkerOptions(
		base_options = BaseOptions(model_asset_path=MODEL_PATH),
		running_mode=VisionRunningMode.VIDEO,
		min_hand_detection_confidence = 0.5,
		min_hand_presence_confidence = 0.5,
		min_tracking_confidence = 0.5,
		num_hands = 2
	)	
	
	landmarker = HandLandmarker.create_from_options(options)


	# LOAD CAMERA FROM OPENCV	
	cap = cv.VideoCapture(1)

	if not cap.isOpened():
		exit()

	@staticmethod
	def Camera(surface):
		# capture frame by frame
		ret, frame = Camera_Detection.cap.read()

		if not ret:
			exit()

		timestamp_ms = int((time.time() - Camera_Detection.start_time) * 1000)

		# CAMERA WINDOW
		frame = np.fliplr(frame) # flip camera
		frame = np.rot90(frame)	# rotate camera
	
		frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

		frame = cv.resize(frame, (210, 320)) # resize camera screen

		# Convert the frame received from OpenCV to a MediaPipe’s Image object.
		mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

		# HAND CONNECTORS
		result = Camera_Detection.landmarker.detect_for_video(mp_image, timestamp_ms) # hand_landmarker_result

		connection = [
		(0,1),(1,2),(2,3),(3,4),	# thumb
		(0,5),(5,6),(6,7),(7,8),	# index finger
		(0,9),(9,10),(10,11),(11,12),	# middle finger
		(0,13),(13,14),(14,15),(15,16),	# ring finger
		(0,17),(17,18),(18,19),(19,20),	# pinky
		(5,9),(9,13),(13,17)		# palm
		]

		height, width, throwaway = frame.shape # get the actual frame dimensions

		for i in result.hand_landmarks:
			for j in i:
				x = int(j.x*width)
				y = int(j.y*height)

				cv.circle(frame,(x, y), 3, (255,0,0), -1)

			for start, end in connection:
				x1, y1 = int(i[start].x*width), int(i[start].y*height)
				x2, y2 = int(i[end].x*width), int(i[end].y*height)

				cv.line(frame,(x1, y1),(x2, y2),(0,255,0),1)

		# TURN ARRAY INTO PYGAME SURFACE
		camArray = pygame.surfarray.make_surface(frame) # Copy an array to a new surface

		surface.blit(camArray, (0, 0)) # BLIT ONTO PYGAME SURFACE

#		cap.release()
#		cv.destroyAllWindows()

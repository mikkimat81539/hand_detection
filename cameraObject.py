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
	def Camera(surface):
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

		# capture frame by frame
		ret, frame = cap.read()

		if not ret:
			running = False

		timestamp_ms = int((time.time() - start_time) * 1000)

		# CAMERA WINDOW
		frame = np.fliplr(frame) # flip camera
		frame = np.rot90(frame)	# rotate camera
	
		frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

		frame = cv.resize(frame, (210, 320)) # resize camera screen

		# Convert the frame received from OpenCV to a MediaPipe’s Image object.
		mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

		# HAND CONNECTORS
		result = landmarker.detect_for_video(mp_image, timestamp_ms) # hand_landmarker_result

		height, width, throwaway = frame.shape # get the actual frame dimensions

		for i in result.hand_landmarks:
			for j in i:
				x = int(j.x*width)
				y = int(j.y*height)

				cv.circle(frame,(x, y), 2, (0,255,0), -1)

		# TURN ARRAY INTO PYGAME SURFACE
		camArray = pygame.surfarray.make_surface(frame) # Copy an array to a new surface

		surface.blit(camArray, (0, 0)) # BLIT ONTO PYGAME SURFACE

		cap.release()
		cv.destroyAllWindows()

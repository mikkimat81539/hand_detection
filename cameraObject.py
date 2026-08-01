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
	

		# LOAD CAMERA FROM OPENCV	
		cap = cv.VideoCapture(1)
		
		if not cap.isOpened():
			exit()

		# capture frame by frame
		ret, frame = cap.read()

		if not ret:
			running = False

		frame = np.fliplr(frame) # flip camera
		frame = np.rot90(frame)	# rotate camera
	
		frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

		frame = cv.resize(frame, (210, 320)) # resize camera screen

		camArray = pygame.surfarray.make_surface(frame) # Copy an array to a new surface


		surface.blit(camArray, (0, 0))

		cap.release()
		cv.destroyAllWindows()

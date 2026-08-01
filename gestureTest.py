import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import time

from numpy import *

import cv2 as cv

# define time
start_time = time.time()

# define tasks
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


# define model
MODEL_PATH = "assets/hand_landmarker.task"

# Create the task

# inside is the mp.tasks.vision.HandLandmarkerOptions
options = HandLandmarkerOptions(base_options=BaseOptions(model_asset_path= MODEL_PATH), 
	running_mode = vision.RunningMode.VIDEO,
	min_hand_detection_confidence = 0.5,
	min_hand_presence_confidence = 0.5,
	min_tracking_confidence = 0.5,
	num_hands = 2)

# this is the mp.tasks.vision.HandLandmarker class
with HandLandmarker.create_from_options(options) as landmarker:
	# Load my camera
	cap = cv.VideoCapture(1) # initialize camera

	if not cap.isOpened():
		exit()

	running = True

	while running:
		ret, frame = cap.read()

		# Elapsed Time
		timestamp = int((time.time() - start_time) * 1000)

		# print(frame)

		# PREPARE DATA

		# Convert the frame received from OpenCV to a MediaPipe’s Image object.
		camColor = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

		mp_image = mp.Image(image_format=mp.ImageFormat.SRGBA, data=camColor)

		if not ret:
			running = False

		# camColor = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

		hand_landmarker_result = landmarker.detect_for_video(mp_image, timestamp)	

		# HAND DOTS
		if hand_landmarker_result.hand_landmarks:
			for hand_landmarks in hand_landmarker_result.hand_landmarks:
				for landmark in hand_landmarks:
					x = int(landmark.x * frame.shape[1])
					y = int(landmark.y * frame.shape[0])

					cv.circle(frame, (x, y), 5, (0, 255, 0), -1)

		# print(len(hand_landmarker_result.hand_landmarks))
	
		cv.imshow('Telekinesis', frame)

		if cv.waitKey(1) == ord('q'):
			running = False

	#cap.release()
	#cv.destroyAllWindows()


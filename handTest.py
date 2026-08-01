import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2 as cv
import time
import numpy as np
from numpy import *

# TIME
start_time = time.time()

# DEFINE CLASSES
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult

# DEFINE MODEL
MODEL_PATH = "assets/hand_landmarker.task"

# CREATE THE TASK
options = HandLandmarkerOptions(
	base_options = BaseOptions(model_asset_path = MODEL_PATH),
	running_mode = VisionRunningMode.VIDEO,
	min_hand_detection_confidence = 0.5,
	min_hand_presence_confidence = 0.5,
	min_tracking_confidence = 0.5,
	num_hands = 2
)

# PREPARE DATA
landmarker = HandLandmarker.create_from_options(options)

# CAMERA
cap = cv.VideoCapture(1)

if not cap.isOpened():
	exit()

running = True

while running:
	ret, frame = cap.read()

	if not ret:
		running = False

	timestamp_ms = int((time.time() - start_time)*1000)

	# Convert the frame received from OpenCV to a MediaPipe’s Image object.
	mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)


	# Perform hand landmarks detection
	hand_landmarker_result = landmarker.detect_for_video(mp_image,	timestamp_ms)

	# 1)Get the hand landmark results from MediaPipe.
	# 2)Draw a small dot/circle at each landmark point
	# 3)Draw lines between specific landmarks

	height, width, throwaway= frame.shape # get the actual frame dimensions:

	for i in hand_landmarker_result.hand_landmarks: # this grabs the list of 21 hand connectors
		for landmark in i: # this allows me to grab each individual point on its axis
			x = int(landmark.x*width) # x values for landmarker
			y = int(landmark.y*height) # y value from landmarker

			#print(x, y)
	
			landmark_index = i.index(landmark)

			start_x = int(i[landmark_index].x * width)
			end_y = int(i[landmark_index].y * height)

			cv.circle(frame, (x,y), 10, (0,255,0), -1) # img, (x, y), radius, color, thickness	

			cv.line(frame, (x, y), (start_x, end_y), (0, 0, 255), 10)
		

	# EXAMPLE of drawing shapes
	#cv.circle(frame,(447,63), 20, (255,0,0), -1) # img, (x, y), radius, color, thickness	
	#cv.line(frame, (100, 100), (200, 10), (0, 0, 255), 10) # img, (x, y), (start, end), color, thickness


	# Handle and display results
	camColor = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

	cv.imshow('Telekinesis', camColor)

	if cv.waitKey(1) == ord('q'):
		running = False

cap.release()
cv.destroyAllWindows()

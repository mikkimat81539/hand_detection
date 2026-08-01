import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2 as cv
import time

# TIME
start_time = time.time()

# DEFINE CLASSES
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

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

	# HAND CONNECTIONS --> each are index for the hand points
	connections = [
		(0,1),(1,2),(2,3),(3,4),	# thumb
		(0,5),(5,6),(6,7),(7,8),	# index finger
		(0,9),(9,10),(10,11),(11,12),	# middle finger
		(0,13),(13,14),(14,15),(15,16),	# ring finger
		(0,17),(17,18),(18,19),(19,20),	# pinky
		(5,9),(9,13),(13,17)		# palm
	]

	height, width, throwaway= frame.shape # get the actual frame dimensions:

	for i in hand_landmarker_result.hand_landmarks: # this grabs the list of 21 hand connectors

		line_landmarks = [] # store the 21 points for the hands so we can connect them

		for landmark in i: # this allows me to grab each individual point on its axis
			x = int(landmark.x*width) # x values for landmarker
			y = int(landmark.y*height) # y value from landmarker

			line_landmarks.append((x, y))

			cv.circle(frame, (x,y), 10, (0,0,255), -1) # img, (x, y), radius, color, thickness	

		for start, end in connections:
			x1, y1 = line_landmarks[start]
			x2, y2 = line_landmarks[end]
			cv.line(frame, (x1, y1), (x2, y2), (255, 255, 255), 10)		


	# EXAMPLE of drawing shapes
	#cv.circle(frame,(447,63), 20, (255,0,0), -1) # img, (x, y), radius, color, thickness	
	#cv.line(frame, (100, 100), (200, 10), (0, 0, 255), 10) # img, (start_x,start_y), (end_x, end_y), color, thickness


	# Handle and display results
	camColor = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

	cv.imshow('Telekinesis', camColor)

	if cv.waitKey(1) == ord('q'):
		running = False

cap.release()
cv.destroyAllWindows()

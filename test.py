import cv2
import numpy as np
import playsound
import threading



# Initialize the video capture
cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera

# Define the lower and upper bounds for the fire color in HSV
lower_bound = np.array([0, 100, 100])
upper_bound = np.array([10, 255, 255])

def play_alarm_sound_function():
	while True:
		playsound.playsound('alarm-sound.mp3',True)




while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    

    if not ret:
        break

    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to identify the red/orange areas (potential fire)
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    # Apply some morphological operations to clean up the mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check for fire detection
    fire_detected = False
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:  # Adjust this threshold as needed
        
        
            fire_detected = True
            break

    # Display the original frame and the mask
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Fire Mask', mask)
    
    
    if fire_detected:
        print("Fire detected!")
        threading.Thread(target=play_alarm_sound_function).start()
        # break
        
    else:
        print("Fire is not detected!")
        # break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


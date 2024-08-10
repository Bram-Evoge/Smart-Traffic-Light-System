import time
import threading
import RPi.GPIO as GPIO
from picamera import PiCamera
import cv2
import numpy as np

# Constants
ULTRASONIC_TRIGGER_PIN = 23
ULTRASONIC_ECHO_PIN = 24
CAMERA_RESOLUTION = (640, 480)

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ULTRASONIC_TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ULTRASONIC_ECHO_PIN, GPIO.IN)

# Initialize camera
camera = PiCamera()
camera.resolution = CAMERA_RESOLUTION

# Function to read distance from ultrasonic sensor
def get_distance():
    GPIO.output(ULTRASONIC_TRIGGER_PIN, True)
    time.sleep(0.00001)
    GPIO.output(ULTRASONIC_TRIGGER_PIN, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(ULTRASONIC_ECHO_PIN) == 0:
        start_time = time.time()
    
    while GPIO.input(ULTRASONIC_ECHO_PIN) == 1:
        stop_time = time.time()
    
    elapsed_time = stop_time - start_time
    distance = (elapsed_time * 34300) / 2  # Speed of sound = 34300 cm/s
    return distance

# Function for camera processing (using OpenCV)
def process_camera():
    # Capture an image from the camera
    camera.capture('image.jpg')
    
    # Process the image using OpenCV
    image = cv2.imread('image.jpg')
    # Add your OpenCV image processing code here
    
    # Example: Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Example: Perform edge detection
    edges = cv2.Canny(gray_image, 100, 200)
    
    # Display processed image (optional for testing)
    cv2.imshow('Processed Image', edges)
    cv2.waitKey(1000)  # Display for 1 second
    cv2.destroyAllWindows()

# Traffic light control function
def control_traffic_lights():
    while True:
        distance = get_distance()
        
        # Example logic: Change traffic lights based on distance
        if distance < 50:
            print("Vehicle detected. Changing lights to green.")
            # Code to change traffic lights to green
        else:
            print("No vehicle detected. Keeping lights red.")
            # Code to keep traffic lights red
        
        time.sleep(2)  # Adjust timing as needed

# Main function
if __name__ == '__main__':
    try:
        # Create and start threads for camera processing and traffic light control
        camera_thread = threading.Thread(target=process_camera)
        traffic_light_thread = threading.Thread(target=control_traffic_lights)
        
        camera_thread.start()
        traffic_light_thread.start()
        
        camera_thread.join()
        traffic_light_thread.join()
        
    except KeyboardInterrupt:
        print("Exiting program.")
    
    finally:
        GPIO.cleanup()

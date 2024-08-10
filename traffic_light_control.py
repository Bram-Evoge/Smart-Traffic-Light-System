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

# Traffic light states
class TrafficLightState:
    RED = 0
    YELLOW = 1
    GREEN = 2

# Traffic directions and states
traffic_directions = ['A', 'B', 'C', 'D']
traffic_states = {
    'A': TrafficLightState.RED,
    'B': TrafficLightState.RED,
    'C': TrafficLightState.RED,
    'D': TrafficLightState.RED
}

# Traffic light timings (in seconds)
GREEN_LIGHT_DURATION = 10 # normally 60 seconds in real world system
YELLOW_LIGHT_DURATION = 3  # normally 5 seconds in real world system
RED_LIGHT_DURATION = 10  # normally 60 seconds in real world system

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
        for direction in traffic_directions:
            if direction in traffic_states and traffic_states[direction] != TrafficLightState.RED:
                continue  # Skip directions with no traffic or already green/yellow
            
            distance = get_distance()
            
            # Example logic: Determine if there is traffic in the direction
            if direction == 'A' and distance < 50:
                traffic_states[direction] = TrafficLightState.GREEN
            elif direction == 'B' and distance < 50:
                traffic_states[direction] = TrafficLightState.GREEN
            elif direction == 'C' and distance < 50:
                traffic_states[direction] = TrafficLightState.GREEN
            elif direction == 'D' and distance < 50:
                traffic_states[direction] = TrafficLightState.GREEN
            else:
                traffic_states[direction] = TrafficLightState.RED
        
        # Update traffic lights based on states
        update_traffic_lights()
        
        time.sleep(2)  # Adjust timing as needed

# Function to update traffic lights based on states
def update_traffic_lights():
    for direction in traffic_directions:
        state = traffic_states.get(direction, TrafficLightState.RED)
        set_traffic_light_state(direction, state)

# Function to set traffic light state for a direction
def set_traffic_light_state(direction, state):
    # Implement code to control physical traffic lights here
    # Example: Use GPIO to switch relays or LEDs
    if state == TrafficLightState.RED:
        print(f"Setting traffic lights for direction {direction} to RED")
    elif state == TrafficLightState.YELLOW:
        print(f"Setting traffic lights for direction {direction} to YELLOW")
    elif state == TrafficLightState.GREEN:
        print(f"Setting traffic lights for direction {direction} to GREEN")
    else:
        print(f"Invalid traffic light state for direction {direction}")

    # Placeholder for actual GPIO control
    # Replace with your own GPIO control logic

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
        camera.close()

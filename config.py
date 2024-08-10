# Configuration parameters for smart traffic light control system

# GPIO pins
ULTRASONIC_TRIGGER_PIN = 23
ULTRASONIC_ECHO_PIN = 24

# Camera settings
CAMERA_RESOLUTION = (640, 480)
CAMERA_FRAMERATE = 30

# Traffic light timings (in seconds)
GREEN_LIGHT_DURATION = 10
YELLOW_LIGHT_DURATION = 3
RED_LIGHT_DURATION = 10

# Thresholds for ultrasonic sensor
DISTANCE_THRESHOLD = 50  # Distance in centimeters to trigger light change

# Paths for saving images (example paths)
IMAGE_SAVE_PATH = '/home/pi/smart_traffic_light/images/'
LOG_FILE_PATH = '/home/pi/smart_traffic_light/logs/'

# Other constants
MAX_DISTANCE = 400  # Maximum reliable distance measurement for the ultrasonic sensor

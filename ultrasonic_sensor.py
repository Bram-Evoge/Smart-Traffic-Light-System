import RPi.GPIO as GPIO
import time

# Constants
ULTRASONIC_TRIGGER_PIN = 23
ULTRASONIC_ECHO_PIN = 24

class UltrasonicSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(ULTRASONIC_TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(ULTRASONIC_ECHO_PIN, GPIO.IN)

    def get_distance(self):
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

    def cleanup(self):
        GPIO.cleanup()

# Example usage (for testing)
if __name__ == '__main__':
    try:
        ultrasonic_sensor = UltrasonicSensor()

        while True:
            distance = ultrasonic_sensor.get_distance()
            print(f"Distance: {distance:.2f} cm")
            time.sleep(1)  # Adjust frequency of distance readings as needed

    except KeyboardInterrupt:
        print("Exiting program.")
    
    finally:
        ultrasonic_sensor.cleanup()

from picamera import PiCamera
import cv2
import numpy as np
import time

# Constants
CAMERA_RESOLUTION = (640, 480)

class CameraModule:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = CAMERA_RESOLUTION

    def capture_image(self, save_path='captured_image.jpg'):
        """Captures an image using PiCamera and saves it."""
        self.camera.capture(save_path)

    def preprocess_image(self, image_path):
        """Preprocesses an image using OpenCV."""
        image = cv2.imread(image_path)
        # Example preprocessing: convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image

    def detect_edges(self, image):
        """Detects edges in a preprocessed image using Canny edge detection."""
        edges = cv2.Canny(image, 100, 200)
        return edges

    def detect_objects(self, image):
        """Detects objects or features in an image using OpenCV algorithms."""
        # Example object detection code (placeholder)
        # Replace with actual object detection logic
        return []

    def cleanup(self):
        """Cleans up resources (e.g., closes PiCamera)."""
        self.camera.close()

# Example usage (for testing)
if __name__ == '__main__':
    try:
        camera_module = CameraModule()

        # Capture an image
        camera_module.capture_image('captured_image.jpg')

        # Preprocess the captured image
        preprocessed_image = camera_module.preprocess_image('captured_image.jpg')

        # Detect edges in the preprocessed image
        edges = camera_module.detect_edges(preprocessed_image)

        # Example: Display the processed image (optional for testing)
        cv2.imshow('Processed Image', edges)
        cv2.waitKey(0)  # Wait indefinitely until a key is pressed
        cv2.destroyAllWindows()

    except KeyboardInterrupt:
        print("Exiting program.")

    finally:
        camera_module.cleanup()

import cv2
import numpy as np
from styx_msgs.msg import TrafficLight

class TLClassifier(object):
    def __init__(self):
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image
        Args:
            image (cv::Mat): image containing the traffic light
        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)
        """
        hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        red_low = np.array([0, 100, 100],np.uint8)
        red_high = np.array([10, 255, 255],np.uint8)        
        red1_low = np.array([160, 100, 100],np.uint8)
        red1_high = np.array([179, 255, 255],np.uint8)
        
        if cv2.countNonZero(cv2.inRange(hsv_image,red_low,red_high))+cv2.countNonZero(cv2.inRange(hsv_image,red1_low,red1_high))>45:
            return TrafficLight.RED
        
        yel_low = np.array([28, 100, 100],np.uint8)
        yel_high = np.array([48, 255, 255],np.uint8)
        if cv2.countNonZero(cv2.inRange(hsv_image, yel_low, yel_high)) > 45:
            return TrafficLight.YELLOW
        
        gr_low = np.array([64, 100, 100],np.uint8)
        gr_high = np.array([100, 255, 255],np.uint8)
        if cv2.countNonZero(cv2.inRange(hsv_image, gr_low, gr_high)) > 45:
            return TrafficLight.GREEN
        
        return TrafficLight.UNKNOWN
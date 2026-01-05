"""
Frame Processors
Implementation of various image processing algorithms
"""

import cv2
import numpy as np
from abc import ABC, abstractmethod


class FrameProcessor(ABC):
    """Abstract base class for all processors."""
    
    @abstractmethod
    def process(self, frame: np.ndarray) -> np.ndarray:
        """Process a single frame."""
        pass


class BlurProcessor(FrameProcessor):
    """Gaussian blur for noise reduction."""
    
    def __init__(self, kernel_size: int = 5):
        self.kernel_size = kernel_size
    
    def process(self, frame: np.ndarray) -> np.ndarray:
        return cv2.GaussianBlur(frame, (self.kernel_size, self.kernel_size), 0)


class EdgeDetectionProcessor(FrameProcessor):
    """Canny edge detection algorithm."""
    
    def __init__(self, threshold1: int = 50, threshold2: int = 150):
        self.threshold1 = threshold1
        self.threshold2 = threshold2
    
    def process(self, frame: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, self.threshold1, self.threshold2)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
class MotionDetectionProcessor(FrameProcessor):
    """Simple motion detection using frame differencing."""
    
    def __init__(self, threshold: int = 25):
        self.prev_frame = None
        self.threshold = threshold
    
    def process(self, frame: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        
        if self.prev_frame is None:
            self.prev_frame = gray
            return frame
        
        # Frame differencing
        diff = cv2.absdiff(self.prev_frame, gray)
        thresh = cv2.threshold(diff, self.threshold, 255, cv2.THRESH_BINARY)[1]
        
        # Find contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, 
                                       cv2.CHAIN_APPROX_SIMPLE)
        
        result = frame.copy()
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        self.prev_frame = gray
        return result
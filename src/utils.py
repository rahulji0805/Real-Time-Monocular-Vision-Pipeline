"""
Utility Functions
Helper classes and functions for the pipeline
"""

import time


class FPSCounter:
    """Calculate frames per second."""
    
    def __init__(self):
        self.prev_time = time.time()
        self.fps = 0.0
    
    def update(self) -> float:
        """Update and return current FPS."""
        curr_time = time.time()
        self.fps = 1.0 / (curr_time - self.prev_time + 1e-6)
        self.prev_time = curr_time
        return self.fps
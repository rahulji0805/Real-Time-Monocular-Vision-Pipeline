"""
Main Vision Pipeline Class
Handles camera capture, processing, and display
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import cv2
import numpy as np
from typing import List, Optional
from src.processors import FrameProcessor, EdgeDetectionProcessor, BlurProcessor, MotionDetectionProcessor
from src.utils import FPSCounter





class VisionPipeline:
    """
    Real-time vision processing pipeline.
    
    Attributes:
        camera_id (int): Camera device ID
        width (int): Frame width
        height (int): Frame height
        processors (List): Chain of frame processors
    """
    
    def __init__(self, camera_id: int = 0, width: int = 640, height: int = 480):
        self.camera_id = camera_id
        self.width = width
        self.height = height
        self.cap: Optional[cv2.VideoCapture] = None
        self.processors: List[FrameProcessor] = []
        self.fps_counter = FPSCounter()
        self.running = False
        self.frame_count = 0
        
    def add_processor(self, processor: FrameProcessor) -> None:
        """Add a processor to the pipeline."""
        self.processors.append(processor)
        print(f"Added: {processor.__class__.__name__}")
        
    def remove_processor(self, processor: FrameProcessor) -> None:
        """Remove a processor from the pipeline."""
        if processor in self.processors:
            self.processors.remove(processor)
            print(f"Removed: {processor.__class__.__name__}")
    
    def clear_processors(self) -> None:
        """Clear all processors."""
        self.processors.clear()
        print("All processors cleared")
    
    def init_camera(self) -> bool:
        """Initialize camera capture."""
        self.cap = cv2.VideoCapture(self.camera_id)
        
        if not self.cap.isOpened():
            print(f"ERROR: Cannot open camera {self.camera_id}")
            return False
        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        
        print(f"Camera initialized: {self.width}x{self.height}")
        return True
    
    def process_frame(self, frame: np.ndarray) -> np.ndarray:
        """
        Apply all processors to frame sequentially.
        
        Args:
            frame: Input frame (BGR format)
            
        Returns:
            Processed frame
        """
        result = frame.copy()
        
        for processor in self.processors:
            result = processor.process(result)
        
        return result
    
    def display_info(self, frame: np.ndarray, fps: float) -> None:
        """Draw information overlay on frame."""
        # FPS display
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        # Active processors
        cv2.putText(frame, f"Processors: {len(self.processors)}", (10, 60),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Frame count
        cv2.putText(frame, f"Frame: {self.frame_count}", (10, 90),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    def save_frame(self, frame: np.ndarray) -> None:
        """Save current frame to output directory."""
        import os
        os.makedirs('output', exist_ok=True)
        filename = f"output/frame_{self.frame_count}.png"
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
    
    def run(self) -> None:
        """Main processing loop."""
        if not self.init_camera():
            return
        
        self.running = True
        print("\n=== Vision Pipeline Started ===")
        print("Controls:")
        print("  q - Quit Application")
        print("  s - Save Current Frame")
        print("  0 - Clear processors")
        print("  1 - Edge Detection")
        print("  2 - Blur Filter")
        print("  3 - Motion Detection ")
        print("================================\n")
        edge_processor = EdgeDetectionProcessor()
        blur_processor = BlurProcessor()
        motion_processor = MotionDetectionProcessor()

        
        while self.running:
            ret, frame = self.cap.read()
            
            if not ret:
                print("ERROR: Failed to capture frame")
                break
            
            # Process frame
            processed = self.process_frame(frame)
            
            # Update metrics
            fps = self.fps_counter.update()
            self.frame_count += 1
            
            # Display info
            self.display_info(processed, fps)
            
            # Show windows
            cv2.imshow('Processed', processed)
            cv2.imshow('Original', frame)
            
            # Handle keyboard input
            key = cv2.waitKey(10) & 0xFF

            if key == ord('q'):
                self.running = False

            elif key == ord('s'):
                self.save_frame(processed)

            elif key == ord('0'):
                self.clear_processors()

            elif key == ord('1'):
                if edge_processor in self.processors:
                    self.remove_processor(edge_processor)
                else:
                    self.add_processor(edge_processor)

            elif key == ord('2'):
                if blur_processor in self.processors:
                    self.remove_processor(blur_processor)
                else:
                    self.add_processor(blur_processor)
            elif key == ord('3'):
                if motion_processor in self.processors:
                    self.remove_processor(motion_processor)
                else:
                    self.add_processor(motion_processor)
        self.add_processor(motion_processor)

        self.cleanup()  
    
    def cleanup(self) -> None:
        """Release resources."""
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()
        print("\n=== Pipeline Stopped ===")
        print(f"Total frames processed: {self.frame_count}")
def main():
    pipeline = VisionPipeline(camera_id=0)
    pipeline.run()

if __name__ == "__main__":
    main()


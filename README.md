# Real-Time-Monocular-Vision-Pipeline

**Course:** Computer Vision / Image Processing  
**Technology:** OpenCV, Python, NumPy

## Project Overview

A modular real-time computer vision system that captures video from a webcam and applies various image processing techniques. The project demonstrates understanding of:

- Video capture and frame processing
- Image filtering and enhancement
- Edge detection algorithms
- Real-time performance optimization
- Object-oriented design patterns

## System Requirements

- Python 3.8+
- Webcam/Camera
- 4GB RAM minimum

## Installation
```bash
git clone https://github.com/yourusername/monocular-vision-pipeline.git
cd monocular-vision-pipeline
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python examples/basic_demo.py
```

### With Specific Processors
```python
from src.vision_pipeline import VisionPipeline
from src.processors import EdgeDetectionProcessor

pipeline = VisionPipeline(camera_id=0)
pipeline.add_processor(EdgeDetectionProcessor(threshold1=50, threshold2=150))
pipeline.run()
```

## Features Implemented

### Core Features
- ✅ Real-time video capture (30+ FPS)
- ✅ Modular processor architecture
- ✅ Multiple image processing algorithms
- ✅ Performance monitoring (FPS counter)
- ✅ Interactive controls

### Image Processing Techniques
1. **Gaussian Blur** - Noise reduction using convolution
2. **Edge Detection** - Canny algorithm implementation
3. **Motion Detection** - Frame differencing


## Keyboard Controls

| Key | Action |
|-----|--------|
| `q` | Quit application |
| `1` | Toggle edge detection |
| `2` | Toggle blur filter |
| `3` | Toggle motion detection |
| `0` | Clear all processors |
| `s` | Save current frame |

## Architecture
```Text
VisionPipeline
├── Camera Manager (Capture)
├── Processor Chain (Sequential processing)
├── Display Manager (Visualization)
└── FPS Counter (Performance monitoring)
```
## Key Concepts Demonstrated

1. **Object-Oriented Programming**: Abstract base classes, inheritance
2. **Design Patterns**: Strategy pattern for processors
3. **Computer Vision**: Filtering, edge detection, morphological operations
4. **Real-time Processing**: Efficient frame handling
5. **NumPy Operations**: Array manipulation, mathematical operations

## Code to run the Program:
It should be run in the terminal only.
```bash
python -m src.vision_pipeline
```

## Future Enhancements

- Object detection using YOLO
- Face recognition
- Optical flow visualization
- Multiple camera support

## References

- OpenCV Documentation: https://docs.opencv.org/
- Digital Image Processing - Gonzalez & Woods
- Computer Vision: Algorithms and Applications - Szeliski

## Author
**Rahul Bhukal**
Department of Electronics and Communication Engineering
Deenbandhu Chhotu Ram University of Science and Technology

## License

MIT License


## Repository Structure

```text
monocular-vision-pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── vision_pipeline.py      # Main pipeline class
│   ├── processors.py           # processors used
|   ├──__main__.py          
│   └── utils.py                # Helper functions
├── docs/
│   ├── report.md              # Project report/documentation
│   └── screenshots/           # Results screenshots
└── output/                    # Saved videos/images
```

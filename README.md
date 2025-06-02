# Real-Time Object Detection

A Python application that performs real-time object detection using YOLOv5 and webcam feed with a simple Tkinter GUI.

![image](https://github.com/user-attachments/assets/47e4f518-11fd-43fa-bb76-9dfd92c1fa19)


## Features

- **Live Detection**: Real-time object detection from webcam feed
- **YOLOv5 Integration**: Uses pre-trained YOLOv5x model for accurate detection
- **Visual Feedback**: Bounding boxes with confidence scores and class labels
- **FPS Counter**: Live frame rate monitoring
- **Clean GUI**: Simple Tkinter interface for easy viewing

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

3. **Usage**
   - The application will automatically access your default camera (index 0)
   - Detected objects appear with green bounding boxes
   - Confidence threshold is set to 0.4 (adjustable in code)
   - Press the window's close button to exit

## Project Structure

```
├── main.py              # Main application entry point
├── model/
│   └── load_model.py    # YOLOv5 model loading
├── webcam/
│   ├── capture.py       # Webcam handling
│   ├── inference.py     # Object detection logic
│   └── display.py       # Frame rendering and UI
└── requirements.txt     # Dependencies
```

## Configuration

- **Camera**: Change `src` parameter in `main.py` for different cameras
- **Confidence**: Adjust threshold in `ObjectDetector` initialization
- **Resolution**: Modify width/height in `WebcamCapturer` setup
- **Colors**: Customize bounding box appearance in `DisplayFrames`

## Requirements

- Python 3.7+
- Webcam/Camera device
- CUDA-compatible GPU (optional, for better performance)

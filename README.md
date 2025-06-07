# Real-Time Face and Emotion Detection

This project uses your webcam to perform real-time face detection and emotion recognition. It displays the video feed with bounding boxes around detected faces and labels the recognized emotions.

## Features

- **Real-time face detection:** Detects faces in the live webcam feed.
- **Emotion recognition:** Identifies the dominant emotion of detected faces (e.g., happy, sad, angry, neutral).
- **Bounding boxes and emotion labels:** Clearly visualizes detected faces with rectangular bounding boxes and displays the corresponding emotion label.
- **Dynamic resizing:** The output window can be resized dynamically by the user.

## Requirements

- opencv-python
- fer
- tkinter

## Installation

```
pip install opencv-python fer
```

## Usage

To run the script:

```
python webcamChecker.py
```

Press 'q' to quit the application.

## How it Works

- **Video Capture:** The application captures video from the default webcam using OpenCV.
- **Emotion Detection:** The FER (Face Emotion Recognition) library is used to detect faces and recognize emotions from the video frames.
- **Display:** OpenCV is utilized to display the video feed, superimposing bounding boxes around detected faces and labeling them with the recognized emotions.

## License

This project is currently not licensed. Please add a license if you intend to share or distribute it.

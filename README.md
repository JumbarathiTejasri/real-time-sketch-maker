# 🖼️ Real-Time Sketch Maker

A Python application that captures live video from your webcam and converts each frame into a pencil sketch.

## 📸 How It Works

1. Capture webcam input
2. Convert frames to grayscale
3. Apply Gaussian blur
4. Detect edges using Canny
5. Invert edges to get a sketch effect

## 🛠️ Technologies Used

- Python
- OpenCV (cv2)
- NumPy
- Webcam

## ▶️ Run It

```bash
pip install -r requirements.txt
python main.py
Press s to save sketch image

Press q to quit
```

📁 Output
Saved images go into the output/ folder.

📷 Demo
<!-- Optional if you record a video -->

📄 License
MIT License 
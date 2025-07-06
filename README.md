
# 🖼️ Real-Time Sketch Maker

A Python application that captures live video from your webcam and converts each frame into a pencil sketch in real time.

## 📸 How It Works

1. Captures webcam input
2. Converts frames to grayscale
3. Applies Gaussian blur
4. Detects edges using Canny
5. Inverts edges to generate a pencil sketch effect
6. Allows users to save sketches by pressing a key

## 🛠️ Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Webcam

## 📁 Folder Structure

real-time-sketch-maker/
├── main.py
├── requirements.txt
├── output/  ← Saved sketch images go here
│ └── pencil.png  ← Example sketch image
├── README.md


> 📝 Note: NOTE:create output folder after cloning of repo

## ▶️ How to Run

```bash
# 1. (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate        # On Windows
# or
source venv/bin/activate     # On macOS/Linux

# 2. Install required libraries
pip install -r requirements.txt

# 3. Run the app
python main.py
🎮 Controls
Press s → Save the current sketch to the output/ folder

Press q → Quit the application

🖼️ Example Output
An example of a sketch saved inside the output folder.

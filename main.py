import cv2
import numpy as np
import time
import random

# Step 1: Open webcam
cap = cv2.VideoCapture(0)

# Step 2: Show live video and wait for 3 seconds
start_time = time.time()
captured_frame = None

print("📷 Scanning... Hold still for 3 seconds...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    elapsed = time.time() - start_time

    # After 3 seconds, capture the frame
    if elapsed >= 3 and captured_frame is None:
        captured_frame = frame.copy()
        print("✅ Snapshot captured!")

        # Convert to sketch now
        gray = cv2.cvtColor(captured_frame, cv2.COLOR_BGR2GRAY)
        inverted = cv2.bitwise_not(gray)
        blur = cv2.GaussianBlur(inverted, (25, 25), 0)
        inverted_blur = cv2.bitwise_not(blur)
        sketch = cv2.divide(gray, inverted_blur, scale=256.0)

        # Create a blank white canvas for animation
        canvas = np.full_like(sketch, 255)

        # Get pixel positions (y, x) and shuffle for natural effect
        pixels = np.column_stack(np.where(sketch < 255))
        random.shuffle(pixels)

        # Start drawing timer
        draw_index = 0

    # Step 3: Animate sketch drawing
    if captured_frame is not None and draw_index < len(pixels):
        # Draw 500 pixels at a time to simulate stroke-by-stroke effect
        for y, x in pixels[draw_index:draw_index + 500]:
            canvas[y, x] = sketch[y, x]
        draw_index += 500

        sketch_bgr = cv2.cvtColor(canvas, cv2.COLOR_GRAY2BGR)
    elif captured_frame is not None:
        sketch_bgr = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
    else:
        # Before 3 seconds, show blank sketch canvas
        sketch_bgr = np.full((480, 640, 3), 255, dtype=np.uint8)

    # Combine live video and animated sketch
    combined = np.hstack((frame, sketch_bgr))
    cv2.imshow("🖼️ Live | ✏️ Drawing", combined)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s') and captured_frame is not None:
        cv2.imwrite("output/sketch_result.png", canvas)
        print("💾 Sketch saved to output/sketch_result.png")

cap.release()
cv2.destroyAllWindows()

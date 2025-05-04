# crowd_detector.py

import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import time
import os

# Initialize model
model = YOLO("yolov8n.pt")

# Output CSV path
CSV_FILE = "crowd_data.csv"

# Start webcam
cap = cv2.VideoCapture(0)

# Create CSV if not exists
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["timestamp", "count"])
    df.to_csv(CSV_FILE, index=False)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        detections = results[0]
        count = sum(1 for d in detections.boxes.cls if int(d) == 0)

        # Display on screen
        cv2.putText(frame, f"People: {count}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Crowd Detector", frame)

        # Append data
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pd.DataFrame([[timestamp, count]], columns=["timestamp", "count"]).to_csv(CSV_FILE, mode='a', header=False, index=False)

        # Stop on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

cap.release()
cv2.destroyAllWindows()

# Plot the crowd graph
data = pd.read_csv(CSV_FILE)
plt.figure(figsize=(10, 4))
plt.plot(data["timestamp"], data["count"], marker='o')
plt.xticks(rotation=45)
plt.title("Crowd Over Time")
plt.xlabel("Time")
plt.ylabel("People Count")
plt.tight_layout()
plt.show()

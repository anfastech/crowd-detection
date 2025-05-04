# Crowd Dictation (Detection) MVP

Track how crowded your shop, café, or public space is using a simple webcam and AI. This project uses a webcam to detect and count people in real-time, providing a live graph of crowd frequency over time.

## MVP Overview

This is the **Minimum Viable Product (MVP)** for a real-time **Crowd Detection System** using:
- YOLOv8 (for person detection)
- OpenCV (for webcam + display)
- Matplotlib (for graph plotting)

You can later convert this into a full dashboard with alerts, database logging, or even deploy on edge devices like Raspberry Pi or Jetson Nano.

---

## 🧪 Basic Flow:

```csharp
[Webcam Feed]
     ↓
[Detect Humans using ML model]
     ↓
[Count People Per Frame]
     ↓
[Store in CSV / Memory]
     ↓
[Plot as Line Graph over Time]

```

---

## Features

- ✅ Real-time webcam feed
- ✅ Human detection using YOLOv8
- ✅ People counting logic
- ✅ Timestamped graph plotting
- ✅ Threshold-ready logic (can trigger alerts)
- 📈 Crowd frequency over time

---

## Tech Stack (MVP)

| Layer | Tools |
|-------|-------|
| Model | [YOLOv8](https://github.com/ultralytics/ultralytics) |
| View  | OpenCV display, Matplotlib graph |
| Controller | Python script that controls flow between webcam, detection, and graph |

---

Happy Coding!!! anfastech
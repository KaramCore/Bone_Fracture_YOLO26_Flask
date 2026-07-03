# YOLO26m-OBB Flask Detection App

This repository provides a simple web app for detecting objects with oriented bounding boxes (OBB) using a YOLOv26-m-OBB model in ONNX format. The app supports image upload, runs inference, and displays detected results through a Flask web interface.

---

## Features

- **YOLOv26 OBB inference** via [Ultralytics YOLO](https://docs.ultralytics.com/) and ONNX model.
- **Web upload interface** for user-friendly usage.
- **Detection visualization** with image result display.
- Simple and clean UI.

---

## Quickstart

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Install dependencies

This app requires Python 3.11+.

```bash
pip install -r requirements.txt
```

### 3. Prepare your ONNX model

Place your trained YOLOv8 OBB ONNX model at `runs/obb/train/weights/best.onnx`.  
*(You can update this path in `app.py` as needed.)*

### 4. Run the Flask app

```bash
python app.py
```

The app will be available at [http://localhost:5000](http://localhost:5000).

---

## File Structure

```
├── app.py              # Main Flask application
├── infer.py            # YOLO predictor logic
├── requirements.txt    # Required Python packages
├── templates/
│   └── index.html      # Web UI template
├── uploads/            # Uploaded images (auto-created)
├── results/            # Output images (auto-created)
├── runs/               # Place your model here as specified above
├── README.md           # This file
└── .gitignore
```

---

## Usage Instructions

1. Open the web app in your browser.
2. Upload an image file.
3. Press "Detect".
4. The page will refresh and display your image with detected OBB annotations.

---

## Notes

- **Model requirements:** You must provide a compatible YOLOv26 OBB ONNX model. You can train one with [Ultralytics YOLO](https://docs.ultralytics.com/obb/).
- **Output directory** (`results/`) and upload directory (`uploads/`) are created automatically and listed in `.gitignore`.

---

## Troubleshooting

- **Model not found:** Ensure the ONNX model path in `app.py` is correct.
- **Dependency errors:** Reinstall requirements and check your Python version compatibility.

---

## License

Apache-2.0 License

---

## Acknowledgements

- Built with [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- Inspired by open-source object detection apps
---
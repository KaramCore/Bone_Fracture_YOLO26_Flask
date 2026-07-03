from ultralytics import YOLO
import cv2
import os


class Detector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def predict(
        self,
        image_path,
        save_dir="results",
        conf=0.1,
        imgsz=640,
    ):
        os.makedirs(save_dir, exist_ok=True)

        results = self.model.predict(
            source=image_path,
            conf=conf,
            imgsz=imgsz,
            save=False,
            verbose=False,
        )

        result = results[0]

        plotted = result.plot()

        output_path = os.path.join(
            save_dir,
            os.path.basename(image_path)
        )

        cv2.imwrite(output_path, plotted)

        return output_path, result
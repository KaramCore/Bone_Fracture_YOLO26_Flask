from flask import Flask, render_template, request, send_from_directory
import os

from infer import Detector

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

detector = Detector(r"runs\obb\train\weights\best.onnx")


@app.route("/", methods=["GET", "POST"])
def index():

    result_image = None

    if request.method == "POST":

        file = request.files.get("image")

        if file and file.filename:

            image_path = os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )

            file.save(image_path)

            output_path, _ = detector.predict(image_path)

            result_image = os.path.basename(output_path)

    return render_template(
        "index.html",
        result_image=result_image
    )


@app.route("/results/<filename>")
def results(filename):
    return send_from_directory(
        RESULT_FOLDER,
        filename
    )


if __name__ == "__main__":
    app.run(debug=True)
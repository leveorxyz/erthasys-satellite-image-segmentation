import os
import gdown
from flask import Flask, request, jsonify, send_from_directory
from erthasys import ErthaSys
from utils import base64_to_numpy
# from utils import GDriveDownloader
from utils.base64utils import numpy_to_base64

IMG_SIZE = 512  # Input image dims: 512x512 px

erthasys = ErthaSys(IMG_SIZE)
# downloader = GDriveDownloader()

# ... Download and load pre-trained weights
weight_fid = "1y0rLn5YWiVntxGlfXbwgZYAFzXeyi3I9"
weight_path = "erthasys/model/InceptionResNetV2-UNet.h5"

if not os.path.exists(weight_path):
    gdown.download(id=weight_fid, output=weight_path)

erthasys.load_weights(weight_path)

app = Flask(__name__, static_folder="frontend/build")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/erthasys', methods=["POST"])
def record():
    try:
        image = base64_to_numpy(request.json["image"])
        prediction, class_distribution = erthasys.get_segmented_image(image)
        return jsonify(
            success=True,
            prediction=numpy_to_base64(prediction),
            class_distribution=class_distribution
        )

    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify(
            success=False
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

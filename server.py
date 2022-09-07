import os
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="frontend/build")


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


@app.route('/record', methods=["POST"])
def record():
    try:
        pass

    except Exception as e:
        print(f"ERROR: {type(e)}")
        return jsonify(
            success=False
        )

    return jsonify(
        success=True
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

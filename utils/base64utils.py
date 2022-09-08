import io
import base64
import numpy as np

from PIL import Image
from numpy.typing import NDArray


def numpy_to_base64(image: NDArray[np.uint8]) -> str:
    pil_image = Image.fromarray(image)
    bio = io.BytesIO()
    pil_image.save(bio, "PNG")
    bio.seek(0)
    b64image = base64.b64encode(bio.read())

    return "data:image/jpeg;base64," + str(b64image).split("'")[1]


def base64_to_numpy(image: str) -> NDArray[np.uint8]:
    image = image.split(",")[1]  # Remove B64 header
    base64_decoded = base64.b64decode(image)
    image = Image.open(io.BytesIO(base64_decoded))
    return np.array(image, dtype=np.uint8)

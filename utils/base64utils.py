import io
import base64
import numpy as np

from PIL import Image
from numpy.typing import NDArray


def numpy_to_base64(image: NDArray[np.uint8]) -> str:
    return base64.b64encode(image).decode("utf-8")


def base64_to_numpy(image: str) -> NDArray[np.uint8]:
    base64_decoded = base64.b64decode(image)
    image = Image.open(io.BytesIO(base64_decoded))
    return np.array(image, dtype=np.uint8)

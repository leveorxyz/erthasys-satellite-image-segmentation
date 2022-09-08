import base64
import numpy as np

from numpy.typing import NDArray


def numpy_to_base64(image: NDArray[np.uint8]) -> bytes:
    return base64.b64encode(image)


def base64_to_numpy(image: bytes, shape: tuple[int, int, int]) -> NDArray[np.uint8]:
    decoded_image = np.frombuffer(base64.b64decode(image), np.uint8)
    return decoded_image.reshape(shape)

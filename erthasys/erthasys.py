import numpy as np
import tensorflow as tf

from numpy.typing import NDArray
from .model import InceptionV2UNet


class ErthaSys(InceptionV2UNet):
    def __init__(self, img_size: int):
        super().__init__(img_size)
        self.img_size = img_size
        self.classes = ["Building", "Land", "Road", "Vegetation",
                        "Water", "Unlabeled"]
        self.colormap = {
            0: (60, 16, 152),       # Building
            1: (132, 41, 246),      # Land
            2: (110, 193, 228),     # Road
            3: (254, 221, 58),      # Vagetation
            4: (226, 169, 41),      # Water
            5: (155, 155, 155)      # Unlabeled
        }

    def preprocess_image(self, image: NDArray[np.uint8]) -> NDArray[np.uint8]:
        image = tf.image.resize(image, size=(self.img_size, self.img_size))
        return tf.expand_dims(self.preprocess(image), axis=0)

    def load_weights(self, weight_path: str) -> None:
        self.model.load_weights(weight_path)

    def post_process_prediction(
        self,
        prediction_one_hot: NDArray[np.uint8]
    ) -> NDArray[np.uint8]:

        single_layer = np.argmax(prediction_one_hot, axis=-1)
        output = np.zeros(prediction_one_hot.shape[:2]+(3,), dtype=np.uint8)

        for k in self.colormap.keys():
            output[single_layer == k] = self.colormap[k]

        return np.uint8(output)

    def get_class_distribution(self, image: NDArray[np.uint8]) -> dict:
        class_distribution = {}
        n_pixels = (self.img_size * self.img_size)
        for classname in self.classes:
            class_distribution[classname] = \
                np.sum(image == self.classes.index(classname)) / n_pixels

        return class_distribution

    def get_segmented_image(
        self,
        image: NDArray[np.uint8]
    ) -> tuple[NDArray[np.uint8], dict]:

        preprocessed_image = self.preprocess_image(image)
        prediction_one_hot = self.model.predict(preprocessed_image, verbose=0)
        prediction = np.argmax(prediction_one_hot, axis=-1)
        class_distribution = self.get_class_distribution(prediction)

        return self.post_process_prediction(
            np.squeeze(prediction_one_hot)
        ), class_distribution

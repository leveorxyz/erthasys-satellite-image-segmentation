from tensorflow import keras
import tensorflow as tf
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

model = keras.models.load_model(
    "segmentation/models/InceptionResNetV2-UNet.h5"
)

model.summary()

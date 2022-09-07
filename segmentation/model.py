import tensorflow as tf


class InceptionV2UNet:
    def __init__(self, img_size: int = 512):
        self.img_size = img_size

    @staticmethod
    def conv_block(input, num_filters):
        x = tf.keras.layers.Conv2D(num_filters, 3, padding="same")(input)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Activation("relu")(x)

        x = tf.keras.layers.Conv2D(num_filters, 3, padding="same")(x)
        x = tf.keras.layers.BatchNormalization()(x)
        x = tf.keras.layers.Activation("relu")(x)

        return x

    @staticmethod
    def decoder_block(input, skip_features, num_filters):
        x = tf.keras.layers.Conv2DTranspose(
            num_filters, (2, 2), strides=2, padding="same")(input)
        x = tf.keras.layers.Concatenate()([x, skip_features])
        x = InceptionV2UNet.conv_block(x, num_filters)

        return x

    def __call__(self):
        """ Input """
        input_shape = (self.img_size, self.img_size, 3)
        inputs = tf.keras.layers.Input(input_shape)

        """ Pre-trained InceptionResNetV2 Model """
        encoder = tf.keras.layers.InceptionResNetV2(
            include_top=False, weights="imagenet", input_tensor=inputs)

        """ Encoder """
        s1 = encoder.get_layer("input_1").output  # (512 x 512)

        s2 = encoder.get_layer("activation").output  # (255 x 255)
        s2 = tf.keras.layers.ZeroPadding2D(((1, 0), (1, 0)))(s2)  # (256 x 256)

        s3 = encoder.get_layer("activation_3").output  # (126 x 126)
        s3 = tf.keras.layers.ZeroPadding2D((1, 1))(s3)  # (128 x 128)

        s4 = encoder.get_layer("activation_74").output  # (61 x 61)
        s4 = tf.keras.layers.ZeroPadding2D(((2, 1), (2, 1)))(s4)  # (64 x 64)

        """ Bridge """
        b1 = encoder.get_layer("activation_161").output  # (30 x 30)
        b1 = tf.keras.layers.ZeroPadding2D((1, 1))(b1)  # (32 x 32)

        """ Decoder """
        d1 = self.decoder_block(b1, s4, 512)  # (64 x 64)
        d2 = self.decoder_block(d1, s3, 256)  # (128 x 128)
        d3 = self.decoder_block(d2, s2, 128)  # (256 x 256)
        d4 = self.decoder_block(d3, s1, 64)  # (512 x 512)

        """ Output """
        dropout = tf.keras.layers.Dropout(0.3)(d4)
        outputs = tf.keras.layers.Conv2D(
            6, 1, padding="same", activation="softmax")(dropout)

        model = tf.keras.layers.Model(
            inputs, outputs, name="InceptionResNetV2-UNet")
        return model

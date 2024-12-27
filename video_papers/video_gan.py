# video_gan.py

import tensorflow as tf
from tensorflow.keras import layers

class VideoGAN:
    def __init__(self):
        self.generator = self.build_generator()
        self.discriminator = self.build_discriminator()

    def build_generator(self):
        model = tf.keras.Sequential()
        model.add(layers.Dense(256, input_dim=100))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.Reshape((4, 4, 16)))
        model.add(layers.Conv2DTranspose(128, kernel_size=5, strides=2, padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.Conv2DTranspose(64, kernel_size=5, strides=2, padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.Conv2DTranspose(3, kernel_size=5, activation='tanh', padding='same'))
        return model

    def build_discriminator(self):
        model = tf.keras.Sequential()
        model.add(layers.Conv2D(64, kernel_size=5, strides=2, padding='same', input_shape=(64, 64, 3)))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.Conv2D(128, kernel_size=5, strides=2, padding='same'))
        model.add(layers.LeakyReLU(alpha=0.2))
        model.add(layers.Flatten())
        model.add(layers.Dense(1, activation='sigmoid'))
        return model

    def compile_models(self):
        self.discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.generator.compile(loss='binary_crossentropy', optimizer='adam')

# Example usage
if __name__ == "__main__":
    video_gan = VideoGAN()
    video_gan.compile_models()
    print("VideoGAN models compiled successfully.")

# -*- coding: utf-8 -*-
"""convert to onnx.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1laKK6xFYyyusqZFwjXwZ7vzx_F0KYE7c
"""

import tensorflow as tf
import tf2onnx

# Load your Keras model
model = tf.keras.models.load_model('audio_classification_spectrogram.keras')
model.output_names=['output']

# Define input signature matching your model's input shape
input_signature = [tf.TensorSpec((None, 32, 32, 1), tf.float32, name="input_spectrogram")]

# Convert using tf2onnx
onnx_model, _ = tf2onnx.convert.from_keras(
    model,
    input_signature=input_signature,
    opset=13,
    output_path="audio_classification_spectrogram.onnx"
)
import numpy as np
import tensorflow as tf


INPUT_TENSOR_NAME = 'image_tensor:0'


def serving_input_fn():
    inputs = {INPUT_TENSOR_NAME: tf.placeholder(tf.uint8, [None, None, None, 3])}
    return tf.estimator.export.ServingInputReceiver(inputs, inputs)

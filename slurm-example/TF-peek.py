
import tensorflow as tf
from tensorflow.keras import Model, layers
import numpy as np

gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    print("Name:", gpu.name, "Type:", gpu.device_type)

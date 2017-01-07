import numpy as np

def init_weights_uniform(shape):
    return np.random.uniform(shape[0], shape[1]) / np.sqrt(shape[0] + shape[1])
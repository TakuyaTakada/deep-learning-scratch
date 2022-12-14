import numpy as np


def step_function(x):
    y = x > 0
    return y.astype(np.int)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def rectified_liner_unit(x):
    return np.maximum(0, x)

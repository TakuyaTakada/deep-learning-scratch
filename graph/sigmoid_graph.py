import numpy as np

from deepl_scratch import sigmoid
from show import show_graph


def show_sigmoid_graph():
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    show_graph(x, y)


if __name__ == '__main__':
    show_sigmoid_graph()

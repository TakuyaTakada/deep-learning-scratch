import numpy as np

from deepl_scratch import step_function
from show import show_graph


def show_step_graph():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step_function(x)
    show_graph(x, y)


if __name__ == '__main__':
    show_step_graph()

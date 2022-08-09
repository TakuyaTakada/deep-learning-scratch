import numpy as np


class Perceptron:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def out(self, x1, x2):
        x = np.array([x1, x2])
        w = np.array([self.weight, self.weight])
        tmp = np.sum(w * x) + self.bias
        if tmp <= 0:
            return 0
        return 1


class AndGate(Perceptron):
    def __init__(self):
        super().__init__(0.5, -0.7)

    def out(self, x1, x2):
        return super().out(x1, x2)


class NandGate(Perceptron):
    def __init__(self):
        super().__init__(-0.5, 0.7)

    def out(self, x1, x2):
        return super().out(x1, x2)


class OrGate(Perceptron):
    def __init__(self):
        super().__init__(0.5, -0.2)

    def out(self, x1, x2):
        return super().out(x1, x2)


class XorGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.nand_gate = NandGate()
        self.or_gate = OrGate()

    def out(self, x1, x2):
        s1 = self.nand_gate.out(x1, x2)
        s2 = self.or_gate.out(x1, x2)
        return self.and_gate.out(s1, s2)

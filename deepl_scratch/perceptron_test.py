import pytest

from .perceptron import AndGate, NandGate, OrGate, XorGate


@pytest.mark.parametrize(['x1', 'x2', 'expected'], [
    (0, 0, 0),
    (1, 0, 0),
    (0, 1, 0),
    (1, 1, 1),
])
def test_and_gate(x1, x2, expected):
    assert AndGate().out(x1, x2) == expected


@pytest.mark.parametrize(['x1', 'x2', 'expected'], [
    (0, 0, 1),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 0),
])
def test_nand_gate(x1, x2, expected):
    assert NandGate().out(x1, x2) == expected


@pytest.mark.parametrize(['x1', 'x2', 'expected'], [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
])
def test_or_gate(x1, x2, expected):
    assert OrGate().out(x1, x2) == expected


@pytest.mark.parametrize(['x1', 'x2', 'expected'], [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 0),
])
def test_xor_gate(x1, x2, expected):
    assert XorGate().out(x1, x2) == expected

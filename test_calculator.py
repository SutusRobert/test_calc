import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(1,2) == 3
    assert add(5,5) == 10
    assert add(-1,-1) == -2
    assert add(1,-1) == 0
    assert add(0,0) == 0 


def test_subtract():
    assert subtract(4,2) == 2
    assert subtract(10,2) == 8
    assert subtract(-2,2) == -4
    assert subtract(0,-2) == 2


def test_multiply():
    assert multiply(4,2) == 8
    assert multiply(10,2) == 20
    assert multiply(12,2) == 24
    assert multiply(0,-2) == 0


def test_divide():
    assert divide(4,2) == 2
    assert divide(10,2) == 5
    assert divide(3,2) == 1.5
    assert divide(625,5) == 125 
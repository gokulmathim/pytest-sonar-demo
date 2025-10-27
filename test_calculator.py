from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(8, 2) == 4
    with pytest.raises(ValueError):
        divide(5, 0)

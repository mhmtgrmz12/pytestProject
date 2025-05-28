import pytest
from main import add, subtract, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, -1) == -2
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(-9, 3) == -3
    assert divide(0, 1) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(5, 0)

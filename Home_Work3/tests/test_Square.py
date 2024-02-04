from Home_Work2.src.Square import Square
import pytest


def test_square_area():
    square = Square(5)
    assert square.get_area() == 25


def test_square_perimeter():
    square = Square(5)
    assert square.get_perimetr() == 20


def test_invalid_square_creation():
    with pytest.raises(ValueError):
        square = Square(-1)


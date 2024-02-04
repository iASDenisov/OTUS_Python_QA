from Home_Work2.src.Rectangle import Rectangle
import pytest


def test_rectangle_area():
    rectangle = Rectangle(3, 4)
    assert rectangle.get_area() == 12


def test_rectangle_perimeter():
    rectangle = Rectangle(3, 4)
    assert rectangle.get_perimetr() == 14


def test_invalid_rectangle_creation():
    with pytest.raises(ValueError):
        rectangle = Rectangle(-1, 4)


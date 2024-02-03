from Home_Work1.src.Circle import Circle
from math import pi
import pytest


def test_circle_init_valid_radius():
    """test """
    circle = Circle(5)
    assert circle.radius == 5


def test_circle_init_invalid_radius():
    """test """
    with pytest.raises(ValueError):
        circle = Circle(-1)


def test_circle_get_area():
    """test """
    circle = Circle(5)
    assert circle.get_area() == pi * (5 * 2)


def test_circle_get_perimeter():
    """test """
    circle = Circle(5)
    assert circle.get_perimetr() == 2 * pi * 5

import pytest
from Home_Work2.src.Triangle import Triangle


def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert triangle.get_area() == 6


def test_triangle_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.get_perimetr() == 12


def test_invalid_triangle_creation_negative_side():
    with pytest.raises(ValueError):
        triangle = Triangle(-1, 2, 3)


def test_invalid_triangle_creation_invalid_sides():
    with pytest.raises(ValueError):
        triangle = Triangle(1, 1, 3)


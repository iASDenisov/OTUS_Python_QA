from Home_Work1.src.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name="Circle")
        if radius <= 0:
            raise ValueError("Нельзя создать круг!")
        self.radius = radius

    def get_area(self):
        return pi * (self.radius * 2)

    def get_perimetr(self):
        return 2 * pi * self.radius

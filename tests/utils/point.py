import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def slope_to(self, other):
        difference_point = other - self
        slope = difference_point.y / difference_point.x
        return slope

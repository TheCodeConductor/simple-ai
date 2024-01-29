from tests.utils.point import Point


class Line:
    def __init__(self, first_point: Point, second_point: Point):
        self.first_point = first_point
        self.second_point = second_point

    def get_slope(self) -> float:
        return self.first_point.slope_to(self.second_point)

    def sample_value_at(self, x: float) -> float:
        return (
                self.get_slope() * (x - self.first_point.x)
                + self.first_point.y
        )

    def is_point_on_line(self, point: Point):
        return point == Point(point.x, self.sample_value_at(point.x))

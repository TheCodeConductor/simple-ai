from tests.utils.line import Line
from tests.utils.point import Point


def test_get_slope():
    first_point = Point(1.23, 4.56)
    second_point = Point(-2.34, 6.78)
    line = Line(first_point, second_point)

    slope = line.get_slope()
    expected_slope = (6.78 - 4.56) / (-2.34 - 1.23)
    assert slope == expected_slope


def test_sample_value():
    first_point = Point(1.0, 2.0)
    second_point = Point(3.0, 3.0)
    line = Line(first_point, second_point)

    sampled_y = line.sample_value_at(7.0)
    expected_y = line.get_slope() * (7.0 - first_point.x) + first_point.y
    assert sampled_y == expected_y


def test_is_point_on_line():
    first_point = Point(5.0, 6.0)
    second_point = Point(-2.0, 7.0)
    line = Line(first_point, second_point)

    third_point = Point(-9.0, line.sample_value_at(-9.0))
    assert line.is_point_on_line(third_point)




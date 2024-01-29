import math


from tests.utils.point import Point


def test_equals():
    first_point = Point(2.4, 6.7)
    second_point = Point(2.4, 6.7)
    assert first_point == second_point


def test_add():
    first_point = Point(3.2, 4.6)
    second_point = Point(-5.7, 2.3)
    sum_point = first_point + second_point
    assert sum_point == Point(-2.5, 6.9)


def test_sub():
    first_point = Point(3.2, 4.6)
    second_point = Point(-5.7, 2.2)
    difference_point = first_point - second_point
    assert difference_point == Point(8.9, 2.4)


def test_slope_to():
    first_point = Point(3.2, 4.6)
    second_point = Point(-5.7, 2.2)
    slope = first_point.slope_to(second_point)
    expected_slope = (2.2 - 4.6) / (-5.7 - 3.2)
    assert slope == expected_slope


def test_str():
    point = Point(5.6, 2.9)
    string = str(point)
    assert string == "(5.6, 2.9)"



import pytest
from lab_4._01_circle import radius, pi, point_1, point_2


def test_circle_area():
    expected_area = pi * radius ** 2
    assert round(expected_area, 4) == 5541.7676


def test_point_inside_circle():
    distance_to_origin = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
    assert distance_to_origin <= radius


def test_point_outside_circle():
    distance_to_origin = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
    assert distance_to_origin > radius

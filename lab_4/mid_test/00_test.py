import pytest
from lab_4._00_distance import sites, distances


def test_moscow_london():
    assert distances['Moscow']['Moscow - London'] == ((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5


def test_moscow_paris():
    assert distances['Moscow']['Moscow - Paris'] == ((sites['Moscow'][0] - sites['Paris'][0]) ** 2 + (sites['Moscow'][1] - sites['Paris'][1]) ** 2) ** 0.5


def test_london_paris():
    assert distances['London']['London - Paris'] == ((sites['London'][0] - sites['Paris'][0]) ** 2 + (sites['London'][1] - sites['Paris'][1]) ** 2) ** 0.5


def test_moscow_london_from_london():
    assert distances['London']['Moscow - London'] == ((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5


def test_moscow_paris_from_paris():
    assert distances['Paris']['Moscow - Paris'] == ((sites['Moscow'][0] - sites['Paris'][0]) ** 2 + (sites['Moscow'][1] - sites['Paris'][1]) ** 2) ** 0.5


def test_london_paris_from_paris():
    assert distances['Paris']['London - Paris'] == ((sites['London'][0] - sites['Paris'][0]) ** 2 + (sites['London'][1] - sites['Paris'][1]) ** 2) ** 0.5

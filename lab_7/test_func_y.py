import pytest
from lab1 import y

t1 = y(3, 2)


def test_y():
    assert t1 == 64.0

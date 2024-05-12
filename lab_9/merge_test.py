import pytest
from lab import merge, s1, s2, s3


def test_merge():
    expected_output = [0, 4, 7, 1, 5, 8, 2, 6, 9, 3, 10]
    assert list(merge(s1, s2, s3)) == expected_output
    assert list(merge([1, 4, 7], [2, 5, 8], [3, 6, 9])) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

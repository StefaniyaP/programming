import pytest
from lab_4._02_operations import result


def test_result():
    expected_res = 25
    assert result == expected_res

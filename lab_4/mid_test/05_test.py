import pytest
from lab_4._05_zoo import zoo, lion_index, lark_index


def test_zoo():
    expected_zoo = ['lion', 'bear', 'kangaroo', 'monkey', ['rooster', 'ostrich', 'lark']]
    assert zoo == expected_zoo


def test_find_lion_and_lark():
    assert lion_index == 1
    assert lark_index == 7

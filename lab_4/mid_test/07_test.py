import pytest
from lab_4._07_secret import secret_str


def test():
    expected_str = 'в бане веник дороже денег'
    assert secret_str == expected_str

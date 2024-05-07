import pytest
from lab_4._06_songs_list import print1, print2


def test():
    expected_p1 = 'Три песни звучат 14.93 минут'
    expected_p2 = 'А другие три песни звучат 13.0 минут'
    assert expected_p1 == print1
    assert expected_p2 == print2

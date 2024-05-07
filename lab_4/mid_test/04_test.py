import pytest
from lab_4._04_my_family import f_height, t_height


def test_print_father_height():
    assert f_height == 'Рост отца - 172 см'


def test_calculate_total_height():
    assert t_height == 'Общий рост моей семьи - 489 см'

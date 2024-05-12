import pytest
from lab_7.lab import create_n_dim_array

t1 = create_n_dim_array(1, 3)
t2 = create_n_dim_array(2, 3)
t3 = create_n_dim_array(3, 2)


def test_create_n_dim_array():
    # Тестирование 1-мерного массива
    assert t1 == ['level 3', 'level 3', 'level 3']

    # Тестирование 2-мерного массива
    assert t2 == [['level 3', 'level 3', 'level 3'],
                  ['level 3', 'level 3', 'level 3'],
                  ['level 3', 'level 3', 'level 3']]

    # Тестирование 3-мерного массива
    assert t3 == [[['level 2', 'level 2'],
                   ['level 2', 'level 2']],
                  [['level 2', 'level 2'],
                   ['level 2', 'level 2']]]

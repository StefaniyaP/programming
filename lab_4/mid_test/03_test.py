import pytest
from lab_4._03_favorite_movies import my_favorite_movies

expected_results = ('Терминатор', 'Назад в будущее', 'Пятый элемент', 'Чужие')


def test_movie_indices():
    assert my_favorite_movies[:10:] == expected_results[0]
    assert my_favorite_movies[42:] == expected_results[1]
    assert my_favorite_movies[12:25:] == expected_results[2]
    assert my_favorite_movies[-22:-17:] == expected_results[3]

# Прог. Лабораторная работа №4
## Задание:
1. Скачать архив с заданиями и распаковать его в свой репозиторий
2. оформить отчет в ```readme.md```. По каждому из заданий - описание задачи, скриншот работы программы

Сложность well-done:     
Покрыть реализованную фукциональность тестами с использованием `pytest`.     
     
## Ход работы:
Был скачан архив и распакован в репозиторий [programming](https://github.com/StefaniyaP/programming.git).     
### Задание 00_distance.py
Был дан словарь    
![image](https://github.com/StefaniyaP/programming/assets/144994975/82aa0160-7cfd-47c5-9586-0fedf99fd889)    
Необходимо было составить словарь словарей расстояний между ними. Дана формула расстояния на координатной сетке: ```((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5```.   
Решение и вывод:    
![image](https://github.com/StefaniyaP/programming/assets/144994975/6720a3b2-0105-4eda-9307-a72076cc1114)  

### Задание 01_circle.py
1) Вычислить значение площади круга по данному радиусу ```radius = 42```     
   Решение:    
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/e0d69052-93c8-494d-9139-51368cd6ab10)       
   Вывод:      
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/d935e5db-019f-4468-8f25-69194a4d82b1)  

3) Далее даны координаты точки ```point_1 = (23, 34)``` и следующее задание:      
   _Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42], то выведите на консоль True, Или False, если точка лежит вовне круга.       
 подсказки:        
       нужно определить расстояние от этой точки до начала координат (0, 0)       
       формула так же есть в интернете      
       квадратный корень - это возведение в степень 0.5      
       операции сравнения дают булевы константы True и False_      
   Решение:       
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/b13573bb-a2d0-435d-a226-26f93dc4b255)       
   Вывод:     
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/f32f37d7-31f9-489d-bcda-41517a104059)         
4) Аналогичо для другой точки ```point_2 = (30, 30)```
   Решение:       
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/ee713109-c38f-419b-a4ae-4404be4b0b07)       
   Вывод:       
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/27363c09-dd8f-4a3d-8173-233ad7e1f3cf)        

### Задание 02_operations.py
_Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25". Использовать нужно только указанные знаки операций, но не обязательно все перечесленные. Порядок чисел нужно сохранить._     
Решение:      
![image](https://github.com/StefaniyaP/programming/assets/144994975/85584208-406e-446e-b7fa-9020f26739e4)     
Вывод:     
![image](https://github.com/StefaniyaP/programming/assets/144994975/b87ec1b8-fe49-4621-b7a8-d30a2f51f7e5)     

### Задание 03_favorite_movies.py
Дана строка с перечислением фильмов:```my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'```. Задание:    
_Выведите на консоль с помощью индексации строки, последовательно:     
   первый фильм     
   последний     
   второй    
   второй с конца     
 Запятая не должна выводиться. Переопределять my_favorite_movies нельзя. Использовать .split() или .find() или другие методы строки нельзя - пользуйтесь только срезами, как указано в задании!_     
 Решение:      
 ![image](https://github.com/StefaniyaP/programming/assets/144994975/fa461986-840a-4c05-94d0-a98e343f461f)         
 Вывод:      
 ![image](https://github.com/StefaniyaP/programming/assets/144994975/e6d3d88b-7482-4e2c-899f-ee6141bab6a0)        

### Задание 04_my_family.py
1) Создать списки: моя семья, список списков приблизительного роста членов семьи.      
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/ccb2a5ff-291d-407b-b7e8-0f57025c0878)     
2) Вывести на консоль рост отца в формате     
   ```Рост отца - ХХ см```     
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/1f86bcfc-9457-4664-9b2b-561ab39f30f3)    
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/92b8f851-b825-4747-9e91-24196e3f0ffd)     
3) Вывести общий рост семьи как сумму ростов всех членов    
    ```Общий рост моей семьи - ХХ см```      
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/e022a90c-4407-495c-9d6e-6631fafe3732)     
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/eb006c44-57d1-4076-a157-d228ef7acb52)      

### Задание 05_zoo.py
Дан список животных в зоопарке:  ```zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]```      
1)_посадите медведя (bear) между львом и кенгуру и выведите список на консоль_   
![image](https://github.com/StefaniyaP/programming/assets/144994975/e2c559ea-1e5c-4274-8682-34ef540f23d3)      
![image](https://github.com/StefaniyaP/programming/assets/144994975/e31f6c89-2e15-4d5d-b68b-cf4077c728ea)        
2)_добавьте птиц из списка birds в последние клетки зоопарка_ ```birds = ['rooster', 'ostrich', 'lark', ]``` _и выведите список на консоль_     
![image](https://github.com/StefaniyaP/programming/assets/144994975/3776a269-4c81-4f02-a70e-afb4587c273f)      
![image](https://github.com/StefaniyaP/programming/assets/144994975/44861140-2f65-46f9-b179-197b2cf58e29)        
3)_уберите слона и выведите список на консоль_    
![image](https://github.com/StefaniyaP/programming/assets/144994975/ef8f9608-ec3c-4ca5-961c-5c37d42ad137)    
![image](https://github.com/StefaniyaP/programming/assets/144994975/cbffb686-7264-48a8-8a57-82bc22f2ca37)    
4)_выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark). Номера при выводе должны быть понятны простому человеку, не программисту._    
![image](https://github.com/StefaniyaP/programming/assets/144994975/ff8119d0-925e-4898-9ba1-a01036921860)      
![image](https://github.com/StefaniyaP/programming/assets/144994975/58474cfb-3024-4333-82bc-06ddf67215a9)     

### Задание 06_songs_list.py
Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут     
```
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]
```       
_распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате     
   ```Три песни звучат ХХХ.XX минут```_     
       ![image](https://github.com/StefaniyaP/programming/assets/144994975/bb96d0e6-1079-4098-a24c-e78cf0f8ac36)          
       ![image](https://github.com/StefaniyaP/programming/assets/144994975/1da104eb-f955-451f-a350-16bf23afa07c)     
       Есть словарь песен группы Depeche Mode:    
```
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}
```
 _распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'     
   ```А другие три песни звучат ХХХ минут```_     
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/62d1ea99-15f1-4c9b-9896-d686115ea0eb)         
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/aee5c602-e16e-4a39-841f-528f90db7573)  

### Задание 07_secret.py
Есть зашифрованное сообщение:    
```
secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]
```
_Нужно его расшифровать и вывести на консоль в удобочитаемом виде. Должна получиться фраза на русском языке, например: как два байта переслать.
Ключ к расшифровке:     
   первое слово - 4-я буква     
   второе слово - буквы с 10 по 13, включительно       
   третье слово - буквы с 6 по 15, включительно, через одну   
   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке    
   пятое слово - буквы с 17 по 21, включительно, в обратном порядке     
   4е и 5е слова нужно получить за 1 срез_    
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/49b5eba1-b2ff-4611-aa15-cd7f5a6844b2)    
   ![image](https://github.com/StefaniyaP/programming/assets/144994975/aedb932e-5fbc-4276-9425-d431a0f20dac)        

### Задание 08_garden.py
_в саду сорвали цветы
```garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )```_   
_на лугу сорвали цветы
```meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )```_    _создайте множество цветов, произрастающих в саду и на лугу_    
![image](https://github.com/StefaniyaP/programming/assets/144994975/c855e88e-5f9f-4d6c-a356-f20c28922879)     
_выведите на консоль все виды цветов_     
![image](https://github.com/StefaniyaP/programming/assets/144994975/d5ab92ce-f326-4380-8bc4-1dda6056c50a)     
![image](https://github.com/StefaniyaP/programming/assets/144994975/14f89a10-b2f6-4fd3-bc07-21c7dd7f444a)      
_выведите на консоль те, которые растут и там и там_       
![image](https://github.com/StefaniyaP/programming/assets/144994975/c5af6366-1793-44ac-b407-00578739016b)       
![image](https://github.com/StefaniyaP/programming/assets/144994975/4766c80b-abc3-400a-8278-c8726bbf90c4)       
 _выведите на консоль те, которые растут в саду, но не растут на лугу_     
 ![image](https://github.com/StefaniyaP/programming/assets/144994975/bf914dff-bdce-4bd1-8be3-458b80027852)       
 ![image](https://github.com/StefaniyaP/programming/assets/144994975/f04d5668-8f77-4c50-b1d6-c4034d3980f1)       
 _выведите на консоль те, которые растут на лугу, но не растут в саду_     
![image](https://github.com/StefaniyaP/programming/assets/144994975/7a08a436-645a-4d08-933a-c45dbbb50fc7)        
![image](https://github.com/StefaniyaP/programming/assets/144994975/37739167-c14e-4e55-9def-98109384e151)        

### Задание 09_shopping.py
Есть словарь магазинов с распродажами:    
```
shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}
```          
_Создайте словарь цен на продкты следующего вида_        
![image](https://github.com/StefaniyaP/programming/assets/144994975/d2cc7717-5b54-4003-a494-bb3b3e53a80e)         
_Указать надо только по 2 магазина с минимальными ценами_

### Задание 10_store.py
Есть словарь кодов товаров:    
```
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
```
Есть словарь списков количества товаров на складе:    
```
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
```
_Рассчитать на какую сумму лежит каждого товара на складе       
Вывести стоимость каждого вида товара на складе:     
один раз распечать сколько всего столов и их общая стоимость,     
один раз распечать сколько всего стульев и их общая стоимость,    
   и т.д. на складе     
 Формат строки ```<товар> - <кол-во> шт, стоимость <общая стоимость> руб```_     
 ![image](https://github.com/StefaniyaP/programming/assets/144994975/fd6091c3-5a4c-4118-9f0c-6da54254e340)         
 ![image](https://github.com/StefaniyaP/programming/assets/144994975/f01045b6-cb53-4ec8-a884-34299aae9802)     
 ![image](https://github.com/StefaniyaP/programming/assets/144994975/6f8877fc-b5b5-4e7c-bb49-cb9cacad4829)      

## Well-done 
### Задание 00_distance.py
Был создан файл `00_test.py`, в котором были реализованы тесты при помощи `pytest`. Тестовые функции начинаются с `test_` и проверяют, что расстояния между городами вычисляются корректно. `assert` - 'nj булево выражение, которое проверяет истинность условия:     
```Python
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
```
Вывод:    
![image](https://github.com/StefaniyaP/programming/assets/144994975/7768e912-54fb-4bd3-92f3-f352c0b6407c) 

### Задание 01_circle.py
Тесты `test_circle_area`, `test_point_inside_circle` и `test_point_outside_circle` проверяют соответственно:    
       - правильность вычисления площади круга;       
       - нахождение точки `point_1` внутри круга с радиусом `radius`;          
       - нахождение точки `point_2` вне круга с радиусом `radius`.      
```Python
import pytest
from lab_4._01_circle import radius, pi, point_1, point_2


def test_circle_area():
    expected_area = pi * radius ** 2
    assert round(expected_area, 4) == 5541.7676


def test_point_inside_circle():
    distance_to_origin = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5
    assert distance_to_origin <= radius


def test_point_outside_circle():
    distance_to_origin = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5
    assert distance_to_origin > radius
```

Вывод:    
![image](https://github.com/StefaniyaP/programming/assets/144994975/367fc8e0-3e4f-4e7b-94db-a0aede12560c)

### Задание _02_operations.py
Тест проверяет, равен ли результат в файле `_02_operations.py` ожидаемому результату, который равен 25.   
```Python
import pytest
from lab_4._02_operations import result


def test_result():
    expected_res = 25
    assert result == expected_res
```
Вывод:    
![image](https://github.com/StefaniyaP/programming/assets/144994975/d0320519-a28c-4117-974e-06d879f345a4)

### Задание 03_favorite_movies.py
Тест проверяет, в правильной ли последовательности (`expected_results`) выводятся фильмы
```Python
import pytest
from lab_4._03_favorite_movies import my_favorite_movies

expected_results = ('Терминатор', 'Назад в будущее', 'Пятый элемент', 'Чужие')


def test_movie_indices():
    assert my_favorite_movies[:10:] == expected_results[0]
    assert my_favorite_movies[42:] == expected_results[1]
    assert my_favorite_movies[12:25:] == expected_results[2]
    assert my_favorite_movies[-22:-17:] == expected_results[3]
```

Вывод:    
![image](https://github.com/StefaniyaP/programming/assets/144994975/ed0d373a-f581-46b4-94a3-74c98a490f7f)

### Задание 04_my_family.py
Тесты проверяют правильность вывода
```Python
import pytest
from lab_4._04_my_family import f_height, t_height


def test_print_father_height():
    assert f_height == 'Рост отца - 172 см'


def test_calculate_total_height():
    assert t_height == 'Общий рост моей семьи - 489 см'
```
Вывод:   
![image](https://github.com/StefaniyaP/programming/assets/144994975/ce0771f2-8d14-445b-a4f0-a9c39c15c0fc)

### Задание 05_zoo.py
Первый тест проверят, правильно ли выведен список. Второй - правильно ли вычислены индексы.
```Python
import pytest
from lab_4._05_zoo import zoo, lion_index, lark_index


def test_zoo():
    expected_zoo = ['lion', 'bear', 'kangaroo', 'monkey', ['rooster', 'ostrich', 'lark']]
    assert zoo == expected_zoo


def test_find_lion_and_lark():
    assert lion_index == 1
    assert lark_index == 7
```

Вывод:   
![image](https://github.com/StefaniyaP/programming/assets/144994975/b83c6774-2392-4c0c-a88f-38dbf6ca2607)

### Задание 06_songs_list.py
Тест проверяет правильность вывода
```Python
import pytest
from lab_4._06_songs_list import print1, print2


def test():
    expected_p1 = 'Три песни звучат 14.93 минут'
    expected_p2 = 'А другие три песни звучат 13.0 минут'
    assert expected_p1 == print1
    assert expected_p2 == print2
```
Вывод:   
![image](https://github.com/StefaniyaP/programming/assets/144994975/7537d671-effb-4042-b857-9574518e465e)

### Задание 07_secret.py
Тест проверяет правильность выведенного секретноого слова
```Python
import pytest
from lab_4._07_secret import secret_str


def test():
    expected_str = 'в бане веник дороже денег'
    assert secret_str == expected_str
```

Вывод:   
![image](https://github.com/StefaniyaP/programming/assets/144994975/fbe0c21c-9102-4d91-869e-9f38ee28110f)

### Задание 08_garden.py


### Задание 09_shopping.py
### Задание 10_store.py

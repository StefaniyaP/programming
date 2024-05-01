import csv
import sqlite3
import pandas as pd

# # Парсинг таблиц с сайта
table1 = pd.read_html('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%8D%D0%BA%D0%B7%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82_%D0%B2_%D0%BE%D0%B1%D0%B8%D1%82%D0%B0%D0%B5%D0%BC%D0%BE%D0%B9_%D0%B7%D0%BE%D0%BD%D0%B5',
                      match='наличие')
table2 = pd.read_html('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%8D%D0%BA%D0%B7%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82_%D0%B2_%D0%BE%D0%B1%D0%B8%D1%82%D0%B0%D0%B5%D0%BC%D0%BE%D0%B9_%D0%B7%D0%BE%D0%BD%D0%B5',
                      match='наличие')

# Удаление лишних столбцов из таблицы "Экзопланеты"
df = table1[0]
df.drop(['Подтверждённое наличие воды', 'Тип звезды', 'Радиус (R⊕)', 'Период обращения (дней)',
         'Эксцентриситет орбиты', 'Большая полуось орбиты (а. е.)', 'Эффективная земная орбита (а. е.)'],
        axis=1, inplace=True)

# Удаление лишних столбцов из таблицы "Типы звезд"
df1 = table2[0]
df1.drop(['Подтверждённое наличие воды', 'Радиус (R⊕)', 'Период обращения (дней)',
          'Эксцентриситет орбиты', 'Масса (M⊕)', 'Температура поверхности (°C)', 'Расстояние до Земли (св. лет)',
          'Большая полуось орбиты (а. е.)', 'Эффективная земная орбита (а. е.)'],
         axis=1, inplace=True)

# # Сохранение таблиц в файлы .csv
# df.to_csv('Exoplanets.csv')
# df1.to_csv('Types_of_stars.csv')

# # Создание таблиц БД с помощью DB API
con = sqlite3.connect('my_db.db')
cur = con.cursor()

# cur.execute('CREATE TABLE Exoplanets (no, name_of_the_planet, weight REAL, surface_temperature REAL, distance_to_the_Ground REAL)')
# cur.execute('CREATE TABLE Types_of_stars (no, name_of_the_planet, types_of_stars)')

file1 = open('Exoplanets.csv')
file2 = open('Types_of_stars.csv')

contents1 = csv.reader(file1)
contents2 = csv.reader(file2)

# Расположение данных в таблицах
# insert_records = 'INSERT INTO Exoplanets (no, name_of_the_planet, weight, surface_temperature, distance_to_the_Ground) VALUES (?, ?, ?, ?, ?)'
# cur.executemany(insert_records, contents1)

# insert_records = 'INSERT INTO Types_of_stars (no, name_of_the_planet, types_of_stars) VALUES (?, ?, ?)'
# cur.executemany(insert_records, contents2)

# Проверка заполненности таблицы
# select_all = 'SELECT * FROM Exoplanets'
# rows = cur.execute(select_all).fetchall()

# Удаление лишних столбцов из таблиц
# cur.execute('ALTER TABLE Types_of_stars DROP COLUMN no')
# cur.execute('ALTER TABLE Types_of_stars DROP COLUMN name_of_the_planet')
# cur.execute('ALTER TABLE Exoplanets DROP COLUMN no')

# # Запросы
# Топ 5 далеких планет
# select_all = 'SELECT name_of_the_planet, distance_to_the_Ground FROM Exoplanets ORDER BY distance_to_the_Ground DESC LIMIT 5'
# rows = cur.execute(select_all).fetchall()

# Топ 3 легких планет
# все прочерки в таблице были заменены на значение 0.0, поэтому производится выборка по массе (weight), где масса > 0
# select_all = 'SELECT name_of_the_planet, weight FROM Exoplanets WHERE weight > 0 ORDER BY weight LIMIT 3'
# rows = cur.execute(select_all).fetchall()

# Топ 5 теплых планет
# select_all = 'SELECT name_of_the_planet, surface_temperature FROM Exoplanets ORDER BY surface_temperature DESC LIMIT 5'
# rows = cur.execute(select_all).fetchall()

# Планеты с группировкой по типам звезд. Выводится тип звезды и количество планет, у которых совпадает этот тип
select_all = 'SELECT *, COUNT(*) AS count_of_planets_whose_star_type_matches FROM Types_of_stars GROUP BY types_of_stars'
rows = cur.execute(select_all).fetchall()

for r in rows:
    print(r)

con.commit()
con.close()

import pandas as pd
import sqlite3

# page = requests.get(url)

# soup = BeautifulSoup(page.text, 'lxml')

table1 = pd.read_html('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%8D%D0%BA%D0%B7%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82_%D0%B2_%D0%BE%D0%B1%D0%B8%D1%82%D0%B0%D0%B5%D0%BC%D0%BE%D0%B9_%D0%B7%D0%BE%D0%BD%D0%B5',
                      match='наличие')
table2 = pd.read_html('https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%8D%D0%BA%D0%B7%D0%BE%D0%BF%D0%BB%D0%B0%D0%BD%D0%B5%D1%82_%D0%B2_%D0%BE%D0%B1%D0%B8%D1%82%D0%B0%D0%B5%D0%BC%D0%BE%D0%B9_%D0%B7%D0%BE%D0%BD%D0%B5',
                      match='наличие')

# Таблица "Экзопланеты"
df = table1[0]
df.drop(['Подтверждённое наличие воды', 'Тип звезды', 'Радиус (R⊕)', 'Период обращения (дней)',
         'Эксцентриситет орбиты', 'Большая полуось орбиты (а. е.)', 'Эффективная земная орбита (а. е.)'],
        axis=1, inplace=True)

# Таблица "Типы звезд"
df1 = table2[0]
df1.drop(['Подтверждённое наличие воды', 'Радиус (R⊕)', 'Период обращения (дней)',
          'Эксцентриситет орбиты', 'Масса (M⊕)', 'Температура поверхности (°C)', 'Расстояние до Земли (св. лет)',
          'Большая полуось орбиты (а. е.)', 'Эффективная земная орбита (а. е.)'],
         axis=1, inplace=True)

# Сохранение таблиц в файлы .csv
df.to_csv('Exoplanets.csv')
df1.to_csv('Types_of_stars.csv')

# Запросы


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

moscow_london = ((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5
moscow_paris = ((sites['Moscow'][0] - sites['Paris'][0]) ** 2 + (sites['Moscow'][1] - sites['Paris'][1]) ** 2) ** 0.5
london_paris = ((sites['London'][0] - sites['Paris'][0]) ** 2 + (sites['London'][1] - sites['Paris'][1]) ** 2) ** 0.5

distances = {
    'Moscow':
    {
        'Moscow - London': moscow_london, 'Moscow - Paris': moscow_paris
    },
    'London':
    {
        'Moscow - London': moscow_london, 'London - Paris': london_paris
    },
    'Paris':
    {
        'Moscow - Paris': moscow_paris, 'London - Paris': london_paris
    }

}

# TODO здесь заполнение словаря

print(distances)





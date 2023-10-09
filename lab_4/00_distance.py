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

x1 = sites['Moscow'][0]
x2 = sites['Moscow'][1]

y1 = sites['London'][0]
y2 = sites['London'][1]

z1 = sites['Paris'][0]
z2 = sites['Paris'][1]

distances = {}

# TODO здесь заполнение словаря

print(distances)





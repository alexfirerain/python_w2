# сборник объектов и подпрограмм для разработки приложений
# версии только чтоб совместимыми были
# PyPI.org - Python Package Index
# Важнейшая конечно математическая:
import math
import math as m  # задание псевдонима
from random import shuffle
from time import strftime

print('Число Пи', m.pi)

# можно не всё пространство имён подключить, экономя память!
from math import pi
from math import sqrt, sin

print("корняшка двух", sqrt(2))

# или даже так
from math import *

# разница видимо в том, что это принудительно грузит всё в память
# "а нечего засорять пространство имён"
print(dir(m))
print(help(m.sinh))
print(help(m.hypot))

# синус 30°
print('синус 30°', round(sin(radians(30)), 3))

###      модуль РАНДОМ       ###
import random as r

num = r.randint(1, 10)
print(num)
for _ in range(10):
    print(r.randint(1, 19))
    print(r.randrange(0, 10, 2), end='|')

nums = list(range(3, 15))
print('\nchoice', r.choice(nums))
for _ in range(37):
    print(r.choice("ОСЛЯБЯ"), end='-')  # чо угодно, кроме словарей и множеств
print()

# но можно так
d = {1: 'a', 2: 'b', 3: 'c'}
keys = list(d.keys())
print(d[r.choice(keys)])

dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
for _ in range(10):
    print(r.choice(dice), r.choice(dice))

# чем отличается чойс от сэмпл
# это выбор без повторов!
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(r.sample(lst, k=5))
abc = "qwertyuioplkjhgfdsazxcvbnm"
s_list = list(abc) + ['1', '2', '#', '$']
r.shuffle(s_list)
print(''.join(s_list[:8]))

# # страдания за пароль
# abc = "qwertyuioplkjhgfdsazxcvbnm"
# abc_cap = abc.upper()
# sym = "!@#$%^&*()_+-="
#
# abc_n = r.randint(1, 6)
# abc_cap_n = r.randint(1, 4)
# sym_n = r.randint(1, 4)
#
# N = 8
# temp = list(abc[:N - 3])
# temp.append(r.choice(abc).upper())
# temp.append(r.choice(nums))
# temp.append(r.choice(sym))
# r.shuffle(temp)
# password = ''.join(temp)
# print(password)

##    ДЭЙТ-ТАЙМ   ##
# идёт от системных часов
import datetime as dt

print(dt.datetime.now())  # выдаёт в особом формате, хотя принт() его хавает
print(dt.datetime.now().date())
print(dt.datetime.now().time())

print(dt.datetime.now()
      .strftime('%d/%m/%Y'))  # выдаёт строку

my_time = dt.time(15, 27, 32)
print(my_time)
my_day = dt.date(2025, 7, 4)
print(my_day)
my_day_time = dt.datetime.combine(my_day, my_time)
print(my_day_time)

date1 = dt.date(2025, 6, 15)
date2 = dt.date(2025, 7, 3)
# delta = dt.timedelta(date2, date1)
print(date2 - date1)

## ПэПринт ##
# для матриц услада
import pprint

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
pprint.pprint(matrix)

## ГРАФИКА ##
# Питоновская Библиотека Изображений
import PIL
# не всегда вспомнишь, какие сторонние библиотеки нужны,
# и какая где: Tools > Sync Python Requirements
# a используй лучше "pip freeze > requirements.txt"
# загрузка в проект так: "pip install -r requirements.txt"
# PIL это для растровых изображений!
# у каждого пикселя есть ряд, место и цвет
# например КЗС (RGB)
# ещё делаем Thumbnails
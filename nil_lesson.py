#
# # неправильно!
# s = set()
# res = s.add('x')
# print(res) # 'None'
#
# s = 'смотреть'
# if s.startswith('смо'):
#     print('это смо')
#
# if s.endswith('еть'):
#     print('это еть')
#
# ss = 'Смотреть, вертеть, видеть'
#
# index = s.find('еть') # даёт индекс первого вхождения
# print(index)
#
# index = s.find('w') # если нет, вернёт -1
# print(index)
#
# """
# 1. find('подстрока') -> индекс первого вхождения
# 2. find('подстрока', start) -> индекс первого вхождения после старта
# 3. find('подстрока', start, end) -> индекс первого вхождения после старта,
#                                     но не далее финиша
# """
# print(ss.find('еть', 6))

ingredient = 'синхрофазотрон'
# сколько букв "о" и на каких позициях
indices = set()
start = 0
while True:
    index = ingredient.find('о', start)
    if index != -1:
        indices.add(index)
        start = index + 1
    else:
        break
print(f'В слове {ingredient} буква "о" встречается {len(indices)} раз на индексах: {indices}')

# Иммутабельная, итерабельная строка
# начала и концы
# 1. replace(what, to_what)
# 2. replace(what, to_what, how_many)
#

s = '+7-812-345-67-89'  # => +7 (812) 345-67-89
res = ''
res = (s.replace('-', ' (', 1)
       .replace('-', ') ', 1))
print(res)

# Срез у строк и других коллекций (упорядоченных, имущих индексы)
# [start:end:step] - как и полагается, начало включительно, конец исключительно
s = 'добрый день'
print(s[0:6:1])
print(s[:6])  # от начала до заданного индекса
print(s[7:])  # от заданного индекса до конца
print(s[5:8])  # от первого до второго (исключительно)
print(s[:-6])  # до символа с конца
print(s[-6:])  # от символа с конца
print(s[::2])  # с шагом два
print(s[::-1])  # реверсия

ingredient = 'потоп'
if ingredient == ingredient[::-1]:
    print(ingredient, 'это палиндром')
else:
    print(ingredient, 'это не палиндром')

words = {"потом", "поток", "лол", "потоп"}

for ingredient in words:
    predicate = " " if ingredient.lower() == ingredient.lower()[::-1] else " не "
    print(f'{ingredient} это{predicate}палиндром')

# в координатах среза выход за границы массива не вызывает ошибок


s = "Дорог Рим город или дорог Миргород"
print(s[-8:] + (s[-15:-9] + '...') * 2)  # Миргород дорог... дорог...

rome = "Дорог Рим"
print(rome[::-1].replace(' ', '').capitalize())  # Миргород

# city = rome[:5][::-1]
# print(city)
# # res = city + ' ' + temp[6:][::-1] + city
# print(res)
# цепочка вызовов съ списком не идёт, методы изменяют и не возвращают

a = ['a', 'b', 'c']
b = a  # теперь обе переменные ведут к одной ячейке памяти
b.append('d')  # добавилось в оба!
print(a, b)
print(id(a), id(b))
c = a.copy()
d = a[:]  # синоним
c.append('e')
d.append('f')
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))

# О, Крошка!
recipe = []
# вводим моржом (до пустой строки) ингредиенты
# выводим нумерованным
while (ingredient := input("Введите ингредиент: ")) != '':
    recipe.append(ingredient)
recipe.sort()
print('Рецепт Окрошки:')
for item in range(len(recipe)):
    print(f'\t{item + 1}. {recipe[item]}')

# для уникализации:
recipe = list(set(recipe))
print(recipe)

stack = []
while (book := input("Название книги: ")) != '':
    stack.append(book)
while stack:
    print(stack.pop())

N = 5
book_list = []
for i in range(N):
    print(f'Кладём книгу {i + 1} в стопку')
    book_list.append(i + 1)
while book_list:
    print(f'Берём книгу {book_list.pop()} из стопки')
  # print(f'Берём книгу {book_list.pop(0)} из стопки') # тогда очередь!


